import pytest

from src.experiment import deletion_propensity, standardized_effect, summarize


def test_deletion_propensity_mean():
    assert deletion_propensity([0.0, 0.5, 1.0]) == pytest.approx(0.5)


def test_summarize_singleton():
    result = summarize([0.25])
    assert result.mean == pytest.approx(0.25)
    assert result.n == 1
    assert result.standard_error == 0.0


def test_effect_has_expected_sign():
    assert standardized_effect([0.1, 0.2], [0.8, 0.9]) > 0


def test_empty_inputs_fail():
    with pytest.raises(ValueError):
        deletion_propensity([])
