FROM prefecthq/prefect:1.2.4-python3.8

COPY flows/*.py /modules/

COPY pyproject.toml .

ENV PYTHONPATH=$PYTHONPATH:modules/


RUN apt update

RUN apt install --no-install-recommends -y curl && \
    apt clean && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python3 \
    && . $HOME/.poetry/env \
    && poetry config virtualenvs.create false \
    && poetry export -f requirements.txt --output requirements.txt --without-hashes \
    && pip install -r requirements.txt \
    && rm -rf /var/lib/apt/lists/*