import pytest
import os
from mlflow_flavor_example.utils import FakeModel
from mlflow_flavor_example.flavor import log_model, load_model
import mlflow


@pytest.fixture
def fake_model():
    return FakeModel(offset=1.5)


def test_log_model_and_load_model(fake_model):
    try:
        model_info = log_model(model=fake_model, artifact_path="123model")
        run_id = mlflow.active_run().info.run_id
        model_uri = f"runs:/{run_id}/123model"
        assert model_info.model_uri == model_uri

        loaded_model = load_model(model_uri=model_uri)
        assert fake_model == loaded_model
    finally:
        mlflow.end_run()
