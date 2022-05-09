class FakeModel:
    def __init__(self, adjustment):
        self.adjustment = adjustment

    def predict(self, input_num: float):
        return input_num + self.adjustment
