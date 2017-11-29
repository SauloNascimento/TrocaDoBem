FROM ubuntu:latest
MAINTAINER Tainah Emmanuele <tainahemmanuele@gmail.com>

RUN apt-get update
RUN apt-get install -y --no-install-recommends python-pip python-dev build-essential python-setuptools
RUN pip install --upgrade pip
RUN pip install --upgrade virtualenv

COPY ./ /opt/trocadobem

RUN pip install -r /opt/trocadobem/requirements.txt


COPY ./entrypoint.sh /
EXPOSE  8000

CMD ["bash", "/entrypoint.sh" ]
