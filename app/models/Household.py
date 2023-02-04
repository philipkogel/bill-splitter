from .Bill import Bill
from .Flatmate import Flatmate


class Household:
    """Creates an object that contains all flatmates and the bill."""
    def __init__(self, bill: Bill = None, flatmates: list[Flatmate] = []) -> None:
        self.bill = bill
        self.flatmates = flatmates

    def add_bill(self, bill: Bill):
        self.bill = bill

    def add_flatmate(self, flatmate: Flatmate):
        self.flatmates.append(flatmate)

    def sum_days_in(self):
        return sum(flatmate.days_in_house for flatmate in self.flatmates)
