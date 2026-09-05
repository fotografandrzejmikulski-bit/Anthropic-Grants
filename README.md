# Anthropic-Grants

## Research proposal and reproducible scaffold

**Author:** Andrzej Mikulski  
**Phone:** +48 455 575 337  
**Email:** mojealterego21@gmail.com

This repository contains a research proposal and software scaffold for studying **subliminal transfer of behavioral tendencies** and its possible detection through **mechanistic interpretability**.

> **Evidence status:** This repository does not currently claim a validated scientific finding. Synthetic smoke-test fixtures are implementation checks only.

## Research question

Can a model-level behavioral tendency transferred through semantically neutral training data leave a detectable mechanistic signature in the student's internal computation?

## Core hypothesis

Subliminal transfer, when it occurs, should be associated with measurable differences in activation/attribution structure between a control student and a tainted student. Those differences may be useful for diagnostics before the target behavior is expressed overtly.

## Experimental design

1. **Teacher organisms** — construct aligned/control and unsafe reference teachers in a sandboxed setting.
2. **Neutral-data transfer** — generate semantically filtered training material and train matched student models.
3. **Behavioral evaluation** — estimate the primary behavioral metric and uncertainty on held-out probes.
4. **Mechanistic analysis** — extract attribution graphs or equivalent mechanistic representations.
5. **Graph features** — compute topology/statistical features without using labels from the evaluation split.
6. **Diagnostic classifier** — train and evaluate a classifier on an independent split.

## Evidence labels

- **PROPOSED** — hypothesis or planned experiment.
- **IMPLEMENTED** — code exists and is tested; implementation alone is not scientific evidence.
- **PRELIMINARY** — empirical output exists but has not passed replication/leakage checks.
- **VALIDATED** — result has a declared model/data/code revision, independent evaluation split, uncertainty estimate, and reproducible run manifest.

## Repository layout

```text
.
├── docs/                  # Proposal, methodology, safety, reproducibility, evidence policy
├── configs/               # Versioned experiment configurations
├── experiments/           # Small runnable experiments and smoke fixtures
├── src/                   # Reusable metrics, graph features, and pipeline code
├── tests/                 # Automated tests
├── results/               # Reproducible outputs only; no fabricated results
└── notebooks/             # Exploratory analysis notebooks
```

## Quick start

```bash
python -m pytest -q
python experiments/baseline_demo.py
```

The baseline demo uses synthetic probabilities and a synthetic graph. It must **not** be interpreted as evidence for subliminal learning.

## Research integrity

Scientific claims must identify the exact model/checkpoint, dataset version, evaluation protocol, seed policy, code revision, analysis procedure, and uncertainty calculation. Results that do not meet those requirements remain non-validated.

## Safety

Experiments involving unsafe behavior are intended to remain sandboxed and synthetic. The research scaffold does not execute destructive operations against real filesystems, credentials, production infrastructure, or external targets. See [`docs/safety.md`](docs/safety.md).

## Documentation

- [`docs/research-proposal.md`](docs/research-proposal.md)
- [`docs/methodology.md`](docs/methodology.md)
- [`docs/evidence-policy.md`](docs/evidence-policy.md)
- [`docs/reproducibility.md`](docs/reproducibility.md)
- [`docs/safety.md`](docs/safety.md)
- [`docs/author.md`](docs/author.md)
