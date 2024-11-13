class ExtractError(Exception):

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.error_type = 'Extract Error'
    def __str__(self):
        return f"{self.error_type}: {self.args[0]}"