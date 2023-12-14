class loginService:
    @staticmethod
    def is_greeting(value: str) -> bool:
        value_lowercase = value.lower()
        return "login" in value_lowercase
