FROM nvcr.io/nvidia/dgl:25.08-py3

ADD . /RE-GCN
WORKDIR /RE-GCN

RUN pip install tqdm pandas rdflib

CMD ["bash"]
