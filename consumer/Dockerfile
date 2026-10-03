FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt && opentelemetry-bootstrap -a install
COPY main.py .
CMD ["opentelemetry-instrument", "--traces_exporter", "otlp", "--metrics_exporter", "none", "python", "main.py"]