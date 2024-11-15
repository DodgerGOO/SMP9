import matplotlib.pyplot as plt
from CSV_Pro_Max_beta_v08.classes.base_visualizer import BaseVisualizer

class HistogramVisualizer(BaseVisualizer):
    def plot(self):
        if 'y_column' not in self.data.columns:
            print("Дані для візуалізації не знайдені!")
            return
        
        plt.figure()
        plt.hist(self.data['y_column'], bins=10, color='g', edgecolor='black')
        plt.title("Гістограма")
        plt.xlabel("Значення")
        plt.ylabel("Частота")        
        self.save_plot(r"C:\Users\Vlad\Desktop\унік\пітоній\All_Super_Ultra_Pro_Max_beta_v09\CSV_Pro_Max_beta_v08\histogram_plot.png")
        
        