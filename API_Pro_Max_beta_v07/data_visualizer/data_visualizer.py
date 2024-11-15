class DataVisualizer:
    
    def visualize(self, data):
        if isinstance(data, list):
            self.display_paginated(data)  # Стратегія для відображення списків
        elif isinstance(data, dict):
            self.display_item(data)  # Стратегія для одного елемента
        else:
            print("Невідомий формат даних.")

    def display_paginated(self, data):
        # Кількість записів на сторінці
        items_per_page = 10
        total_items = len(data)
        total_pages = (total_items + items_per_page - 1) // items_per_page  # Обчислюємо загальну кількість сторінок

        while True:
            # Відображення кількості сторінок
            print(f"\nКількість сторінок: {total_pages}")

            # Запит на введення номера сторінки
            user_input = input(f"Введіть номер сторінки (1-{total_pages}) або 'back' для повернення: ")
            if user_input.lower() == 'back':
                print("Повертаємося до основного меню...")
                # Виводимо доступні запити та їх кількість
                self.show_available_requests()
                return  # Повертаємося до основного меню

            try:
                page_number = int(user_input)
                if page_number < 1 or page_number > total_pages:
                    print("Помилка: Неправильний номер сторінки. Спробуйте ще раз.")
                    continue

                # Виводимо елементи на вибраній сторінці
                start_index = (page_number - 1) * items_per_page
                end_index = min(start_index + items_per_page, total_items)
                page_items = data[start_index:end_index]

                for item in page_items:
                    self.display_item(item)
                    print("\n" + "-" * 40)  # Відокремлюємо кожен елемент

            except ValueError:
                print("Помилка: Введіть коректний номер сторінки.")

    def display_item(self, item):
        # Метод для виведення окремого елемента
        print(item)

    def show_available_requests(self):
        resource_counts = {
            "posts": 100,
            "comments": 500,
            "users": 10,
            "albums": 100,
            "photos": 5000,
            "todos": 200,
        }
        print("Доступні запити та їх кількість:")
        for resource, count in resource_counts.items():
            print(f"{resource} - {count}")
