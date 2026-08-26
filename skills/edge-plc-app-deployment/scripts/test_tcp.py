#!/usr/bin/env python3
"""Minimal TCP reachability test for industrial edge deployments."""

import argparse
import socket
import sys
import time


def main() -> int:
    parser = argparse.ArgumentParser(description="Test TCP reachability to a controller/service endpoint.")
    parser.add_argument("host", help="Controller or service host/IP")
    parser.add_argument("port", type=int, help="TCP port")
    parser.add_argument("--timeout", type=float, default=5.0, help="Timeout in seconds")
    args = parser.parse_args()

    started = time.monotonic()
    try:
        with socket.create_connection((args.host, args.port), args.timeout):
            elapsed_ms = (time.monotonic() - started) * 1000
            print(f"OK {args.host}:{args.port} reachable ({elapsed_ms:.1f} ms)")
            return 0
    except OSError as exc:
        elapsed_ms = (time.monotonic() - started) * 1000
        print(f"FAIL {args.host}:{args.port} unreachable after {elapsed_ms:.1f} ms: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
