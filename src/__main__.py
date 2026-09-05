from .config import ExperimentConfig


def main() -> None:
    config = ExperimentConfig()
    config.validate()
    print("Anthropic-Grants experiment scaffold OK")


if __name__ == "__main__":
    main()
