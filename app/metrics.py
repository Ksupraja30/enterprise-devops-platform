from prometheus_client import Counter

API_REQUEST_COUNT = Counter(
    "api_requests_total",
    "Total API Requests"
)