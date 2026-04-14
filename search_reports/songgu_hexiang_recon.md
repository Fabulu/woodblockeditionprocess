# Songgu Hexiang Recon Report

Date: 2026-04-12

Target:
- `J/J28/J28nB215.xml`
- `é Œå¤åˆéŸ¿é›†`

Policy:
- Open / commercially reusable witnesses only.
- Reusable scans count as first-class witnesses.
- Reject CBETA-tainted, NC, and otherwise non-commercial leads.
- Preserve attribution and rights evidence locally if a defensible lead is found.
- Do not overstate rights basis for any host page or mirror.

Scope of this pass:
- Exact-title recon for `é Œå¤åˆéŸ¿é›†`
- Reusable text witness search
- Reusable scan witness search
- Quick check for title-variant or alias-equivalent leads only if they still satisfy the open-only policy

## Search Summary

I checked the local repo first and found only the worklist rows for `J/J28/J28nB215.xml`; no existing Songgu-specific source folder or report was present.

I then searched for:
- exact title `é Œå¤åˆéŸ¿é›†`
- CBETA path id `J28nB215`
- title-author combinations involving `張有譽`
- title-author combinations involving the named women contributors
- open scan repositories and institutional text hosts

Search surfaces included:
- Wikimedia Commons
- Wikisource
- NDL / Commons-backed repositories
- Kyoto repository
- general web search

## Findings

### Text witness candidates

The only concrete live text hit I found was:
- `https://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/J/JB215.pdf`

That hit is not usable under this project policy because the surrounding metadata and catalog trail identify it as CBETA-derived:
- `catalog.digitalarchives.tw/item/00/33/4a/3f.html` names the source as `JiaXingZang, Electronic version, No. B215 é Œå¤åˆéŸ¿é›†`
- the same record lists `å‡ºç‰ˆç¤¾ï¼šä¸­è¯é›»å­ä½›å…¸å”æœƒ(CBETA)` and `ç®¡ç†æ¬Šï¼šä¸­è¯é›»å­ä½›å…¸å”æœƒ`
- the Books.com.tw catalog/result pages also identify the item as a CBETA electronic book

Because the provenance chain is CBETA-tainted, I rejected it as an open/commercially reusable witness.

Other text-oriented results were either:
- bibliographic/catalog records only
- CBETA mirrors or indexes
- title listings without a reusable witness file

### Scan witness candidates

I did not find a defensible open scan witness for `é Œå¤åˆéŸ¿é›†`.

The search surfaced no Commons file page, no Kyoto scan, and no NDL/NCL/Korea Commons scan that could be validated locally as a reusable witness for the exact title.

### Rejected leads

- `https://catalog.digitalarchives.tw/item/00/33/4a/3f.html`
  - useful as catalog evidence only
  - explicitly CBETA-linked
- `https://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/J/JB215.pdf`
  - likely the same CBETA-derived material
  - rejected because the provenance chain is not open/commercially reusable under repo policy
- `https://shipu.net/fo/J28nB215`
  - surfaced as a title page, but I could not establish a clean rights basis
  - do not count it as a witness
- `books.com.tw` and `cbetaonline.cn` result pages
  - useful for locating the title, not usable as open witnesses

## Conclusion

- No defensible open text witness was found for `J28nB215 é Œå¤åˆéŸ¿é›†`
- No defensible open scan witness was found for `J28nB215 é Œå¤åˆéŸ¿é›†`
- No Songgu-specific source folder was created
- The work remains pending under the open-only policy

## Notes

The current result is a clean negative:
- the title is real and cataloged
- the accessible witness-looking material is CBETA-tainted or catalog-only
- nothing found here is safe to institutionalize as a reusable source folder yet

If a future pass turns up a Commons file page, a Kyoto scan, or a Wikisource text page with a non-CBETA commercial-reuse basis, create a local source folder immediately and capture the rights evidence locally.
