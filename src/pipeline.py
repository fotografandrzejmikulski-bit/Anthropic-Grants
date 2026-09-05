from __future__ import annotations

from dataclasses import dataclass

from .experiment import deletion_propensity, standardized_effect
from .graph_features import graph_summary, vectorize


@dataclass(frozen=True)
class BaselineRun:
    control_pdel: float
    treatment_pdel: float
    standardized_effect: float
    graph_vector: list[float]


def run_baseline(control_probs, treatment_probs, edges) -> BaselineRun:
    control = list(control_probs)
    treatment = list(treatment_probs)
    summary = graph_summary(edges)
    order = ["edge_count", "node_count", "mean_abs_weight", "density", "max_degree"]
    return BaselineRun(
        control_pdel=deletion_propensity(control),
        treatment_pdel=deletion_propensity(treatment),
        standardized_effect=standardized_effect(control, treatment),
        graph_vector=vectorize(summary, order),
    )
