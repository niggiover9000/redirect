FROM python:3.12-slim

ARG VERSION=latest

EXPOSE 5000

WORKDIR /app

COPY requirements.txt requirements.txt
RUN apt-get update && apt-get upgrade -y
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]