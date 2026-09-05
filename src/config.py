from dataclasses import dataclass

@dataclass(frozen=True)
class ExperimentConfig:
    seed: int = 0
    behavior_name: str = "simulated_deletion_propensity"
    evaluation_samples: int = 1000
    classifier_test_fraction: float = 0.2

    def validate(self) -> None:
        if self.evaluation_samples <= 0:
            raise ValueError("evaluation_samples must be positive")
        if not 0 < self.classifier_test_fraction < 1:
            raise ValueError("classifier_test_fraction must be between 0 and 1")
