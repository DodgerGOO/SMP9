def log_error(error_message):
    with open("error_log.txt", "a") as log_file:
        log_file.write(f"Помилка: {error_message}\n")

def log_calculation(expression, result):
    with open("calculation_log.txt", "a") as log_file:
        log_file.write(f"Обчислення: {expression} = {result}\n")
