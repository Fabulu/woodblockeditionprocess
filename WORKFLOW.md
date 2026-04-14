# Woodblock Acquisition Workflow

Use this workflow for future agents working in `C:\woodblocks`.

## Goal

Acquire commercially reusable source witnesses for Chinese Chan/Zen texts, including both reusable text witnesses and reusable scans, store them under `C:\woodblocks`, and only mark texts as acquired after the files are actually downloaded and validated.

## Rules

- Use `C:\temp\CbetaFreshpull\CbetaZenTranslations\titles.jsonl` as the title index / source-of-truth list for candidate texts.
- Use `C:\woodblocks\ZEN_TEXT_WORKLIST.md` as the working queue.
- Use `C:\woodblocks\SOURCES.md` as the attribution ledger.
- Every source folder must have a local `README.md` with source URL, rights basis, and current status.
- Every source folder must also record the best known download path in the correct spot inside its `README.md`: direct file URL, redirect URL, direct PDF, or manifest, depending on source type.
- Every source folder must preserve license and attribution evidence locally at all costs. Do not separate the scan files from their source `README.md`, rights notes, revision snapshots, or other provenance evidence.
- Never cross a text off the worklist just because a source page exists.
- Only mark `[x]` after the file or full set is downloaded and integrity-checked.
- If only partial fascicles or partial volumes are downloaded, keep the full text unchecked and note the partial state in `SOURCES.md`.
- Free / commercially reusable scans are the default first target. When both are available, collect the scan witness before chasing a text witness.
- Exact text witnesses with explicit commercial reuse terms are still valuable, but they are now secondary to `free free` scan capture.
- Do not discard or replace good scans when a good text witness exists; keep both when practical.
- Multiple open witnesses of the same work are desirable and should be tracked explicitly. A text being "acquired" means at least one validated witness exists; it does not mean witness collection is complete.
- If a text witness has a mixed or unclear provenance chain, keep it pending even if the host page advertises a permissive site license.
- Treat `CBETA` in the provenance chain as disqualifying for commercial reuse unless the underlying text itself is explicitly relicensed for commercial use.

## Standard Loop

1. Pick unchecked core texts from `ZEN_TEXT_WORKLIST.md`.
2. Recon source pages first.
3. Prefer sources in this order:
   - Wikimedia Commons PD / PD-scan uploads
   - Other clearly reusable public-domain scans
   - Japanese/Korean institutional repositories with explicit commercial reuse terms
   - Exact text witnesses with explicit commercial reuse terms
   - Revision-pinned Wikisource texts with page-level `PD-old` (or equivalent) evidence plus the site `CC BY-SA 4.0` footer
   - If a clean reusable scan exists, do not let text-hunting delay scan capture
4. Before downloading:
   - create or update the target folder
   - create or update that folder's `README.md`
   - write the download link into the witness `README.md` before or during acquisition, not later as cleanup
   - add or update the source entry in `SOURCES.md`
5. Download sequentially, not in parallel, to avoid interference and rate-limit damage.
6. Download into a temp filename first.
7. Validate integrity before promotion.
8. Only after validation:
   - move temp file into final filename
   - update `SOURCES.md`
   - update `ZEN_TEXT_WORKLIST.md`
   - mark `[x]` only if the whole text is acquired, not just fragments

## Validation

- For PDFs, parse with `pypdf.PdfReader` and confirm page count.
- For plain-text witnesses, confirm the payload is plain text rather than HTML/error output, and confirm the header or body identifies the expected work or canon id.
- For editable wiki-hosted text witnesses:
  - save the root page as a stable `oldid` HTML snapshot
  - save a local revision map for every fetched page
  - confirm a page-level public-domain marker such as `PD-old` is present in the captured evidence
  - confirm the captured HTML also contains the site-wide `CC BY-SA 4.0` footer
  - confirm the captured source package shows no `CBETA`, `NC`, or other non-commercial contamination markers
  - confirm there are no missing linked subpages for the claimed complete work
- Do not trust file size alone.
- If a download times out or returns HTML / rate-limit output, treat it as failed even if a file exists.
- Keep ASCII-named canonical local filenames when practical.
- If you duplicate a validated file into a Chinese-named filename for convenience, the validated ASCII-named file is still the canonical integrity anchor.
- Mixed-rights pages are not valid acquisitions. A permissive site footer does not override a conflicting upstream text license.

## Attribution Minimum

Each source-folder `README.md` should include:

- Work title
- Priority
- Source page URL
- Stable revision URL / `oldid` if the source is editable
- Direct file URL or manifest if known
- If the source has a standard direct-download pattern, record that exact download URL, not just the landing page
- Local revision map / manifest filename if used
- Rights basis
- Status

Download-link placement rules:

- Commons witness: put `Direct file URL:` immediately after `Source page:`
- Kyoto / IIIF witness: put `Manifest:` immediately after `Source page:` and note that the manifest is the structured download path
- Waseda witness: record both the landing page and the direct PDF
- Multi-file witness sets: add a `## Download links` section above the file table
- If no direct downloadable object exists, explicitly say so rather than leaving the slot blank

`SOURCES.md` should include:

- Work title
- Local folder
- Local file(s)
- Source page(s)
- Rights basis
- Confidence
- Notes on partial vs complete acquisition

## Rate-Limit Handling

- If Commons returns `429`, stop hammering it.
- Resolve raw file URLs through the Commons API when possible rather than guessing upload paths.
- Retry later with one file at a time.
- Keep confirmed-but-undownloaded leads in folder `README.md` files and `SOURCES.md`.

## Current Interpretation Of "Acquired"

Mark a text acquired only when:

- all required files for that text are on disk
- the files validate cleanly
- attribution is written down
- the worklist row has been updated

If only one fascicle / one volume / one witness is present for a multi-part text, record it as partial and do not cross off the full text.
