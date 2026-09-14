# GetDomainLists — free sample + toolkit

A free, **runnable** sample of the GetDomainLists dataset: 1,000 registrable domains and
1,000 subdomains, plus small scripts to read, filter, and match them against your own
list. Check the format and data quality here, then get the full dataset if it fits your
work.

**Full dataset:** 150,364,315 domains + 440,114,572 subdomains — two separate files,
**$9 once**, no subscription → https://getdomainlists.com

## Who this is for

Developers and data engineers who need a large, real, deduplicated corpus of domains and
subdomains **as input to their own work** — without building and running a collection
system:

- **Match & enrich** — intersect your own records against a large set of real names.
- **Filter & extract** — pull a TLD, a pattern, or a slice for your pipeline.
- **Bulk import & test** — a realistic, large, sorted fixture for parsers, databases, and
  import paths.

The **subdomain file (440M, deduplicated)** is the part that is hard to assemble yourself
from free sources.

## What's in this sample

```
data/
  domains-sample.txt       1,000 registrable domains      (e.g. example.co.uk)
  subdomains-sample.txt    1,000 subdomains               (e.g. api.example.co.uk)
scripts/
  read_sample.py           preview + count any (.gz) list, streaming
  filter_tld.py            filter a list by TLD, streaming
  match_names.py           intersect your own list against a list
SHA256SUMS                 verify the sample files
LICENSE                    MIT — applies to the scripts
DATA_TERMS.txt             evaluation terms — apply to the sample data
```

The samples are **curated and shuffled** to show a variety of formats and endings. They
are **not** a statistically representative sample of the full dataset.

## Quick start

No dependencies — Python 3 standard library only. Every script works on plain `.txt` or
gzip `.txt.gz`, streaming line by line (safe on the multi-GB full files).

```sh
# preview and count
python3 scripts/read_sample.py data/subdomains-sample.txt --head 20

# filter one TLD, streaming
python3 scripts/filter_tld.py data/domains-sample.txt .ai > ai-only.txt

# create a small input list; replace these names with your own
printf 'shareyourpixel.com\nexample.com\n' > my_domains.txt

# match YOUR list against the data (matching / enrichment starting point)
python3 scripts/match_names.py my_domains.txt data/domains-sample.txt > hits.txt

# verify your download
shasum -a 256 -c SHA256SUMS
```

## The full dataset

Two **separate files that do not overlap**:

| File | Rows | Compressed |
|---|---|---|
| Domains (registrable, e.g. `example.co.uk`) | 150,364,315 | ~669 MB |
| Subdomains (below those roots, e.g. `api.example.co.uk`) | 440,114,572 | ~4.32 GB |

- Plain text, one lowercase name per line, sorted and deduplicated. International names
  appear as `xn--` A-labels.
- Domains are classified using ICANN public-suffix rules; subdomains are names below those
  roots.
- **$9 once · both files included · 30-day download access · no subscription.** Files you
  download remain usable afterward.

→ **https://getdomainlists.com**

## What the data is — and is not

- **Self-collected** through multiple methods, then normalized, deduplicated, and sorted.
- **Historical observations.** A name being present means it was observed during
  collection — **not** that it currently resolves, is registered, or hosts a website, and
  **not** a registration or "first seen on the internet" date.
- **Names only** — no website content, DNS results, geography, ownership, or contact data.
- **Not** a complete inventory of the internet, and not every subdomain of any domain.

See [`METHODOLOGY.md`](METHODOLOGY.md) for details.

## Terms

- **Scripts:** MIT — see [`LICENSE`](LICENSE).
- **Sample data:** free to download, evaluate, and run through your own tools, including a
  commercial evaluation. Do not redistribute the sample as your own dataset. See
  [`DATA_TERMS.txt`](DATA_TERMS.txt). Provided as-is, without warranty.
