FROM ubuntu:16.04

MAINTAINER Sam Murphy <samsammurphy@gmail.com>

RUN apt-get update                              && \
                                                   \
    apt-get install -y --no-install-recommends     \
    bzip2                                          \
    build-essential                                \
    git                                            \
    libssl-dev                                     \
    libffi-dev                                     \
    python3                                        \
    python3-dev                                    \
    python3-pip                                    \
    wget                                           \
                                                && \
    apt-get clean                               && \
    rm -rf /var/lib/apt/lists/*

RUN wget --quiet https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    /bin/bash /Miniconda3-latest-Linux-x86_64.sh -b -p /miniconda                      && \
    rm Miniconda3-latest-Linux-x86_64.sh                                               

ENV PATH=/miniconda/bin:${PATH}          

RUN conda update -y conda                       && \
    conda config --add channels conda-forge     && \
    conda install -y py6s

RUN conda install -c anaconda pip               && \
    pip install earthengine-api oauth2client
    
RUN conda install -y jupyter

EXPOSE 8888




