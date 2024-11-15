import requests

class APITools:
    @staticmethod
    def get(endpoint):
        """
        Виконує GET-запит до API.
        """
        try:
            response = requests.get(endpoint)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Помилка запиту: {e}")
            return None
