# Install Docker in your system and extension

FROM python:3.8-slim-buster

WORKDIR /app

COPY . /app

RUN pip install -r requirement.txt 

CMD ["python3", "app.py"]