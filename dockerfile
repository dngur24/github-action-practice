FROM python:3.12

WORKDIR /flask
COPY app.py .
RUN apt update
RUN apt install -y python3
RUN apt install -y python3-pip
RUN apt install -y python3-flask

CMD [ "flask", "-app", "app.py", "run" ]