class Sample:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_value(self, new_value):
        self.value = new_value

    def __repr__(self):
        return f"Sample(value={self.value})"
