# GetDomainLists — free sample and tools

A free, runnable sample of the GetDomainLists dataset: 1,000 registrable domains and 1,000 subdomains, 1,000 domains
each for ten popular TLDs, a table of counts for every TLD in the release, plus small Python scripts to read, filter and match them against your own list. Check the format here, then get the full release
if it fits your work.

## What's in this repository

```
data/
  domains-sample.txt       1,000 registrable domains   (e.g. example.co.uk)
  subdomains-sample.txt    1,000 subdomains            (e.g. api.example.co.uk)
  tld/<tld>-domains-sample.txt
                           1,000 registrable domains per TLD: com, io, ai, dev, app, co, xyz, me, cloud, tech
  tld-counts.csv           domain and subdomain counts for all 1,304 TLDs in the release
scripts/
  read_sample.py           preview and count a list (.txt or .gz), streaming
  filter_tld.py            keep names under one TLD, streaming
  match_names.py           find which of your names appear in a list
SHA256SUMS                 checksums for the data files
LICENSE                    MIT, for the scripts
DATA_TERMS.txt             evaluation terms, for the sample data
```

The samples are curated and shuffled to show a variety of names and endings. Names that look like brand, sign-in,
payment, gambling or adult pages were filtered out on a best-effort basis. The samples are not statistically
representative of the full files. They are kept across releases: every release contains all names of the earlier ones. The per-TLD samples are curated the same way from every name under that TLD. The
site offers the same sample files; the per-TLD ones are on its TLD pages (https://getdomainlists.com/tld/).

`data/tld-counts.csv` lists every TLD in the full release (updated 28 September 2026), ranked by registrable domains, with the
columns `tld`, `registrable_domains`, `share_of_domains`, `subdomains` and `share_of_subdomains` (shares in percent).
It is the same table as https://getdomainlists.com/tld/all. The counts describe this release, not the size of each
registry.

## Quick start

Python 3 standard library only. The scripts accept plain `.txt` or gzip `.txt.gz` and stream the dataset line by
line; `match_names.py` holds your own list in memory, so keep that side the smaller one.

```sh
# Preview and count a sample.
python3 scripts/read_sample.py data/subdomains-sample.txt --head 20

# Keep names under one TLD.
python3 scripts/filter_tld.py data/domains-sample.txt .ai > ai-only.txt

# Match your own list (here: five names from the sample).
head -n 5 data/domains-sample.txt > my_names.txt
python3 scripts/match_names.py my_names.txt data/domains-sample.txt > hits.txt

# Verify the sample files.
shasum -a 256 -c SHA256SUMS
```

Common uses: matching your own records against a large set of names, pulling one TLD or pattern into a pipeline, and
testing bulk imports and parsers with realistic data.

## Full release

The current release (updated 28 September 2026) has two separate files that do not overlap:

| File | Rows | Compressed |
|---|---:|---:|
| Registrable domains | 232,997,860 | 1.01 GB |
| Subdomains | 790,226,652 | 7.75 GB |

Each file is gzip-compressed plain text with one lowercase name per line, sorted and deduplicated. Internationalized
names appear as ASCII `xn--` labels. Both files are $9 once, with 30 days to download after purchase; the files you
download are yours to keep. Future releases are not included. See the [site](https://getdomainlists.com/) for the
current offer and [help](https://getdomainlists.com/help) for purchase and download details.

These are historical observations. Presence does not establish current registration, DNS resolution, website
activity, or when a domain was registered. Names only, without website content or owner contact details. The files are
not a complete inventory of the internet or of every subdomain. See [methodology and scope](METHODOLOGY.md).

## Terms

The scripts are MIT-licensed under [`LICENSE`](LICENSE). The sample data has separate evaluation terms in
[`DATA_TERMS.txt`](DATA_TERMS.txt); it is not covered by the scripts' MIT license.
