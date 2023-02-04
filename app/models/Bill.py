from datetime import datetime


class Bill:
    """Object that contains data about a bill."""
    def __init__(self, amount: int, period: datetime) -> None:
        self.amount = amount
        self.period = period
