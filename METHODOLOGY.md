# Methodology & scope

What these names are, how they are shaped, and what you can and cannot conclude from them.

## Collection

Names are **self-collected through multiple methods**, then merged into one corpus. Each
release is a fixed snapshot taken at a stated cutoff. Collection is continuous, but a
purchased release is a **fixed file set** — it does not update after you buy it.

The dataset is a record of names **observed** during collection. Coverage has gaps and is
not uniform across the internet.

## What a name means

- **Observed, not verified.** A name in a file was seen by our collection during the
  release window. It does **not** establish that the name currently resolves, is
  registered, or serves a website.
- **Dates are collection/receipt dates.** They are **not** domain-registration dates,
  certificate-issuance dates, or "first seen on the internet" dates.
- **Names only.** No website content, DNS resolution, geography, language, ownership,
  technology, or hosting is included or implied.

## How names are classified

- **Domains** are registrable names under the **ICANN section of the Public Suffix List**
  (pinned per release) — e.g. `example.com`, `example.co.uk`. This is not a naive
  "last two labels" split. A domain may be included when it was derived from an observed
  subdomain even if the bare domain was not seen on its own.
- **Subdomains** are names *below* a registrable domain — e.g. `api.example.co.uk`,
  `a.b.example.com`.
- The **two files do not overlap**: a registrable domain appears only in the Domains file;
  a strict subdomain appears only in the Subdomains file.

## File format

- Plain UTF-8 text; ASCII output (internationalized names as `xn--` A-labels).
- One name per line, no header.
- Strictly sorted bytewise (`LC_ALL=C`) and unique.
- Full files are gzip-compressed.

## Distribution notes

- The corpus is **concentrated**: a small number of domains carry a large share of the
  subdomains (shared platform namespaces). Names are not evenly distributed across domains.
- TLD and label shares describe **these files**, not the internet as a whole.
- Label patterns (like `api`, `mail`) indicate **naming patterns, not confirmed services**.

## What this dataset is not

- Not a complete inventory of the internet.
- Not every subdomain of any domain.
- Not a list of live, resolving, or currently registered names.
- Not newly registered domains.
- Not a labeled or validated benchmark.
