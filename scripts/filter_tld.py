#!/usr/bin/env python3
"""Filter a domain/subdomain list by TLD, streaming (low memory).

Prints matching names to stdout. Works on .txt or .txt.gz. Names are ASCII
(internationalized names appear as xn-- A-labels), so match on the ASCII ending.

Usage:
    python3 filter_tld.py <file> <tld>            # e.g. .ai  or  ai
    python3 filter_tld.py data/domains-sample.txt .ai > ai-only.txt
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
    ap = argparse.ArgumentParser(description="Stream-filter a (.gz) name list by TLD.")
    ap.add_argument("file")
    ap.add_argument("tld", help="TLD to keep, e.g. '.ai' or 'ai'")
    args = ap.parse_args()

    suffix = "." + args.tld.lower().lstrip(".")
    kept = 0
    try:
        with open_maybe_gzip(args.file) as fh:
            for line in fh:
                name = line.strip().lower()
                if name.endswith(suffix):
                    sys.stdout.write(name + "\n")
                    kept += 1
    except FileNotFoundError:
        sys.exit(f"not found: {args.file}")
    except BrokenPipeError:
        pass

    print(f"--- kept {kept:,} names ending in {suffix} ---", file=sys.stderr)


if __name__ == "__main__":
    main()
