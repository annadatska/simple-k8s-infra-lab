from fastapi import FastAPI
from prometheus_client import start_http_server, Counter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry import trace

app = FastAPI()
REQUESTS = Counter('http_requests_total', 'Total HTTP Requests')

@app.get("/health")
def health():
    REQUESTS.inc()
    return {"status": "ok"}

@app.get("/api/data")
def get_data():
    REQUESTS.inc()
    return {"data": [1, 2, 3]}
