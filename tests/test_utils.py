from mlflow_flavor_example.utils import FakeModel


def test_fake_model():
    model = FakeModel(0.5)
    assert 3.5 == model.predict(3)


def test_save_and_load_fake_model(tmp_path):
    model = FakeModel(0.6)
    path = tmp_path / "some.pickle"
    model.save(path)
    loaded_model = model.load(path)
    assert model == loaded_model
