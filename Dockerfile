
FROM ubuntu:20.04


RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y python3.11 python3.11-venv python3-pip && \
    apt-get clean


RUN pip3 install poetry

ENV PATH="/root/.local/bin:$PATH"


COPY . /app

WORKDIR /app

RUN poetry install

CMD ["nohup", "poetry", "run", "python", "main.py", "&"]
