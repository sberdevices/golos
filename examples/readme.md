# How to run

If you have properly configured NeMo environment you can run example from your environment, or you can run example from docker image.

## Run from docker

>> Minimal driver requirements: NVIDIA Driver release 460.32.03 or later. However, if you are running on Data Center GPUs (formerly Tesla), for example, T4, you may use NVIDIA driver release 418.40 (or later R418), 440.33 (or later R440), 450.51(or later R450). ) see https://docs.nvidia.com/deeplearning/frameworks/pytorch-release-notes/rel_21-03.html#rel_21-03

```bash
cd <this_repository>/examples 
sh build_and_run_docker.sh 
```

After container is started

```
python ./examples/infer.py /workspace/models/QuartzNet15x5_golos.nemo ./examples/data/example1.json -lm /workspace/models/kenlms/lm_commoncrawl.binary
```