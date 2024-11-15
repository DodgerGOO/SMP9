from Calculator_Pro_Max_beta_v06.GlobalVariables.GlobalVariables import memory, history
from Calculator_Pro_Max_beta_v06.functions.functions import get_operator,  calculate
from Calculator_Pro_Max_beta_v06.tools.tools import save_to_memory, get_from_memory, show_history
from Calculator_Pro_Max_beta_v06.AppSettings.AppSettings import decimal_places


class Calculator:
    def __init__(self):
        self.memory = memory
        self.history = history
        self.decimal_places = decimal_places      
       
    def get_numbers(self):
        choice = input("Використати значення з пам'яті? (так/ні): ").lower()  
        if choice not in ['так', 'ні']:               
               print("Помилка: введіть так або ні.")
               return self.get_numbers()           
        if choice == 'так':
            num1 = get_from_memory()                  
            if num1 is None:  
                return self.get_numbers() 
            print(f"Використано значення з пам'яті: {num1}")
        else:
            try:
                num1 = float(input("Введіть перше число: "))
            except ValueError:
                print("Помилка: потрібно ввести дійсне число.")
                return self.get_numbers()

        try:
            num2 = float(input("Введіть друге число: "))
            return num1, num2
        except ValueError:
            print("Помилка: потрібно ввести дійсне число.")
            return self.get_numbers()        

    def run(self):     
        while True:
            num1, num2 = self.get_numbers()
            operator = get_operator()
            result = calculate(num1, num2, operator)            
            
            if result is not None:
                result = round(result, self.decimal_places)
                print(f"Результат: {result}")
                self.history.append(f"{num1} {operator} {num2} = {result}")                
                self.ask_save_to_memory(result)
                
            if not self.ask_continue():
                break

            if self.ask_view_history():
                show_history()      

            if self.ask_customize():
                self.customize()
     
             
    def ask_save_to_memory(self, result):       
        save_choice = input("Зберегти результат у пам'ять? (так/ні): ").lower()
        if save_choice == 'так':
            save_to_memory(result)

    def ask_continue(self):        
        return input("Чи хочете виконати ще одне обчислення? (так/ні): ").lower() == 'так'

    def ask_view_history(self):        
        return input("Бажаєте переглянути історію? (так/ні): ").lower() == 'так'
    
    def ask_customize(self):        
        return input("Бажаєте налаштувати калькулятор? (так/ні): ").lower() == 'так'    
    
    def customize(self):
        
        try:
            new_decimal_places = int(input("Введіть кількість десяткових розрядів для результатів (за замовчуванням 2): "))
            self.decimal_places = new_decimal_places
            print(f"Кількість десяткових розрядів змінена на: {self.decimal_places}")
            self.history.append(f"Користувач змінив кількість десяткових знаків на: {self.decimal_places}")
        except ValueError:
            print("Помилка: потрібно ввести ціле число.")
            self.history.append("Помилка при налаштуванні десяткових розрядів.")
    
    