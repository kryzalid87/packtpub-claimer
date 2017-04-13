FROM python:2.7.13-wheezy

RUN apt-get update
RUN apt-get -y install python-pip
COPY requirements.txt packtpub/requirements.txt
COPY ./src packtpub/src
RUN pip install -r packtpub/requirements.txt
WORKDIR packtpub/src

CMD python start.py