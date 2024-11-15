import matplotlib.pyplot as plt
from CSV_Pro_Max_beta_v08.classes.base_visualizer import BaseVisualizer

class LinePlotVisualizer(BaseVisualizer):
    def plot(self):
        if 'x_column' not in self.data.columns or 'y_column' not in self.data.columns:
            print("Дані для візуалізації не знайдені!")
            return
        
        plt.figure()
        plt.plot(self.data['x_column'], self.data['y_column'], marker='o', color='b', linestyle='-')
        plt.title("Лінійний графік")
        plt.xlabel("X-вісь")
        plt.ylabel("Y-вісь")
        plt.grid(True)
        self.save_plot(r"C:\Users\Vlad\Desktop\унік\пітоній\All_Super_Ultra_Pro_Max_beta_v09\CSV_Pro_Max_beta_v08\line_plot.png")
               