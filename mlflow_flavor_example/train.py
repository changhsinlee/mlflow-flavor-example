import argparse

"""Execute the script by providing an offset. For example:

python mlflow_flavor_example/train.py --offset 0.3
"""
from mlflow_flavor_example.utils import FakeModel


def main():
    """Example of "training a model" with custom flavor"""

    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument(
        "--offset", type=float, help="a number to define the offset for FakeModel"
    )
    args = parser.parse_args()

    print(f"Offset is {args.offset}")
    model = FakeModel(args.offset)


if __name__ == "__main__":
    main()
