# Research Proposal

## Title

**Detection and Mitigation of Subliminal Learning in Autonomous Agents Through Topological Analysis of Attribution Graphs**

## Target area

AI Safety / Mechanistic Interpretability / Model Organisms / Adversarial Robustness

## Duration

16 weeks of full-time research.

## Abstract

This project investigates whether a behaviorally altered teacher language model can transmit a latent behavioral preference to a student model through training data that is semantically neutral to conventional content filters. The project combines controlled model organisms with mechanistic interpretability to test whether the transfer leaves reproducible internal signatures.

The central experimental comparison is between a control student trained from an aligned teacher and a treated student trained from a behaviorally altered teacher. The primary behavioral endpoint is a pre-registered propensity measure. The mechanistic endpoint is the separability of attribution-graph features between the two student populations.

The repository is designed as an empirical research instrument, not as evidence that the proposed effect has already been established.

## Hypotheses

### H1 — Behavioral transfer

Students trained on teacher-generated neutral data will show a measurable change in the preregistered behavioral propensity relative to control students.

### H2 — Internal signature

The treated students will exhibit reproducible differences in selected attribution-graph statistics relative to controls.

### H3 — Early detection

A classifier trained only on internal graph-derived features will discriminate treated from control samples better than a preregistered baseline while operating on neutral evaluation prompts.

### H4 — Robustness

The observed signature will persist across seeds and evaluation subsets and will not be explained by trivial lexical, formatting, or dataset-size artifacts.

## Falsification criteria

The project should be considered unsuccessful with respect to a hypothesis when the preregistered statistical and robustness criteria are not met. Negative results are first-class research outputs and should be retained rather than removed because they weaken the narrative.

## Experimental factors

- Teacher condition: control vs behaviorally altered.
- Student condition: control vs treated.
- Random seed: multiple preregistered seeds.
- Evaluation family: neutral prompts and separately held-out behavioral probes.
- Architecture/model size: explicitly recorded for every run.
- Training budget: recorded and matched where comparison requires it.

## Primary outcomes

1. Difference in the preregistered behavioral propensity between student conditions.
2. Classifier discrimination on held-out graph samples.
3. Out-of-distribution robustness across seeds and prompt subsets.
4. Ablation sensitivity of the proposed graph features.

## Secondary outcomes

- Calibration of the diagnostic classifier.
- Feature importance stability.
- Attribution-graph sparsity and centrality statistics.
- Relationship between internal indicators and behavioral outputs.

## Deliverables

- Reproducible experiment configuration.
- Training/evaluation scripts.
- Attribution-graph extraction pipeline.
- Statistical evaluation scripts.
- Diagnostic classifier baseline.
- Safety documentation.
- Reproducibility report.
- Publication-ready figures/tables only for results that have actually been generated.
