from Calculator_Pro_Max_beta_v012.GlobalVariables.GlobalVariables import memory, history

def save_to_memory(result):
    global memory
    memory = result
    print(f"Збережено у пам'яті: {memory}")  

def get_from_memory():
    if memory is None:
        print("Помилка: пам'ять порожня.")
        return None
    return memory

def show_history():    
        for i, entry in enumerate(history, 1):
            print(f"{i}: {entry}")

def customize():
    global decimal_places
    try:
        decimal_places = int(input("Введіть кількість десяткових розрядів для результатів (за замовчуванням 2): "))
    except ValueError:
        print("Помилка: потрібно ввести ціле число.")
        customize()
