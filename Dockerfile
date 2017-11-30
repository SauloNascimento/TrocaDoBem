FROM ubuntu:latest
MAINTAINER Tainah Emmanuele <tainahemmanuele@gmail.com>

RUN apt-get update
RUN apt-get install -y --no-install-recommends links net-tools python-pip python-dev build-essential python-setuptools libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
RUN pip install --upgrade pip
RUN pip install --upgrade virtualenv

COPY ./ /opt/trocadobem

RUN pip install -r /opt/trocadobem/requirements.txt


COPY ./entrypoint.sh /
EXPOSE  8000 37289

CMD ["bash", "/entrypoint.sh" ]
