from API_Pro_Max_beta_v07.api_client.api_client import APIClient
from API_Pro_Max_beta_v07.input_parser.input_parser import InputParser
from API_Pro_Max_beta_v07.data_visualizer.data_visualizer import DataVisualizer
from API_Pro_Max_beta_v07.data_storage.data_storage import DataStorage
from API_Pro_Max_beta_v07.error_handler.error_handler import ErrorHandler
from API_Pro_Max_beta_v07.query_history.query_history import QueryHistory

def run():
    api_client = APIClient()
    input_parser = InputParser()
    data_visualizer = DataVisualizer()
    data_storage = DataStorage()
    error_handler = ErrorHandler()
    query_history = QueryHistory()

    resource_counts = {
        "posts": 100,
        "comments": 500,
        "users": 10,
        "albums": 100,
        "photos": 5000,
        "todos": 200,
    }

    print("Доступні ресурси та їх кількість:")
    for resource, count in resource_counts.items():
        print(f"{resource} - {count}")

    while True:
        try:
            user_input = input("Введіть ваш запит у форматі 'назва запиту' (або 'exit' для виходу): ")
            if user_input.lower() == 'exit':
                break
            
            parsed_input = input_parser.parse(user_input)
            data = api_client.get_data(parsed_input)
            data_visualizer.visualize(data)
            data_storage.save(data)
            query_history.record(user_input, data)
        
        except Exception as e:
            error_handler.handle(e)


