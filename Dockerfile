# Dockerfile - this is a comment. Delete me if you want.
FROM python:3.6
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
ENTRYPOINT ["python"]
CMD ["app.py"]
