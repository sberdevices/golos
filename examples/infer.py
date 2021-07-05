import argparse
import json
import os
import torch

import nemo.collections.asr as nemo_asr

def read_file_list(manifest):
    manifest_path, _ = os.path.split(manifest)
    files, texts = [], []
    with open(manifest, "r") as input_file:
        for line in input_file:
            as_dict = json.loads(line.rstrip('\n'))
            files.append(os.path.join(manifest_path, as_dict["audio_filepath"]))
            texts.append(as_dict["text"])
    return files, texts

def infer_beam_search_lm(files, asr_model, beam_search_lm):
    hyps = []
    logits = torch.tensor(asr_model.transcribe(files, batch_size=20, logprobs=True))
    log_probs_length = torch.tensor([logit.shape[0] for logit in logits])
    logits_tensor = torch.nn.utils.rnn.pad_sequence(logits, batch_first=True)
    for j in range(logits_tensor.shape[0]):
        best_hyp = beam_search_lm.forward(log_probs = logits_tensor[j].unsqueeze(0),
                                          log_probs_length=log_probs_length[j].unsqueeze(0))[0][0][1]
        hyps.append(best_hyp)
    return hyps

def infer_greedy(files, asr_model):
    transcripts = asr_model.transcribe(paths2audio_files=files, batch_size=20)
    return transcripts

def print_mistakes(hyps, refs):
    for hypo, reference in zip(hyps, refs):
        if hypo != reference:
            print(' h', hypo, '\n r', reference)

def _parse_args():
    parser = argparse.ArgumentParser(description='Run inference using NeMo checkpoint')
    parser.add_argument('asr_ckpt', help='Path to ASR NeMo checkpoint file (.nemo)')
    parser.add_argument('manifest', help='Path to manifest where each line is a json with'
                                         ' transcription (.jsonl)')
    parser.add_argument('-lm', help='Path to KenLM binary filem (.binary)', default=None)
    return parser.parse_args()


if __name__ == '__main__':
    args = _parse_args()
    asr_model = nemo_asr.models.EncDecCTCModel.restore_from(args.asr_ckpt)
    asr_model.cuda()

    files, texts = read_file_list(args.manifest)

    hyps = infer_greedy(files, asr_model)
    print_mistakes(hyps, texts)
    print("Greedy WER:", nemo_asr.metrics.wer.word_error_rate(hyps, texts))

    if args.lm:
        beam_search_lm = nemo_asr.modules.BeamSearchDecoderWithLM(
            vocab=list(asr_model.decoder.vocabulary),
            beam_width=16,
            alpha=2, beta=1.5,
            lm_path=args.lm,
            num_cpus=1,
            cutoff_prob=1.0, cutoff_top_n=40,
            input_tensor=True)

        hyps = infer_beam_search_lm(files, asr_model, beam_search_lm)
        print_mistakes(hyps, texts)
        print("Beam search WER:", nemo_asr.metrics.wer.word_error_rate(hyps, texts))
