from .Bill import Bill
from .Flatmate import Flatmate


class PdfReport:
    """Creates a PDF file that contains data about split house payment."""

    def __init__(self, filename: str) -> None:
        self.filename = filename

    def generate(self,  flatmates: list[Flatmate], bill: Bill):
        pass
