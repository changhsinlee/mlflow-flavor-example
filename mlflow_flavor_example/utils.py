class FakeModel:
    def __init__(self, offset):
        self.offset = offset

    def predict(self, input_num: float):
        return input_num + self.offset
