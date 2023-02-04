"""Main console app file"""
import datetime

from models import (
    Bill,
    Flatmate,
    Household
)

# Create household
household = Household()

bill = Bill(amount=120, period=datetime.datetime.now())
household.add_bill(bill=bill)
flatmate = Flatmate(name="Phil", days_in_house=20)
household.add_flatmate(flatmate=flatmate)

print(bill.period)
print(flatmate.name)

print(f'{flatmate.name} pays: {flatmate.pays(bill, household_days_sum=household.sum_days_in())}')
