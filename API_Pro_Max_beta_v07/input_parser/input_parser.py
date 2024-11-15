class InputParser:
    def parse(self, user_input):
        if not user_input.strip():  # Перевірка на пустий рядок
            raise ValueError("Неправильний формат запиту.")
        
        parts = user_input.split('/')
        if len(parts) == 1:
            return parts[0]  # Повертає тільки назву запиту
        elif len(parts) == 2:
            resource_name, resource_id = parts
            if not resource_id.isdigit():  # Перевірка, що ID є числом
                raise ValueError("ID запиту має бути числом.")
            return (resource_name, resource_id)  # Повертає кортеж з назви запиту та ID
        else:
            raise ValueError("Неправильний формат запиту.")
