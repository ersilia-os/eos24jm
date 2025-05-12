FROM bentoml/model-server:0.11.0-py38
MAINTAINER ersilia

RUN pip install rdkit==2022.3.3
RUN pip install molvs==0.1.1
RUN pip install scikit-learn==0.24.2

WORKDIR /repo
COPY . /repo
