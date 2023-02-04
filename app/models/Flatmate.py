from .Bill import Bill


class Flatmate:
    """Creates a person that contains information such as name and days stayed."""
    def __init__(self, name: str, days_in_house: int):
        self.name = name
        self.days_stayed = days_in_house

    def pays(self, bill: Bill):
        return bill.amount / 2
