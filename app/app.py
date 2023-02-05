"""Main console app file"""
import datetime

from models import (
    Bill,
    Flatmate,
    Household,
    PdfReport
)

# Create household
household = Household()

bill = Bill(amount=120, period=datetime.datetime.now())
household.add_bill(bill=bill)
flatmate = Flatmate(name="Phil", days_in_house=20)
flatmate2 = Flatmate(name='Marc', days_in_house=25)
household.add_flatmate(flatmate=flatmate)
household.add_flatmate(flatmate=flatmate2)

print(bill.period)
print(flatmate.name)
print(household.sum_days_in())

print(f'{flatmate.name} pays: {flatmate.pays(bill, household_days_sum=household.sum_days_in())}')

pdf = PdfReport(filename="household_report.pdf")
pdf.generate(household=household)
