import os
import sys
from urllib.error import URLError
from urllib.request import urlopen


def main() -> int:
    url = os.environ.get("HEALTH_CHECK_URL", "http://127.0.0.1:8000/health")
    try:
        with urlopen(url, timeout=5) as response:
            if response.status != 200:
                print(f"Health check failed: HTTP {response.status}", file=sys.stderr)
                return 1
            print(f"Health check passed: {url}")
            return 0
    except (OSError, URLError) as exc:
        print(f"Health check failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
