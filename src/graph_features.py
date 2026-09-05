from __future__ import annotations

from dataclasses import dataclass

@dataclass(frozen=True)
class GraphSummary:
    nodes: int
    edges: int
    density: float


def summarize_graph(nodes: int, edges: int) -> GraphSummary:
    if nodes < 0 or edges < 0:
        raise ValueError("nodes and edges must be non-negative")
    if nodes < 2:
        density = 0.0
    else:
        density = edges / (nodes * (nodes - 1))
    return GraphSummary(nodes=nodes, edges=edges, density=density)
