import matplotlib.pyplot as plt
from abc import ABC, abstractmethod


class BaseVisualizer(ABC):
    def __init__(self, data):
        self.data = data

    @abstractmethod
    def plot(self):
        pass

    def save_plot(self, filename):
        plt.savefig(filename)
        print(f"Файл збережено як {filename}")
        plt.close()

    def show_plot(self):
        plt.show()

