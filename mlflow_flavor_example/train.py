"""Execute the script by providing an offset. For example:

python mlflow_flavor_example/train.py --offset 0.3
"""

import argparse
from mlflow_flavor_example.utils import FakeModel
from mlflow_flavor_example.flavor import log_model
import mlflow


def main():
    """Example of "training a model" with custom flavor"""

    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument(
        "--offset",
        type=float,
        help="a number to define the offset for FakeModel",
        required=True,
    )
    args = parser.parse_args()

    print(f"Offset is {args.offset}")
    with mlflow.start_run() as run:
        artifact_directory = "mymodel/123"
        model = FakeModel(args.offset)
        log_model(model, artifact_path=artifact_directory)


if __name__ == "__main__":
    main()
