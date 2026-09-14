#!/usr/bin/env python3
"""Preview and count a domain/subdomain list.

Streams a plain .txt or gzip-compressed .txt.gz file line by line, so it never
loads the whole file into memory. Safe on the multi-GB full dataset.

Usage:
    python3 read_sample.py <file> [--head N]

Example:
    python3 read_sample.py data/subdomains-sample.txt --head 20
"""
import argparse
import gzip
import io
import sys


def open_maybe_gzip(path):
    if path.endswith(".gz"):
        return io.TextIOWrapper(gzip.open(path, "rb"), encoding="utf-8", errors="replace")
    return open(path, encoding="utf-8", errors="replace")


def main():
    ap = argparse.ArgumentParser(description="Preview + count a (.gz) name list.")
    ap.add_argument("file")
    ap.add_argument("--head", type=int, default=10, help="rows to preview (default 10)")
    args = ap.parse_args()

    total = 0
    try:
        with open_maybe_gzip(args.file) as fh:
            for line in fh:
                total += 1
                if total <= args.head:
                    sys.stdout.write(line)
    except FileNotFoundError:
        sys.exit(f"not found: {args.file}")

    print(f"\n--- {args.file}: {total:,} names ---", file=sys.stderr)


if __name__ == "__main__":
    main()
