FROM python:3.9-alpine3.13

ENV PYTHONUNBUFFERED 1

COPY ./app /app
WORKDIR /app
EXPOSE 8000

ARG DEV=false
COPY /requirements.txt /tmp/
RUN python -m venv /py
ENV PATH="/py/bin:$PATH"
RUN /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    rm -rf /tmp && \
    apk del .tmp-build-deps && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

    USER django-user
