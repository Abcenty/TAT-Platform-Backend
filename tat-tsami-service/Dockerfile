FROM python:3.11

WORKDIR .

COPY /tat-tsami-service .

RUN python3.11 -m pip install poetry
RUN poetry install --no-dev

CMD poetry run python -m tat_tsami_service.api
