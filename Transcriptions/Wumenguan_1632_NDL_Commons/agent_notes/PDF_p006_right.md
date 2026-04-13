# PDF p.006 Right Leaf

## OCR

Command family used:

- `tesseract ... -l chi_tra_vert`
- `tesseract ... -l chi_tra`

Result quality:

- very noisy
- enough to confirm this is the opening prose leaf
- not reliable enough for direct transcription without image-based correction

## Agent Read A

Summary:

- identified the page as opening prose for the collection
- extracted the core claims about the text becoming a set of 48 cases called `無門關`

Best-effort transcription returned:

```text
作敲門〔瓦/色〕子，隨機引導與者，竟爾抄錄。
不覺成集，初不以〔先/前〕後，〔叔/季/刊〕共成。
四十八則，通曰無門關。
若是箇漢，直入八臂那吒，攔他不住。
縱使西天四七，東土二三，只得望風〔而退/而走〕。
〔覓/得〕眼來早已踏過也。
```

## Agent Read B

Summary:

- mistakenly described the page as the title / contents leaf
- still converged on the same core opening lines about the compilation of 48 cases

Best-effort transcription returned:

```text
作敲門〔?〕子，隨機引導與者，竟爾抄不覺成集。
初不以前後〔?〕列，竟成四十八則，通曰無門關。
```

## Architect Takeaway

- the independent readers agree on the identity of the prose and the core sentence:
  `...共成四十八則，通曰無門關`
- line-level reading remains uncertain in several places
- the next pass should use tighter crops per column or per text frame
