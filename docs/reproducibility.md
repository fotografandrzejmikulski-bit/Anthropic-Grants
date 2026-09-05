# Reproducibility Standard

A result is reproducible only when another researcher can identify the exact code version, configuration, data provenance, model revision, seed, evaluation set, and runtime conditions used to produce it.

## Required metadata

Every experiment must record:

- Git commit SHA;
- configuration file;
- dependency lockfile/version information;
- model and tokenizer revision;
- dataset version or content hash;
- random seeds;
- hardware and relevant software runtime;
- evaluation protocol;
- output artifact identifiers.

## Determinism

Use deterministic settings when practical. When a workload is inherently nondeterministic, report that fact and repeat runs sufficiently to characterize variability.

## Artifact policy

Large model checkpoints and generated datasets should not be committed directly unless licensing, repository size, and provenance permit it. Prefer documented artifact locations and checksums.

## Result record

Each validated result should have a companion machine-readable result file containing the metric values, uncertainty estimates, sample counts, and experiment identifiers.

## Reproduction procedure

1. Checkout the recorded commit.
2. Install the recorded dependency versions.
3. Resolve the recorded model and dataset revisions.
4. Run the exact configuration.
5. Verify artifact hashes.
6. Compare metrics against the stored result manifest.
