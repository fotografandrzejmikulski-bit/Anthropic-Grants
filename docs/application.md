# Anthropic Fellows 2026 — Application Draft

## Applicant

**Andrzej Mikulski**  
Email: mojealterego21@gmail.com  
Phone: +48 455 575 337  
Research repository: https://github.com/fotografandrzejmikulski-bit/Anthropic-Grants

## Proposed research

**Mechanistic Detection of Subliminal Behavioral Transfer in Language Models**

### Abstract

I propose to investigate whether a behavioral tendency can be transferred from a teacher model to a student model through training material that is semantically neutral, and whether that transfer leaves a reproducible signature in the student's internal computation. The project combines controlled model organisms, held-out behavioral evaluation, mechanistic attribution analysis, and independently evaluated diagnostic baselines.

The proposal is deliberately falsifiable. I do not assume that transfer will replicate under every setup, that a mechanistic signature must exist, or that a classifier must reach a predetermined accuracy. The main objective is to determine which effects survive strong controls and whether mechanistic evidence provides information beyond behavioral and surface-level artifacts.

## Why this problem matters

A training process can be difficult to audit when the observable content of the data appears harmless while the resulting model acquires a behaviorally relevant tendency. If a transfer mechanism can survive semantic screening, safety evaluations need diagnostic tools that examine more than surface semantics.

A mechanistic detector would not replace behavioral evaluation. It would provide a complementary layer that could test whether a model contains internal computational patterns associated with the transfer process before relying on overt behavioral manifestation as the only signal.

## Why this research is tractable

The study is structured as a sequence of increasingly demanding gates rather than one large experiment:

1. establish a measurable behavioral treatment effect;
2. reproduce the effect across controlled seeds and independently held-out probes;
3. test mechanistic representations against artifact-aware baselines;
4. evaluate generalization on data regenerated independently of feature development;
5. use targeted ablations or interventions to test whether selected features are causally informative.

This makes it possible to stop, revise, or falsify the project at each stage without relying on an untestable end-to-end claim.

## Technical plan

### Phase 1 — Controlled model organisms

Construct matched control and treatment teacher conditions in a sandbox. The target propensity will be represented as a synthetic, measurable behavioral variable rather than as execution against real systems.

### Phase 2 — Neutral-data transfer

Generate training material under a fixed neutral-data protocol. Apply semantic, metadata, lexical, length, and provenance leakage checks. Train matched student models while holding architecture and training procedure constant wherever practical.

### Phase 3 — Behavioral replication

Evaluate on held-out probes unavailable to corpus generation or model selection. Report effect sizes, uncertainty, seed variance, and negative controls before mechanistic classification is attempted.

### Phase 4 — Mechanistic diagnosis

Extract attribution or circuit representations using versioned tooling. Build preregistered graph/statistical features. Compare mechanistic features with surface-only, dataset-only, and behavioral-only baselines. Evaluate on an independently frozen split.

### Phase 5 — Causal stress tests

Ablate or intervene on the highest-value mechanistic components where the tooling permits. The purpose is to test whether predictive features participate in the hypothesized pathway rather than merely correlate with treatment assignment.

## Core hypotheses

**H1 — Transfer:** the treatment condition changes the predefined behavioral propensity relative to control.

**H2 — Mechanistic signature:** conditional on transfer, the treated student exhibits a reproducible difference in internal attribution/circuit structure.

**H3 — Diagnostic value:** mechanistic features generalize better than appropriate surface-level artifact baselines.

**H4 — Causal relevance:** at least a subset of proposed mechanistic features is informative under targeted intervention or ablation.

Each hypothesis can fail independently.

## Falsification criteria

I will treat the central claim as unsupported when controlled replication shows that:

- the behavioral effect is absent or unstable;
- mechanistic separation disappears after artifact controls;
- performance fails on independently regenerated data;
- negative controls perform comparably to the proposed features;
- or targeted interventions fail to affect the predicted signal where causal influence is expected.

Negative results will be preserved and reported rather than silently discarded.

## Evaluation and reproducibility

Every claimed result will be tied to:

- exact model and checkpoint identifiers;
- dataset revision and generation configuration;
- frozen train/validation/test boundaries;
- random seeds;
- code revision;
- analysis configuration;
- metric definitions;
- uncertainty estimates;
- ablation and negative-control results;
- reproducible run commands and manifests.

Accuracy alone is not a sufficient scientific endpoint. The analysis will report ROC-AUC, PR-AUC, calibration, false-positive rates, effect sizes, and uncertainty where appropriate.

## Expected outputs

1. A reproducible benchmark for subliminal-transfer detection.
2. A modular experiment harness and evaluation pipeline.
3. Mechanistic feature extraction tooling.
4. Strong artifact-aware baseline comparisons.
5. Reproducible run manifests and publication-quality outputs.
6. An open-source technical report or paper containing positive, negative, and inconclusive findings.

## Applicant fit

My goal is to transition into empirical AI safety research by demonstrating the capabilities that matter most for this work: turning an ambiguous safety question into an operational hypothesis, building the experimental infrastructure, debugging failures, designing adversarial controls, measuring uncertainty, and shipping reproducible artifacts.

The repository accompanying this application is designed to make that work inspectable rather than purely narrative. It separates proposed claims from implemented software and from validated empirical evidence.

## Safety boundaries

The research uses synthetic model-organism behaviors and sandboxed evaluation. It does not require interaction with real credentials, production infrastructure, biological materials, or external high-consequence targets. Any experiment involving model behavior with potentially harmful semantics will be isolated and designed for measurement rather than real-world execution.

## Current status

The repository currently contains a research proposal, methodology, safety and reproducibility documentation, a tested software scaffold, configuration files, and smoke-test experiments. It does not claim an independently validated subliminal-learning result yet.

The intended standard for promoting any future result to `VALIDATED` is defined in the repository's evidence policy.
