from prometheus_client import Counter, start_http_server


def start_server():
    start_http_server(8000)


SITE_ACCESSED_COUNTER = Counter(
    'demo_site_accessed',
    'A count of the number of times the site has been accessed'
)
