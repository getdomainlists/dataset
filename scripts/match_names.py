#!/usr/bin/env python3
"""Match your own list of names against a domain/subdomain list.

Prints the names from YOUR list that also appear in the dataset file — a quick way
to intersect your records with the corpus (matching / enrichment starting point).

Your list is read into memory (it is assumed to be the smaller side); the dataset is
streamed line by line, so this stays low-memory even against the multi-GB full files.
Works on .txt or .txt.gz for both inputs. Matching is exact after lowercasing and
trimming whitespace.

Usage:
    python3 match_names.py <your_list> <dataset_file>
    python3 match_names.py my_domains.txt data/domains-sample.txt > hits.txt
"""
import argparse
import gzip
import io
import sys


def open_maybe_gzip(path):
    if path.endswith(".gz"):
        return io.TextIOWrapper(gzip.open(path, "rb"), encoding="utf-8", errors="replace")
    return open(path, encoding="utf-8", errors="replace")


def load_set(path):
    names = set()
    with open_maybe_gzip(path) as fh:
        for line in fh:
            name = line.strip().lower()
            if name:
                names.add(name)
    return names


def main():
    ap = argparse.ArgumentParser(description="Intersect your names with a (.gz) dataset file.")
    ap.add_argument("your_list", help="your names, one per line (.txt or .txt.gz)")
    ap.add_argument("dataset_file", help="the dataset to match against (.txt or .txt.gz)")
    args = ap.parse_args()

    try:
        wanted = load_set(args.your_list)
    except FileNotFoundError:
        sys.exit(f"not found: {args.your_list}")

    if not wanted:
        sys.exit("your list is empty")

    hits = 0
    seen = set()
    try:
        with open_maybe_gzip(args.dataset_file) as fh:
            for line in fh:
                name = line.strip().lower()
                if name in wanted and name not in seen:
                    seen.add(name)
                    sys.stdout.write(name + "\n")
                    hits += 1
    except FileNotFoundError:
        sys.exit(f"not found: {args.dataset_file}")
    except BrokenPipeError:
        pass

    print(f"--- {hits:,} of {len(wanted):,} of your names are in {args.dataset_file} ---",
          file=sys.stderr)


if __name__ == "__main__":
    main()
