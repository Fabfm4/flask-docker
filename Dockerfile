FROM python:3.4
ENV PYTHONUNBUFFERED 1
RUN mkdir /src
RUN mkdir /src/requirements
WORKDIR /src
ADD src/requirements/local.txt /src/requirements/
ADD src/requirements/base.txt /src/requirements/
RUN pip install -r requirements/local.txt
ADD . /src/
