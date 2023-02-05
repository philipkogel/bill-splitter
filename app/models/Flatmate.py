from .Bill import Bill

class Flatmate:
    """Creates a person that contains information such as name and days stayed."""
    def __init__(self, name: str, days_in_house: int) -> None:
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill: Bill, household_days_sum: int) -> int:
        weight = self.days_in_house / household_days_sum
        return bill.amount * weight
