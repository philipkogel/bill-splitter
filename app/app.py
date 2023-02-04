"""Main console app file"""
import datetime

from models import (
    Bill,
    Flatmate
)

bill = Bill(amount=100, period=datetime.datetime.now())
flatmate = Flatmate(name="Phil", days_in_house=20)

print(bill.period)
print(flatmate.name)

print(flatmate.pays(bill))
