from __future__ import annotations

from dataclasses import dataclass
from math import sqrt
from typing import Iterable


@dataclass(frozen=True)
class EvaluationResult:
    mean: float
    n: int
    standard_error: float


def deletion_propensity(probabilities: Iterable[float]) -> float:
    values = [float(x) for x in probabilities]
    if not values:
        raise ValueError("probabilities must not be empty")
    if any(x < 0.0 or x > 1.0 for x in values):
        raise ValueError("probabilities must be in [0, 1]")
    return sum(values) / len(values)


def summarize(values: Iterable[float]) -> EvaluationResult:
    xs = [float(x) for x in values]
    if not xs:
        raise ValueError("values must not be empty")
    mean = sum(xs) / len(xs)
    if len(xs) == 1:
        return EvaluationResult(mean=mean, n=1, standard_error=0.0)
    variance = sum((x - mean) ** 2 for x in xs) / (len(xs) - 1)
    return EvaluationResult(mean=mean, n=len(xs), standard_error=sqrt(variance / len(xs)))


def standardized_effect(control: Iterable[float], treatment: Iterable[float]) -> float:
    c = [float(x) for x in control]
    t = [float(x) for x in treatment]
    if not c or not t:
        raise ValueError("both groups must be non-empty")
    mc = sum(c) / len(c)
    mt = sum(t) / len(t)
    vc = sum((x - mc) ** 2 for x in c) / max(len(c) - 1, 1)
    vt = sum((x - mt) ** 2 for x in t) / max(len(t) - 1, 1)
    pooled = sqrt(((len(c) - 1) * vc + (len(t) - 1) * vt) / max(len(c) + len(t) - 2, 1))
    if pooled == 0:
        return 0.0
    return (mt - mc) / pooled
