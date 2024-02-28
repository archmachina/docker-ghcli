FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y curl gnupg2 && \
    curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | apt-key add - && \
    echo "deb [arch=amd64] https://cli.github.com/packages stable main" > /etc/apt/sources.list.d/github-cli.list && \
    apt-get update && \
    apt-get install -y gh

ARG BUILD_VERSION
RUN echo "${BUILD_VERSION}" > /build_version.txt

RUN useradd -m -d /work ghcli
USER ghcli:ghcli

ENV HOME /work
WORKDIR /work

ENTRYPOINT [ "/usr/bin/gh" ]
