import os
import subprocess
import sys


def main() -> int:
    namespace = os.environ.get("KUBERNETES_NAMESPACE", "default")
    deployment = os.environ.get("KUBERNETES_DEPLOYMENT", "monitoring-app")
    command = [
        "kubectl",
        "rollout",
        "undo",
        f"deployment/{deployment}",
        "--namespace",
        namespace,
    ]
    try:
        return subprocess.run(command, check=False).returncode
    except FileNotFoundError:
        print("Rollback failed: kubectl is not installed or not on PATH.", file=sys.stderr)
        return 127


if __name__ == "__main__":
    raise SystemExit(main())
