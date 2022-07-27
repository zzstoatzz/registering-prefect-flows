FROM prefecthq/prefect:1.2.4-python3.8

COPY flows/*.py /modules/

COPY pyproject.toml .

ENV PYTHONPATH=$PYTHONPATH:modules/

RUN apt update && apt install --no-install-recommends -y curl && \
    apt clean && rm -rf /var/lib/apt/lists/*

RUN pip install -r requirements.txt