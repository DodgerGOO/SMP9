from Calculator_Pro_Max_beta_v06.GlobalVariables.GlobalVariables import memory, history

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
    if history:
        for i, entry in enumerate(history, 1):
            print(f"{i}: {entry}")
    else:
        print("Історія порожня.")



