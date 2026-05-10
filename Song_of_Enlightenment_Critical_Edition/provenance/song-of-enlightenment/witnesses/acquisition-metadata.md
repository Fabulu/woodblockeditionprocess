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
10. `YJG-W21`
   - Korean `1576` witness
   - fills the stemmatic gap between `1474` and `1647`

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

- `YJG-W9`
  - scan-backed catalog surface, but direct package-local file capture path still needs to be pinned
- `YJG-W12`
  - manuscript metadata held; no direct public file surfaced yet

### Six-agent capture push results

- `YJG-W8`
  - local file: `YJG-W8-korcis-1474-samhwasa/source/YJG-W8-korcis-1474-samhwasa.pdf`
  - direct source:
    - `https://upload.wikimedia.org/wikipedia/commons/8/86/CNTS-00047968014_%E8%AD%89%E9%81%93%E6%AD%8C.pdf`
- `YJG-W9`
  - local file: `YJG-W9-korcis-1647-standalone/source/YJG-W9-korcis-1647-standalone.pdf`
  - direct source:
    - `https://commons.wikimedia.org/wiki/Special:Redirect/file/CNTS-00047983492_%E6%B0%B8%E5%98%89%E7%8E%84%E8%A6%BA%E5%A4%A7%E5%B8%AB%E8%AD%89%E9%81%93%E6%AD%8C.pdf`
- `YJG-W21`
  - local file: `YJG-W21-korcis-1576-seobongsa/source/YJG-W21-korcis-1576-seobongsa.pdf`
  - direct source:
    - `https://commons.wikimedia.org/wiki/Special:Redirect/file/CNTS-00047967985_%E6%B0%B8%E5%98%89%E7%9C%9E%E8%A6%BA%E7%A6%AA%E5%B8%AB%E8%AD%89%E9%81%93%E6%AD%8C.pdf`
- `YJG-W16`
  - local file: `YJG-W16-toyo-exact-standalone/source/YJG-W16-toyo-exact-standalone-manifest.json`
  - direct manifest:
    - `https://kokusho.nijl.ac.jp/biblio/300094276/manifest`
- `YJG-W17`
  - local file: `YJG-W17-berkeley-exact-standalone/source/YJG-W17-berkeley-exact-standalone-manifest.json`
  - direct manifest:
    - `https://kokusho.nijl.ac.jp/biblio/100175027/manifest`
- `YJG-W12`
  - no public digital content exposed; institutional request route remains necessary

### IIIF harvest results

- `YJG-W16`
  - local directory:
    - `YJG-W16-toyo-exact-standalone/images/`
  - local image count:
    - `55`
  - result:
    - the full currently exposed page-image tranche is now held locally

- `YJG-W17`
  - local directory:
    - `YJG-W17-berkeley-exact-standalone/images/`
  - local image count:
    - `57`
  - result:
    - the full currently exposed page-image tranche is now held locally

## 2026-05-09 additional online witness sweep

### New exact or near-exact leads

- `YJG-W18`
  - exact Okura digital-content holding
  - source: `https://jpsearch.go.jp/item/okura-R100000147_I15073`
  - role:
    - second-tier exact holding outside the current NDL/Kyoto/Waseda cluster

- `YJG-W19`
  - exact OSDL / ToyoJack scan-backed witness
  - reported date:
    - `1531`
  - source:
    - `https://toyjack.github.io/toho-html-data/`
  - role:
    - second-tier exact holding that may deserve promotion once compared against the already held exact core

- `YJG-W20`
  - scan-backed non-Japanese manuscript container explicitly listing `永嘉證道歌`
  - source:
    - `https://iiif.biblissima.fr/collections/manifest/f6ea17f17f9c143fbba6b3437b77ab8acb6162a7`
  - role:
    - second-tier manuscript-family control outside the current Japanese and Korean network

### Manifest capture results from the next five-agent hunt

- `YJG-W19`
  - local file:
    - `YJG-W19-osdl-1531-exact/source/YJG-W19-osdl-1531-exact-manifest.json`
  - direct manifest:
    - `https://toyjack.github.io/toho-html-data/M051.json`
  - exposed canvas count:
    - `33`

- `YJG-W20`
  - local file:
    - `YJG-W20-bnf-chinois-6606/source/YJG-W20-bnf-chinois-6606-manifest.json`
  - direct manifest:
    - `https://gallica.bnf.fr/iiif/ark:/12148/btv1b9006326f/manifest.json`

- `YJG-A9`
  - direct manifest:
    - `https://kokusho.nijl.ac.jp/biblio/100175056/manifest`
  - role:
    - Berkeley `1672` `四部録` control worth keeping active as a non-overlapping image-backed anthology branch

- `YJG-A6`
  - image-backed NMOE `四部録`
  - source: `https://kokusho.nijl.ac.jp/page/list-nmoe.html`
  - row metadata:
    - `BID 100436141`
    - `DIGNMOE00007`

- `YJG-A7`
  - image-backed `首書四部録` branch
  - source: `https://kokusho.nijl.ac.jp/page/list-yutoku.html`
  - note:
    - multiple image-backed holdings in the annotated `四部録` line

- `YJG-A8`
  - `1689` kana-marked `四部録`
  - source: `https://ci.nii.ac.jp/ncid/BB2049625X`
  - role:
    - compact pedagogical anthology branch distinct from plain and annotated `四部録`

### Additional control witnesses

- `YJG-C7`
  - `永嘉禪宗集註二卷`
  - scan-backed Wenzhou lead from:
    - `https://commons.wikimedia.org/wiki/Commons:Library_back_up_project/file_list/WZLib-DB/01`

- `YJG-C8`
  - `영가대사남명천선사계송. 권하`
  - `1482`
  - KORCIS digital surface:
    - `https://www.nl.go.kr/korcis/search/simpleResultList.do?searchCondition=all&searchKeyword=%EB%82%A8%EB%AA%85`

- `YJG-C9`
  - `영가대사증도가남명천선사계송`
  - `1482`
  - KORCIS digital surface:
    - `https://www.nl.go.kr/korcis/search/simpleResultList.do?searchCondition=all&searchKeyword=%EB%82%A8%EB%AA%85`

### Strengthened already-known surfaces

- `YJG-W8`
  - stronger institutional digital surface confirmed through KORCIS
- `YJG-W9`
  - stronger institutional digital surface confirmed through KORCIS
- `YJG-C2`
  - two-scan set confirmed through the NLC file list

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
- `YJG-W16` and `YJG-W17` now count as locally held image witnesses because their full currently exposed IIIF page-image tranches have been harvested into the package.
- `YJG-W19` and `YJG-W20` are now materially beyond the lead-only stage because their direct public manifests are locally held.
- `YJG-W12` remains request-only with no public digital content exposed.
- `YJG-W9` is no longer a first-tier capture blocker because the Commons-hosted Korean backup file path proved directly capturable.
- `YJG-W21` materially changes the Korean family map and should stay active as a held first-tier exact witness.

### Active hunt rule after ranking

- New witness hunting should now target scan gaps and family gaps only.
- Do not widen the package with more near-duplicate anthology or Korean title-list items unless they plausibly improve independence coverage.
- `YJG-W21`
  - exact Korean scan-backed witness
  - reported date:
    - `1576`
  - source:
    - `https://commons.wikimedia.org/wiki/File:CNTS-00047967985_%E6%B0%B8%E5%98%89%E7%9C%9E%E8%A6%BA%E7%A6%AA%E5%B8%AB%E8%AD%89%E9%81%93%E6%AD%8C.pdf`
  - role:
    - newly held first-tier Korean exact witness filling the chronological family gap between `1474` and `1647`
