class messageService:
    @staticmethod
    def is_greeting(value: str) -> bool:
        value_lowercase = value.lower()
        return "message" in value_lowercase
