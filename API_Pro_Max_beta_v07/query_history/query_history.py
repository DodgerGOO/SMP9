class QueryHistory:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(QueryHistory, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'history'):  # Ініціалізуємо тільки один раз
            self.history = []

    def record(self, query, result):
        self.history.append({"query": query, "result": result})

    def show_history(self):
        for entry in self.history:
            print(f"Запит: {entry['query']}, Результат: {entry['result']}")
