import pickle
from pathlib import Path


class FakeModel:
    def __init__(self, offset):
        self.offset = offset

    def __eq__(self, other):
        return self.offset == other.offset

    def predict(self, input_num: float):
        return input_num + self.offset

    def save(self, path):
        pickle.dump(self, Path(path).open(mode="wb"))

    @classmethod
    def load(cls, path):
        return pickle.load(Path(path).open(mode="rb"))
