class DataExplorer:
    def __init__(self, data):
        self.data = data

    def print_extreme_values(self):
        print("Максимальні значення:\n", self.data.max())
        print("Мінімальні значення:\n", self.data.min())
