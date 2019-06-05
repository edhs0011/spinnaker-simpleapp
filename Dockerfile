FROM python:3-slim

WORKDIR /
ENV APP_VERSION=v1 \
    FLASK_APP=app.py
STOPSIGNAL SIGINT
CMD ["python", "/app.py"]
RUN pip install flask prometheus_client
COPY app.py /app.py
