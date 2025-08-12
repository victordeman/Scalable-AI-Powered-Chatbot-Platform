from prometheus_client import Counter, Histogram

# Define metrics
requests_total = Counter("chatbot_requests_total", "Total API requests")
request_duration = Histogram("chatbot_request_duration_seconds", "Request duration")

def setup_metrics():
    print("Setting up Prometheus metrics...")
