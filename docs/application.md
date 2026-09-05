# Anthropic Fellows 2026 — Application Draft

**Applicant:** Andrzej Mikulski  
**Email:** mojealterego21@gmail.com  
**Phone:** +48 455 575 337  
**Repository:** https://github.com/fotografandrzejmikulski-bit/Anthropic-Grants

## Project title

**Mechanistic Detection of Subliminal Behavioral Transfer in Language Models**

## One-sentence proposal

I propose to determine whether subliminal transfer of a behavioral tendency through semantically neutral training data leaves a reproducible mechanistic signature in the student's internal computation, and whether that signature can support an independently validated early-warning diagnostic.

## Why this matters

A safety-relevant transfer mechanism that survives semantic filtering would create a gap between surface-level data screening and model-level behavioral integrity. A mechanistic detector could provide a complementary diagnostic layer: instead of waiting for the target behavior to manifest, it would test whether the internal computation has acquired a reproducible signature associated with the transfer process.

## Research plan

The work is organized as four empirical phases:

1. **Controlled model organisms.** Build matched control and treatment conditions in a sandboxed environment, with a behavior that is operationally measurable and does not depend on real-world destructive actions.
2. **Neutral-data transfer.** Generate semantically neutral training corpora from the matched teachers, apply explicit leakage controls, and train matched student models.
3. **Behavioral confirmation.** Measure the target propensity on held-out probes with multiple seeds and report effect sizes and uncertainty before attempting mechanistic classification.
4. **Mechanistic diagnosis.** Extract attribution/circuit representations, derive preregistered graph features, and test a classifier on an independently held-out split. Ablations will test whether the classifier relies on genuine mechanistic structure rather than superficial artifacts.

## Falsification criteria

The central hypothesis will be treated as unsupported when one or more of the following persist under controlled replication:

- the treatment does not produce a statistically distinguishable behavioral effect;
- mechanistic representations do not separate treatment from control beyond appropriate baselines;
- predictive performance collapses under an independently generated holdout or artifact-controlled split;
- matched negative controls produce comparable predictive performance;
- the proposed features fail causal or intervention-based validation.

A negative result will be retained as a meaningful research outcome.

## Evaluation standard

The project will report:

- exact model/checkpoint identifiers;
- dataset and generator revisions;
- train/validation/test separation;
- random seeds;
- effect sizes and confidence intervals or bootstrap uncertainty;
- classifier ROC-AUC, PR-AUC, precision, recall, calibration, and false-positive rate where applicable;
- ablation and negative-control results;
- complete run manifests and code revision identifiers.

No threshold such as 95% accuracy is assumed in advance. Performance thresholds are hypotheses to be evaluated against baselines and uncertainty, not guaranteed outcomes.

## Researcher fit

My objective is to transition into empirical AI safety research by demonstrating execution: converting an ambiguous safety question into a controlled experiment, implementing the analysis pipeline, testing failure modes, documenting negative results, and shipping reproducible research artifacts.

## Deliverables

By the end of the project I intend to produce:

1. a reproducible benchmark for subliminal-transfer detection;
2. a documented experimental harness and evaluation pipeline;
3. mechanistic feature extraction tooling;
4. independently evaluated diagnostic baselines;
5. an open-source research repository with complete provenance;
6. a technical report or paper describing positive, negative, and inconclusive findings.

## Scope and safety

All unsafe behavior is represented as synthetic, sandboxed model-organism behavior. The project does not require execution against real credentials, production systems, personal data, external infrastructure, biological materials, or other high-consequence targets. Safety boundaries and release criteria are documented in `docs/safety.md`.

## Current evidence status

This repository currently contains an implementation scaffold and research proposal. It does **not** claim that subliminal learning has been independently replicated here. Any future empirical claim will be promoted to `VALIDATED` only after satisfying the evidence policy in this repository.
