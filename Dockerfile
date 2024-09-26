# First stage: build the Python app
FROM python:3.10.10 AS build

# install dependencies
COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copie o código da aplicação
COPY . /src

# Defina o diretório de trabalho
WORKDIR /src