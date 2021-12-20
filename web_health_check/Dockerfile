# syntax=docker/dockerfile:1
FROM python:3.7-alpine
WORKDIR /web_health_check
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 2499
COPY . .
CMD ["python", "/web_health_check/app.py"]