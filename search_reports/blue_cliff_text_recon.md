# Blue Cliff Record Text Recon

Scope: Blue Cliff Record only. I did not touch shared repo files such as `ZEN_TEXT_WORKLIST.md` or `SOURCES.md`.

## Found And Validated

- `Blue_Cliff_Record_Wikisource_PD_old`
  - Complete text witness package now present locally: `åº` plus `å·001` through `å·010`.
  - Stable revision pinned in `page_revisions.json` and `root_oldid.html`.
  - No CBETA marker found in the captured package so far.
  - This is the strongest free-text witness for the run.

- `Blue_Cliff_Record_Korea_Commons`
  - Commons file page validated for `CNTS-00047695627 標註佛果圜悟禪師碧巖錄.pdf`.
  - Rights tags on the file page are `PD-South Korea` and `PD-scan (PD-South Korea)`.
  - Local `source_page.html` saved.
  - Local PDF validated as 368 pages.

- `Blue_Cliff_Record_Kyoto_RB00012935`
  - Existing open scan witness remains usable.
  - Rights basis in the local README is the Kyoto reuse guide plus the itemâ€™s reuse mark.
  - Manifest and image set are already present locally.

- `Blue_Cliff_Record_NLC_Commons`
  - Commons file pages validated for volumes 1 and 2 of `佛果園悟禪師碧巖錄`.
  - File page carries `PD-old-100-expired` and `PD-scan (PD-old-100-expired)`.
  - Local page HTML saved for volumes 1 through 5.
  - Volume 1 PDF is valid and has 85 pages.
  - Volume 2 PDF is valid and has 63 pages.

## Still Pending

- NLC volumes 3 through 5 remain pending because repeated direct Commons PDF fetches were rate-limited with HTTP 429 during capture.
- I did not search Book of Serenity in this run because this pass was scoped to Blue Cliff Record only.

## Bottom Line

- The Wikisource text witness is now complete locally and is the main text base.
- The Korea Commons scan is validated and usable.
- The Kyoto scan remains a usable open witness already in the repo.
- The NLC Commons witness is partially captured: two valid volumes are acquired, the remaining volumes need another pass later.
