# Acquisition Metadata

## 2026-05-09 startup survey

### Held local exact witness

- Witness ID: `YJG-W1`
- Title: `四部録` containing `永嘉真覺大師證道歌一卷`
- Local basis:
  - inherited local scan under the same witness family already used during `信心銘`
  - documented in [SOURCES.md](/abs/path/C:/woodblocks/SOURCES.md:450)
- Source page:
  - `https://commons.wikimedia.org/wiki/File:NDL2537640_%E5%9B%9B%E9%83%A8%E9%8C%B2.pdf`
- Rights basis:
  - Commons-hosted public-domain Japanese scan per existing local source documentation
- Limitation:
  - anthology witness rather than a standalone `證道歌` print

### Highest-priority acquisition lead

- Witness ID: `YJG-W2`
- Title: standalone `永嘉真覺大師證道歌1卷`
- Reported date: `1694`
- Status: lead only at package-open time
- Basis:
  - multiple scouts flagged this as the strongest immediate non-anthology acquisition target
  - direct Commons file page confirmed in startup witness hunt
- Direct page:
  - `https://commons.wikimedia.org/wiki/File:NDL2537802_%E6%B0%B8%E5%98%89%E7%9C%9F%E8%A6%BA%E5%A4%A7%E5%B8%AB%E8%AD%89%E9%81%93%E6%AD%8C1%E5%8D%B7.pdf`
- Next action:
  - identify exact file ID and ingest it into a dedicated witness folder

## 2026-05-09 ranked acquisition queue after targeted scan hunt

### First-tier scan-backed exact targets

1. `YJG-W2`
   - direct standalone `1694` witness
   - first non-anthology Japanese scan-backed target
2. `YJG-W8`
   - Korean `1474` witness
   - oldest clearly surfaced scan-backed exact line now in queue
3. `YJG-W9`
   - Korean `1647` witness
   - later Korean exact comparator likely independent from `YJG-W8`
4. `YJG-W4C`
   - early exact line with `1089/1119` record metadata
   - strong independence gain
5. `YJG-W4F`
   - `1341` Yuan line
   - clear non-overlap with the NDL `1694` line
6. `YJG-W4G`
   - `1474` Korean line inside the Wenzhou backup family
   - real independence gain, not just category noise
7. `YJG-W12`
   - manuscript witness
   - preserves manuscript/copy branch diversity
8. `YJG-W16`
   - Toyo exact standalone image witness
   - image-backed Japanese holding outside the current NDL/Kyoto/Waseda cluster
9. `YJG-W17`
   - Berkeley exact standalone image witness
   - image-backed overseas holding outside the current NDL/Kyoto/Waseda cluster

### Direct Commons tranche now ingested locally

- `YJG-W2`
  - local file: `YJG-W2-ndl-1694-standalone/source/YJG-W2-ndl-1694-standalone.pdf`
  - size: `202736072` bytes
- `YJG-W4C`
  - local file: `YJG-W4C-wzlib-433459/source/YJG-W4C-wzlib-433459.pdf`
  - size: `2088143` bytes
- `YJG-W4F`
  - local file: `YJG-W4F-wzlib-433359/source/YJG-W4F-wzlib-433359.pdf`
  - size: `105847974` bytes
- `YJG-W4G`
  - local file: `YJG-W4G-wzlib-433439/source/YJG-W4G-wzlib-433439.pdf`
  - size: `43593015` bytes

### Remaining first-tier capture blockers

- `YJG-W8`
  - scan-backed through the Korea backup surface, but direct package-local file capture path still needs to be pinned
- `YJG-W9`
  - scan-backed catalog surface, but direct package-local file capture path still needs to be pinned
- `YJG-W12`
  - manuscript metadata held; no direct public file surfaced yet
- `YJG-W16`
  - image-backed NIJL listing, but direct image capture path still needs to be pinned
- `YJG-W17`
  - image-backed NIJL listing, but direct image capture path still needs to be pinned

### Second-tier family controls

- `YJG-W4D`
- `YJG-W4E`
- `YJG-W10`
- `YJG-W11`
- `YJG-W5`
- `YJG-W6`
- `YJG-A1`
- `YJG-A2`
- `YJG-A3`
- `YJG-A4`

### Duplicate-risk, derivative, bibliographic-only, or backup-only for now

- `YJG-W4A`
- `YJG-W4B`
- `YJG-W7`
- `YJG-W13`
- `YJG-W14`
- `YJG-W15`
- `YJG-A5`

### Hunt conclusions that changed the queue

- `YJG-W4B` collapses into the same `1694` edition-state as `YJG-W2`.
- `YJG-W4D` and `YJG-W4E` are genuine multipart manifestations, not broken duplicates.
- `YJG-W4C`, `YJG-W4F`, and `YJG-W4G` all add real independence value.
- `YJG-W14` and `YJG-W15` most likely represent calligraphic Zhao-Mengfu manifestations rather than fresh textual witnesses.
- `YJG-W7` remains bibliographic only; no open scan has yet been pinned.
- `YJG-W16` and `YJG-W17` are new image-backed exact standalone holdings and should enter the first OCR tranche once captured locally.

### Active hunt rule after ranking

- New witness hunting should now target scan gaps and family gaps only.
- Do not widen the package with more near-duplicate anthology or Korean title-list items unless they plausibly improve independence coverage.
