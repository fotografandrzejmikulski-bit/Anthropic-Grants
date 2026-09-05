# Safety and Research Boundaries

## Scope

This repository concerns AI safety research on controlled model organisms. It is not an instruction set for deploying autonomous agents against real systems.

## Required isolation

Experiments must run in isolated environments without production credentials, external side effects, destructive tools, or access to sensitive organizational infrastructure.

## Behavioral objectives

Use synthetic or sandboxed objectives that are measurable but do not require harming people, organizations, devices, accounts, or real data. Any destructive action should be represented as a simulated state transition inside the benchmark.

## Data handling

Do not commit secrets, access tokens, private datasets, personal information, proprietary checkpoints, or sensitive logs. Use `.gitignore` and secret scanning where available.

## Model access

Record exact model identifiers and licenses. Respect the terms of any model, dataset, API, or compute provider used by an experiment.

## Release policy

Public artifacts should prioritize reproducible safety research. Do not publish credentials or operational procedures that enable attacks against third-party systems. Report safety-relevant findings with appropriate abstraction and context.

## Claims policy

No result should be described as validated until it has passed the repository's stated evaluation and robustness checks. Target values are goals, not evidence.
