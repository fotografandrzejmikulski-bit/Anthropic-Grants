from src.config import ExperimentConfig
from src.graph_features import summarize_graph
from src.metrics import binary_rate


def test_config_validates():
    ExperimentConfig().validate()


def test_binary_rate():
    result = binary_rate([True, False, True, False])
    assert result.positive_rate == 0.5
    assert result.negative_rate == 0.5


def test_graph_density():
    result = summarize_graph(3, 2)
    assert result.nodes == 3
    assert result.edges == 2
    assert result.density == 1 / 3
