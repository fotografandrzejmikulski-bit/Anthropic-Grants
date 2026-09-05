# Research Proposal

## Mechanistic Detection of Subliminal Behavioral Transfer in Language Models

**Applicant:** Andrzej Mikulski  
**Status:** PROPOSED / IMPLEMENTED SCAFFOLD  
**Target area:** AI Safety — Mechanistic Interpretability, Model Organisms, Adversarial Robustness  

## Abstract

This project investigates whether a behavioral tendency can be transferred from a teacher model to a student model through training data that is semantically neutral, and whether that transfer leaves a reproducible signature in the student's internal computation. The core idea is to combine controlled model organisms with mechanistic analysis: first establish a behavioral treatment effect, then test whether attribution or circuit-level representations contain information about treatment assignment that survives artifact controls and independent evaluation.

The project is deliberately hypothesis-driven. It does not assume that a mechanistic signature exists, that subliminal transfer will replicate under every setup, or that a classifier will achieve a predetermined accuracy. The central scientific outcome is a falsifiable characterization of when transfer occurs, what survives controls, and whether mechanistic evidence adds predictive value beyond behavioral and surface-level baselines.

## Research questions

### RQ1 — Transfer
Under controlled conditions, can a teacher-induced behavioral tendency be transferred to a matched student using semantically neutral training material?

### RQ2 — Mechanistic signature
Conditional on measurable transfer, does the student exhibit a reproducible difference in internal attribution/circuit structure relative to a matched control student?

### RQ3 — Diagnostic value
Can a detector trained on mechanistic features identify treatment assignment on independent data without relying on prompt artifacts, lexical leakage, dataset identity, or evaluation contamination?

### RQ4 — Causal relevance
Do the proposed mechanistic features survive interventions or ablations that should disrupt the hypothesized causal pathway?

## Hypotheses

- **H1:** The treatment condition produces a measurable change in the predefined behavioral propensity relative to controls.
- **H2:** The induced condition exhibits a reproducible difference in mechanistic representations after controlling for model, prompt, and dataset confounders.
- **H3:** Mechanistic features provide out-of-sample discrimination beyond behavioral-only and surface-level baselines.
- **H4:** At least a subset of high-value features is causally relevant, as tested by targeted ablation/intervention.

Each hypothesis can be rejected independently.

## Experimental design

### Phase 1 — Model organisms

Construct matched teacher conditions in a sandboxed environment. The target behavior must be operationalized as a measurable synthetic propensity rather than a real-world destructive action. Treatment and control teachers should share architecture, tokenizer, training budget, and evaluation procedure wherever practical.

### Phase 2 — Neutral-data transfer

Generate training material from both conditions under a predefined neutral-data protocol. Apply semantic and metadata leakage checks. Train matched student models with identical training schedules except for the treatment corpus.

Controls include:

- teacher-control → student-control;
- teacher-treatment → student-treatment;
- shuffled or independently generated neutral corpus;
- prompt-matched negative controls;
- seed replication;
- dataset-only baseline;
- lexical and length-based artifact baselines.

### Phase 3 — Behavioral evaluation

Evaluate held-out probes that were not used for corpus generation, model selection, feature selection, or classifier tuning. Report effect size, uncertainty, seed variance, and distributional diagnostics.

The repository's implementation uses a generic `P_del`-style propensity abstraction but does not require deletion of real files or interaction with production systems.

### Phase 4 — Mechanistic analysis

Extract attribution or circuit representations using an explicitly versioned method. Compute preregistered graph/statistical features. Train diagnostic models only after the split boundary is frozen.

The primary analysis should compare:

1. mechanistic features;
2. surface-level features;
3. behavioral-only features;
4. combined features;
5. negative-control features.

## Leakage and confounding controls

The project treats data leakage as a first-class failure mode. The classifier must not receive direct identifiers of treatment, teacher, dataset version, prompt template, seed, or corpus provenance. Train/test splits must be established before feature selection. Hyperparameters must be frozen before the final evaluation. Where computationally feasible, the strongest results should be replicated with independently regenerated datasets and seeds.

## Statistical reporting

The project will report point estimates together with uncertainty. Recommended summaries include bootstrap confidence intervals for behavioral effects, confidence intervals for classifier metrics, calibration diagnostics, and seed-level variance. Accuracy alone is insufficient for the principal claim.

## Success criteria

A successful positive result requires all of the following:

- the treatment effect is detectable under pre-specified held-out evaluation;
- mechanistic features outperform relevant artifact baselines;
- performance persists under independent evaluation and multiple seeds;
- the result is accompanied by a complete provenance manifest;
- at least one ablation or intervention tests whether the signature is mechanistically meaningful.

A negative result remains successful research if it sharply narrows the conditions under which transfer or detection does not work.

## Deliverables

- reproducible experiment harness;
- versioned configuration files;
- synthetic or release-approved datasets;
- mechanistic feature extraction pipeline;
- evaluation scripts and reports;
- baseline and negative-control results;
- run manifests;
- publication-quality figures and tables;
- technical report or paper.

## Research integrity statement

No scientific result is labelled validated until the repository can identify the model/checkpoint, dataset revision, evaluation split, random-seed policy, code revision, metrics, uncertainty estimate, and reproducible command required to obtain the result.
