FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN pip install rdkit
RUN pip install molvs
RUN pip install scikit-learn==0.24.2

WORKDIR /repo
COPY . /repo
