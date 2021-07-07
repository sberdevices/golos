# Distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

FROM nvcr.io/nvidia/pytorch:21.03-py3

WORKDIR /workspace

RUN git clone --branch v1.0.2 https://github.com/NVIDIA/NeMo  

WORKDIR /workspace/NeMo   
RUN ./reinstall.sh   
RUN conda install -c anaconda swig   
WORKDIR /workspace/NeMo/scripts/asr_language_modeling/ngram_lm  
RUN sh install_beamsearch_decoders.sh


RUN mkdir /workspace/models
WORKDIR /workspace/models

RUN echo "Download and extract QuartzNet15x5_golos.nemo ..."
RUN wget https://sc.link/ZMv -O QuartzNet15x5_golos.nemo

RUN echo "Download and extract KenLMs ..."
RUN wget https://sc.link/YL0 -O kenlms.tar
RUN tar -xvf kenlms.tar 


WORKDIR /workspace/golos

CMD ["bash"]

#CMD python ./examples/infer.py /workspace/models/QuartzNet15x5_golos.nemo ./examples/data/example1.json -lm /workspace/models/kenlms/lm_commoncrawl.binary

