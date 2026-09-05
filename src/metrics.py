from __future__ import annotations

from dataclasses import dataclass

@dataclass(frozen=True)
class BinaryMetrics:
    positive_rate: float
    negative_rate: float


def binary_rate(values: list[bool]) -> BinaryMetrics:
    if not values:
        raise ValueError("values must not be empty")
    positive = sum(values) / len(values)
    return BinaryMetrics(positive_rate=positive, negative_rate=1.0 - positive)
