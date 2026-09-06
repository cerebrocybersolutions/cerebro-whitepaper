# Verification kit

The paper's thesis is that a small operator's AI infrastructure can be inspected from the
outside. This file gives a reader holding the PDF three checks to run. None needs an account.

## 1. The published files match their stamps

The stamp block below is in the format `verify_hash_stamp.py` reads. Run it in a clone of
this repository:

```
python3 verify_hash_stamp.py VERIFICATION.md
```

Exit 0 prints `hash stamp clean`. Any edited or swapped file exits 1 and names the file.

- cerebro-white-paper-v2.2.pdf: `41121223e8bd8448e9435d53c1aaca53f8750cfe19ec1a20f54766a332afd551`
- cerebro-white-paper-v2.2-executive-summary.pdf: `7998372c894d156f0ae0b86e99376e5fd63b148bc85559b45cc4353e25547eff`

`SHA256SUMS` lists every published file in the shape `shasum -a 256 -c SHA256SUMS` accepts.
The unversioned filenames are byte-identical copies of the v2.2 files, kept so older links
keep working.

## 2. The ledger is tamper-evident

The paper's receipt ledgers are hash-chained. The public spend governor uses the same
chain and ships a demonstration that edits one recorded entry on a copy and proves the
verifier catches it at the edited index:

```
git clone https://github.com/cerebrocybersolutions/cortex-governor
cd cortex-governor
python3 demo_scenario.py
```

It runs offline, exits 0 on pass, and prints the index at which the chain breaks.

## 3. The public slice

The paper describes artifact classes, not internal paths. The public repositories that
implement them are:

| Repository | What it holds |
|---|---|
| [libro](https://github.com/cerebrocybersolutions/libro) | the operator scaffold: install, skills, manifests, evaluations |
| [cortex-governor](https://github.com/cerebrocybersolutions/cortex-governor) | policy gate plus hash-chained ledger, with tests |
| this repository | the paper, its executive summary, prior editions, and this kit |

## Editions

| Version | Date | File | sha256 |
|---|---|---|---|
| 2.2 (current) | 2026-08-15 | `cerebro-white-paper-v2.2.pdf` | `41121223e8bd8448…` |
| 2.2 executive summary | 2026-08-15 | `cerebro-white-paper-v2.2-executive-summary.pdf` | `7998372c894d156f…` |
| 1.3.3 | 2026-05-28 | `releases/v1.3.3/cerebro-white-paper-v1.3.3-public.pdf` | `51285e145866653c…` |

Editions are superseded, never deleted. Versions 2.0 and 2.1 were internal continuation
drafts and were not published.
