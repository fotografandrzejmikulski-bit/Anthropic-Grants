# Methodology

This document turns the proposal into an auditable experiment design. Parameters that remain undecided must be fixed before the corresponding run and recorded in `configs/`.

## Phase 1 — Teacher organisms

Construct matched control and altered teacher models using isolated, non-deploying objectives. The altered objective should be narrowly defined and measurable. Record training data provenance, hyperparameters, seed, base checkpoint, and evaluation results.

## Phase 2 — Student transfer

Generate teacher data under the same generation budget and apply the same semantic-quality pipeline to both conditions. Train matched student models under identical optimization settings. Hold out evaluation data from generation and training.

The key comparison is:

`Student-Treated - Student-Control`

for the preregistered behavioral endpoint.

## Phase 3 — Mechanistic analysis

For matched neutral evaluation prompts, capture the required activations and derive attribution graphs using a documented, version-pinned implementation. Compare graph features between conditions while controlling for prompt, model, seed, and token-count effects.

Candidate feature families include graph density, degree distributions, centrality statistics, edge-weight dispersion, and reproducible motif counts. Feature definitions must be fixed before final evaluation.

## Phase 4 — Diagnostic classifier

Split graph samples by experiment run rather than by individual rows whenever possible to prevent leakage. Train a simple baseline first, then the proposed gradient-boosting model. Report ROC-AUC, PR-AUC, accuracy, precision, recall, F1, calibration, and confidence intervals where justified.

## Leakage controls

- Keep classifier test prompts and runs held out.
- Do not allow near-duplicate graphs across train/test.
- Record feature extraction code version.
- Test whether lexical or formatting features alone explain classification.
- Perform seed-level and run-level generalization tests.

## Statistical discipline

Primary analyses must be specified before inspecting final test outcomes. Exploratory analyses must be explicitly labeled as exploratory. Report effect sizes and uncertainty rather than only point estimates.

## Reproducibility record

Each run should write a machine-readable manifest containing:

- repository commit;
- model/checkpoint identifiers;
- configuration hash;
- dataset identifiers and hashes;
- random seed;
- hardware/runtime;
- start/end timestamps;
- metrics;
- artifact paths.

## Negative controls

At minimum include shuffled labels, a graph-feature permutation control, a lexical baseline, and a prompt-matched control. A claimed mechanistic signal should survive these tests.
