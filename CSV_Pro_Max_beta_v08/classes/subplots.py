import matplotlib.pyplot as plt

class Subplots:
    def __init__(self, data):
        self.data = data

    def create_subplots(self):
        fig, axs = plt.subplots(1, 2, figsize=(10, 5))
        axs[0].plot(self.data['x_column'], self.data['y_column'], marker='o', color='b', linestyle='-')        
        axs[1].hist(self.data['y_column'])        
        plt.show()
