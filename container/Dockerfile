FROM ubuntu:18.10
MAINTAINER Soichi David Nakahashi <sdn03.tech@gmail.com>

WORKDIR /root/
RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y wget build-essential gcc zlib1g-dev libffi-dev apt-utils unzip git curl xz-utils sudo file make
RUN wget https://www.openssl.org/source/openssl-1.1.1d.tar.gz \
        && tar zxf openssl-1.1.1d.tar.gz \
        && cd openssl-1.1.1d \
        && ./config \
        && make \
        && make install

RUN wget https://www.python.org/ftp/python/3.7.4/Python-3.7.4.tgz \
        && tar zxf Python-3.7.4.tgz \
        && cd Python-3.7.4 \
        && ./configure \
        && make altinstall
ENV PYTHONIOENCODING "utf-8"

WORKDIR /usr/local/bin/
RUN ln -s python3.7 python
RUN ln -s pip3.7 pip

WORKDIR /
COPY requirements.txt requirements.txt
RUN mkdir /app
RUN apt-get install -y mecab libmecab-dev mecab-ipadic mecab-ipadic-utf8 && apt-get clean
RUN mkdir -p /usr/lib/mecab/dic/userdic && \
    git clone https://github.com/neologd/mecab-ipadic-neologd.git \
    && ./mecab-ipadic-neologd/bin/install-mecab-ipadic-neologd -n -a -y

RUN pip install --upgrade pip && pip install -r requirements.txt

RUN wget --no-check-certificate https://ipafont.ipa.go.jp/IPAexfont/IPAexfont00401.zip \
    && unzip -j IPAexfont00401.zip "*.ttf"

EXPOSE 8080
