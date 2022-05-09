from setuptools import setup

setup(
    name="mlflow_flavor_example",
    version="0.1",
    description="Examples for creating custom MLFlow flavors",
    author="Chang Hsin Lee",
    license="MIT",
    packages=["mlflow_flavor_example"],
    install_requires=["mlflow", "pytest", "pytest-mock"],
    # Require 3.9 before Apple M1 has trouble installing numpy for versions <= 3.8
    python_requires=">=3.9",
    zip_safe=False,
)
