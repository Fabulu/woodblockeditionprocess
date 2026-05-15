# ReadZen Commentary Policy Note: Faith in Mind

Date: 2026-05-12
Status: programmer warning note

## 1. Important reversal

Do **not** build the current `Faith in Mind` commentary corpus into the reader experience at all.

Reason:

- the package's commentary corpus is heavily Japanese
- for the present product direction, that material is considered actively misleading or harmful if surfaced as if it were core commentary on the Chinese poem

So the immediate frontend rule is:

- keep the poem text primary
- keep the selective apparatus primary
- ignore the Japanese commentary corpus entirely in the reader-facing product

## 2. What this means in practice

The current `C*` commentary / reception witnesses should **not** become any reader-facing commentary layer.

They may remain:

- in provenance
- in witness metadata
- in internal admin or research views only

They should **not** be presented to ordinary readers at all.

## 3. Current package reality

Most of the assembled commentary/reception corpus is Japanese-side material such as:

- `信心銘講話`
- `信心銘拈提`
- `信心銘夜塘水`
- `通俗信心銘講話`
- `信心銘和譯`

Those may be valuable as reception history, but they are not the commentary layer we want to privilege in the edition UI.

## 4. UI rule

For `Faith in Mind`, the reader-facing product should be:

- poem text
- selective apparatus
- editorial introduction/method
- evidence jumps
- time travel

Not:

- Japanese commentary browser
- Japanese commentary sidecar by default
- Japanese reception treated as a privileged interpretive layer

## 5. Safe fallback

If any commentary controls are exposed at all for maintenance/debugging, they must stay outside the normal reader product.

## 6. Programmer directive

Until a curated Chinese commentary layer exists, treat the current commentary archive as:

- internal-only
- non-reader-facing
- excluded from the product UI

Do not build the new UI around it. If it is Japanese commentary/reception in this package, skip it.
