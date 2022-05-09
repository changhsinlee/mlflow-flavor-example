from mlflow_flavor_example.utils import FakeModel


def test_fake_model():
    model = FakeModel(0.5)
    assert 3.5 == model.predict(3)
