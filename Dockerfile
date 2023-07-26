FROM python:3.10.12-slim-bullseye

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY ./src ./

RUN pip install --no-cache-dir -r requirements.txt

USER 1000

CMD [ "python", "./main.py" ]