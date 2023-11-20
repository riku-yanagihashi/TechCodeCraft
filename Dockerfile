FROM python:3.11 AS PYTHON

WORKDIR /work/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM node:21.1.0 AS TAILWIND

WORKDIR /work

COPY package*.json ./
COPY tailwind.config.js ./
RUN npm install
