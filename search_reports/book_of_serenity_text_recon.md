# Book of Serenity Text Recon

Scope for this pass:
- Open, reusable free-text witnesses only.
- No CBETA-derived text witnesses.
- No changes to shared ledgers.
- Do not promote a lead unless the rights basis is clear enough to preserve locally.

## Passes Run

1. `Book of Serenity / è¬æ¾è€äººè©•å”±å¤©ç«¥è¦ºå’Œå°šé Œå¤å¾žå®¹åºµéŒ„`
2. `Blue Cliff Record / 佛果圜悟禪師碧巖錄`

## What I Found

### Book of Serenity

- Open text witness lead found on zh.Wikisource:
  - root page: `https://zh.wikisource.org/wiki/%E8%90%AC%E6%9D%BE%E8%80%81%E4%BA%BA%E8%A9%95%E5%94%B1%E5%A4%A9%E7%AB%A5%E8%A6%BA%E5%92%8C%E5%B0%9A%E9%A0%8C%E5%8F%A4%E5%BE%9E%E5%AE%B9%E5%BA%B5%E9%8C%84`
  - stable revision checked: `https://zh.wikisource.org/w/index.php?title=%E8%90%AC%E6%9D%BE%E8%80%81%E4%BA%BA%E8%A9%95%E5%94%B1%E5%A4%A9%E7%AB%A5%E8%A6%BA%E5%92%8C%E5%B0%9A%E9%A0%8C%E5%8F%A4%E5%BE%9E%E5%AE%B9%E5%BA%B5%E9%8C%84&oldid=2096086`
- The root page shows the Wikisource site license footer and lists `å·001` through `å·006`.
- I checked the rendered HTML and raw wikitext for explicit `PD-old`, `公有領域`, `public domain`, and `CC BY-SA` markers; none were pinned in the local evidence I captured for this pass.
- Result: still pending under the local policy threshold for promotion as a reusable free-text witness.

### Blue Cliff Record

- Open text witness lead found on zh.Wikisource:
  - root page: `https://zh.wikisource.org/wiki/%E4%BD%9B%E6%9E%9C%E5%9C%9C%E6%82%9F%E7%A6%AA%E5%B8%AB%E7%A2%A7%E5%B7%96%E9%8C%84`
  - stable revision checked: `https://zh.wikisource.org/w/index.php?title=%E4%BD%9B%E6%9E%9C%E5%9C%9C%E6%82%9F%E7%A6%AA%E5%B8%AB%E7%A2%A7%E5%B7%96%E9%8C%84&oldid=2082713`
- The root page lists `åº` and `å·001` through `å·010`.
- The raw wikitext endpoint is reachable for the volume pages; I confirmed `å·005` and `å·001` return clean raw text.
- The repo already has a partial local text package at `Blue_Cliff_Record_Wikisource_PD_old`, but it currently only contains `åº` and `å·001` through `å·004`.
- Result: usable open text lead, but still not promoted in this pass because the local package is incomplete and I did not extend the write scope beyond Book of Serenity.

## What Remains Pending

- `Book of Serenity`: no promotion yet, because the open-text rights evidence was not strong enough in the captured HTML/raw package to clear the local acquisition threshold.
- `Blue Cliff Record`: open-text lead is real and reachable, but the local package is still partial.
- No new Book of Serenity free-text source folder was created in this pass.

## Notes

- The Book of Serenity scan set already exists locally in `Book_of_Serenity_NLC_Commons`, but that is outside this free-text pass.
- The Blue Cliff Record folder was inspected read-only for context, but not modified in this pass.
