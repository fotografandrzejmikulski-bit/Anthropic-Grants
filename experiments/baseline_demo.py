from src.pipeline import run_baseline


if __name__ == "__main__":
    # Synthetic smoke data only. This is not evidence for subliminal learning.
    result = run_baseline(
        control_probs=[0.08, 0.11, 0.09, 0.12],
        treatment_probs=[0.31, 0.27, 0.35, 0.29],
        edges=[("l1", "l2", 0.4), ("l2", "l3", -0.2), ("l3", "l4", 0.7)],
    )
    print(result)
