FROM python:2-alpine

ARG GIT_EMAIL
ARG GIT_NAME

ENV PYTHONUNBUFFERED=1

WORKDIR /web

COPY ./src /web/src

RUN set -x \
    && apk update \
    && apk add -u --no-cache \
        bash \
        curl \
        git \
        openssh \
        patch \
    && git config --global user.email "${GIT_EMAIL}" \
    && git config --global user.name "${GIT_NAME}"

CMD ["python", "./src/server.py"]
