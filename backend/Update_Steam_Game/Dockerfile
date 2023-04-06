FROM python:3.9.2

WORKDIR /python-docker

COPY requirements.txt requirements.txt 

RUN pip3 install -r requirements.txt 

COPY app.py .
COPY api api

ENV FLASK_APP=app.py

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]