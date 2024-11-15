import matplotlib.pyplot as plt
from CSV_Pro_Max_beta_v08.classes.data_loader import DataLoader
from CSV_Pro_Max_beta_v08.classes.data_explorer import DataExplorer
from CSV_Pro_Max_beta_v08.classes.histogram_visualizer import HistogramVisualizer
from CSV_Pro_Max_beta_v08.classes.subplots import Subplots
from CSV_Pro_Max_beta_v08.classes.line_plot_visualizer import LinePlotVisualizer

def main():
    # Завантаження даних
    loader = DataLoader()
    data = loader.load_data()

    # Дослідження даних
    explorer = DataExplorer(data)
    explorer.print_extreme_values()
    
    # Вибір візуалізації
    visualizer = LinePlotVisualizer(data)  # Використовуємо лінійний графік
    visualizer.plot()

    # Інша візуалізація
    visualizer_hist = HistogramVisualizer(data)  # Використовуємо гістограму
    visualizer_hist.plot()

    # Декілька піддіаграм
    subplots = Subplots(data)
    subplots.create_subplots()

if __name__ == "__main__":
    main()
