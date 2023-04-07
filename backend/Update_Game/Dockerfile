FROM python:3.9.2-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt 

RUN pip3 install -r requirements.txt 

COPY app.py .

COPY config.py .
COPY gameder-1163d-39552ceb875d.json .

COPY api api

ENV FLASK_APP=app.py
ENV STEAM_API_KEY=""

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]