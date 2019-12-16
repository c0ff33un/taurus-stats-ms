# Dockerfile - this is a comment. Delete me if you want.
FROM python:3.6-slim-stretch
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN apt-get update
RUN apt-get install -y default-libmysqlclient-dev
#RUN apt-get install -y python3-dev
RUN apt-get install -y gcc
RUN pip install -r requirements.txt
COPY . /app
ENTRYPOINT ["python"]
CMD ["app.py"]
