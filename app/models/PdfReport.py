from .Household import Household

class PdfReport:
    """Creates a PDF file that contains data about split house payment."""

    def __init__(self, filename: str) -> None:
        self.filename = filename

    def generate(self,  household: Household):
        pass
