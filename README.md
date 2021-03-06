## MLFlow custom flavor examples

Example on how to create a custom flavor for MLFlow

## Running the code

### Requirements

* Python version `>=3.9` is required.

### Create environment

After cloning the repository, create a virtual environment in the repository with

```sh
python3 -m venv .venv
```

Then activate the virtual environment and install the repository as a package

```sh
# For Macs or Linux
source .venv/bin/activate

# For Windows
.venv\Scripts\activate
```

### Installing dependencies

Once the virtual environment is activated, run

```sh
# Navigate to where setup.py is
pip install -e .
```

### Start MLFlow server

Once the virtual environment is activated, run

```sh
mlflow ui
```

and it will start a local MLFlow server at the default URI: http://127.0.0.1:5000 with artifacts saved to `./mlruns`

Note: most teams run MLFlow as a remote server. I'm not going to bother with setting one up here. You will not be able to log models to Model Registry and test the full `log_model()`, `load_model()` workflow with this setup. For more information, please see [the official MLFlow doc](https://www.mlflow.org/docs/latest/index.html).

### Running tests

To run the tests, run

```sh
pytest
```

If you want to ignore the deprecation warnings, run

```sh
pytest -W ignore::DeprecationWarning
```
