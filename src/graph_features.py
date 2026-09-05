from __future__ import annotations

from collections import Counter
from typing import Iterable, Mapping, Sequence


def graph_summary(edges: Iterable[tuple[str, str, float]]) -> dict[str, float]:
    rows = list(edges)
    if not rows:
        return {"edge_count": 0.0, "node_count": 0.0, "mean_abs_weight": 0.0, "density": 0.0}
    nodes: set[str] = set()
    weights: list[float] = []
    degree = Counter()
    for source, target, weight in rows:
        nodes.add(source); nodes.add(target)
        weights.append(abs(float(weight)))
        degree[source] += 1
        degree[target] += 1
    n = len(nodes)
    possible = n * (n - 1) if n > 1 else 1
    return {
        "edge_count": float(len(rows)),
        "node_count": float(n),
        "mean_abs_weight": sum(weights) / len(weights),
        "density": len(rows) / possible,
        "max_degree": float(max(degree.values(), default=0)),
    }


def vectorize(summary: Mapping[str, float], order: Sequence[str]) -> list[float]:
    return [float(summary.get(name, 0.0)) for name in order]
