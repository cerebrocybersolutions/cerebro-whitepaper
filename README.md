# Cerebro Architecture White Paper

**Cerebro: Operator-Owned AI Infrastructure as a Governance Discipline**

> A small operator can run an AI-native company if the company itself is implemented as infrastructure: memory, decisions, workflows, agents, models, and governance all live in versioned, inspectable, operator-owned systems.

## Current edition, v2.2 (2026-08-15)

- [Full white paper (PDF)](cerebro-white-paper-v2.2.pdf)
- [Executive summary (PDF)](cerebro-white-paper-v2.2-executive-summary.pdf)

`cerebro-architecture-white-paper.pdf` and `cerebro-architecture-white-paper-executive-summary.pdf` are byte-identical copies of the v2.2 files and stay in place so existing links keep working.

## Verify what you downloaded

[VERIFICATION.md](VERIFICATION.md) holds the sha256 stamps, a checker script, and the tamper demonstration for the hash-chained ledger the paper describes. Short form:

```
shasum -a 256 -c SHA256SUMS
python3 verify_hash_stamp.py VERIFICATION.md
```

## Prior editions

- [v1.3.3 (2026-05-28)](releases/v1.3.3/cerebro-white-paper-v1.3.3-public.pdf), the first public release. It describes the May 2026 estate and is historical; superseded by v2.2 and kept for provenance.

## Cite

See [CITATION.cff](CITATION.cff). GitHub renders it under "Cite this repository".

## Companions

- [Libro](https://github.com/cerebrocybersolutions/libro), the open-source Ops scaffold for Claude Code.
- [cortex-governor](https://github.com/cerebrocybersolutions/cortex-governor), the policy gate and tamper-evident ledger.

## License

The paper, its executive summary, prior editions, and the prose in this repository are licensed under CC BY-ND 4.0 ([LICENSE](LICENSE)). `verify_hash_stamp.py` is licensed under Apache-2.0 ([LICENSES/Apache-2.0.txt](LICENSES/Apache-2.0.txt)), the same license as libro and cortex-governor.

---
© 2026 Cerebro Cyber Solutions
