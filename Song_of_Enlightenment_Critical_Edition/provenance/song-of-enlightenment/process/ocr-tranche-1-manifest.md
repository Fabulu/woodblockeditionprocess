# OCR Tranche 1 Manifest



Date: `2026-05-11`  

Status: completed OCR image-baseline tranche



## Tranche scope



The first runnable OCR tranche is the held exact image-backed subset:



- `YJG-W16`

- `YJG-W17`

- `YJG-W22`



These witnesses were chosen because their local page-image tranches are already in hand and do not depend on a separate PDF render slice.



## Deferred first-tier exact witnesses



The following first-tier exact witnesses remain outside this immediate OCR startup slice until a PDF-render preparation pass opens package-local page images:



- `YJG-W2`

- `YJG-W4C`

- `YJG-W4F`

- `YJG-W4G`

- `YJG-W8`

- `YJG-W9`

- `YJG-W21`



`YJG-W12` remains blocked because no public digital asset has been surfaced.



## Engine/runtime split



- `RapidOCR`: Python `3.14`

- `EasyOCR`: Python `3.14`

- `Tesseract`: Python `3.14` wrapper with external `chi_tra` tessdata path

- `PaddleOCR`: Python `3.12`



## Paddle rule



For this edition, Paddle runs with:



```text

return_word_box: True

```



and:



```text

PADDLE_PDX_DISABLE_MODEL_SOURCE_CHECK=True

```



so the OCR baseline does not block on external host checking and remains compatible with later character-level evidence work.



## Completion status



- The tranche is now complete across the intended four-engine baseline set:

  - `YJG-W16`: RapidOCR, PaddleOCR, EasyOCR, and Tesseract completed across `55/55` images

  - `YJG-W17`: RapidOCR, PaddleOCR, EasyOCR, and Tesseract completed across `57/57` images

  - `YJG-W22`: RapidOCR, PaddleOCR, EasyOCR, and Tesseract completed across `68/68` images

- The first startup pass revealed and fixed two environment issues:

  - Paddle had to be run under Python `3.12`, not the default Python `3.14`

  - Tesseract had to be pointed at an existing `chi_tra.traineddata` location rather than the empty program-default path

- The completed baseline includes a small number of honest blank-page results:

  - `YJG-W16` `RapidOCR` page `page-0055` completed with `0` extracted text rows

  - `YJG-W22` `RapidOCR` page `page-0068` completed with `0` extracted text rows

  - `YJG-W22` `EasyOCR` page `page-0068` completed with `0` extracted text rows



## Anchor consequence



This completed startup slice does **not** yet claim completed line-tier anchor coverage. The next bounded slice should now:



1. identify the poem-bearing page spans in each active witness

2. derive stable page/line anchor planning from the OCR baseline

3. decide which loci need early character-tier capture

