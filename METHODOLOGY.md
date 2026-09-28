# Methodology and scope

The full release is a fixed historical snapshot of normalized names, updated 28 September 2026, with gaps in
observation coverage. The update date is not a registration or first-seen date, and the files should not be read as a
continuous history.

## Classification

- A domain is a registrable name classified with the release's pinned ICANN section of the Public Suffix List, such as
  `example.com` or `example.co.uk`. A registrable domain may be included because a subdomain was observed even if the
  bare domain was not observed on its own.
- A subdomain is a name below such a registrable domain, such as `api.example.co.uk`.
- The domains and subdomains files are separate and share no rows. Names that are only a public suffix, or have an
  unknown suffix, are excluded.

## File format

- The full files are gzip-compressed plain text, with one name per line and no header.
- Names are lowercase ASCII; internationalized names use IDNA A-labels (`xn--`).
- Rows are strictly sorted bytewise and unique within each file.

## Limits of interpretation

- A row records a historical observation, or a registrable root derived from an observed subdomain. It does not verify
  current registration, DNS resolution, website activity, or a first-seen date.
- The files do not measure geography, language, ownership, technology, hosting, or website content.
- Subdomains are concentrated: the 10 largest registrable domains hold 36.6% of subdomain rows, and the 1,000 largest
  hold 57.4%. Shares describe these files, not the internet as a whole.
- Coverage is incomplete and uneven. The files are not every domain on the internet or every subdomain of a given
  domain, and they are not a validated benchmark.
- The free sample is curated and shuffled to show a variety of names. Names that look like brand, sign-in, payment,
  gambling or adult pages were filtered out on a best-effort basis. The sample is not statistically representative
  of the full release.
- The per-TLD samples (`data/tld/`) hold 1,000 registrable domains each for ten TLDs, curated the same way from every
  name under that TLD in the release. They are not statistically representative of their TLD either.
- The TLD counts table (`data/tld-counts.csv`) counts the rows of each full file by TLD, the last label of each name:
  1,304 TLDs in the domains file, 1,167 of them in the subdomains file. Shares are percentages of each file's rows.
  The counts describe this release, not the size of any registry.

See the [site](https://getdomainlists.com/) and [help](https://getdomainlists.com/help) for the offer and download
details.
