FROM python:3.10.12-alpine3.18
ARG group

LABEL name=tatmis.platform.gateway

# Update packages
RUN apk update && apk add --no-cache &&  \
    apk add --no-cache libc-dev libffi-dev gcc


# Creating a new user, upgrading pip to the latest version
RUN adduser -D -s /bin/bash newuser && \
    python -m pip install --upgrade pip && \
    pip install poetry

# Copy  requirements.txt to install dependencies
WORKDIR /project
COPY pyproject.toml poetry.lock ./

# Installing dependencies to system python
RUN poetry config virtualenvs.create false && \
    poetry install --no-root --no-interaction $group
    #--only main

# Сopy the remaining files
COPY . .
RUN poetry install
#--only main

# Runing the file as an executable script
RUN chmod +x ./scripts/entrypoint.sh

# Changing user
# USER newuser

# Launching the script
ENTRYPOINT [ "./scripts/entrypoint.sh" ]
