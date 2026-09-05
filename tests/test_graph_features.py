import pytest

from src.graph_features import graph_summary, vectorize


def test_graph_summary():
    summary = graph_summary([("a", "b", 2.0), ("b", "c", -1.0)])
    assert summary["edge_count"] == 2.0
    assert summary["node_count"] == 3.0
    assert summary["mean_abs_weight"] == pytest.approx(1.5)


def test_vectorize_missing_values_default_to_zero():
    assert vectorize({"x": 1}, ["x", "y"]) == [1.0, 0.0]
