FROM python:3.11.7-bookworm

ENV \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  # Poetry's configuration:
  POETRY_NO_INTERACTION=1 \
  POETRY_VIRTUALENVS_CREATE=false \
  POETRY_CACHE_DIR='/var/cache/pypoetry' \
  POETRY_HOME='/usr/local' \
  POETRY_VERSION=1.7.1

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install curl build-essential -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

RUN curl -sSL https://install.python-poetry.org | python3 -

WORKDIR /client
COPY pyproject.toml /client/

RUN poetry install --only=main --no-interaction --no-ansi
COPY . /client

ENTRYPOINT [ "poetry", "run", "python", "-m", "gateway" ]
