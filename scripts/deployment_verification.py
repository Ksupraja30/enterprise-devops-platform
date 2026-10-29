import os
import sys
from urllib.error import URLError
from urllib.request import urlopen


def main() -> int:
    base_url = os.environ.get("APP_URL", "http://127.0.0.1:8000").rstrip("/")
    endpoints = ("/health", "/ready", "/api/v1/system")
    for endpoint in endpoints:
        url = f"{base_url}{endpoint}"
        try:
            with urlopen(url, timeout=10) as response:
                if response.status != 200:
                    print(f"Verification failed: {url} returned HTTP {response.status}", file=sys.stderr)
                    return 1
        except (OSError, URLError) as exc:
            print(f"Verification failed for {url}: {exc}", file=sys.stderr)
            return 1
    print(f"Deployment verification passed: {base_url}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
