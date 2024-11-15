from common.logger import Logger
from common.api_tools import APITools
logger = Logger()
class APIClient:
    base_url = "https://jsonplaceholder.typicode.com"
    
    def get_data(self, endpoint):
        full_url = f"{self.base_url}/{endpoint}"
        data = APITools.get(full_url)
        if data:
            logger.log_info(f"Успішний запит до {full_url}")
        else:
            logger.log_error(f"Не вдалося отримати дані з {full_url}")
        return data