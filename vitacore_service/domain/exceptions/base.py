class DomainError(Exception):
    def __init__(self, message: str | None = None):
        self.message = message

    def __str__(self) -> str:
        return (
            str(self.__class__.__name__) + f": {self.message}" if self.message else ""
        )
