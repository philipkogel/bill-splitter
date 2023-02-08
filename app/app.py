"""Main console app file"""
import datetime

from flask import Flask

from models import (
    Bill,
    Flatmate,
    Household,
    PdfReport,
    HomePage,
    BillFormPage,
    ResultsPage
)

app = Flask(__name__)
app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill', view_func=BillFormPage.as_view('bill_form_page'))
app.add_url_rule('/results', view_func=ResultsPage.as_view('results_page'))

# Create household
# household = Household()
#
# print('------------------------------------------')
# print('-----      Bill Splitter CLI        ------')
# bill = Bill(
#     amount=float(input('Enter bill amount. E.g. 350: ')),
#     period=datetime.datetime.strptime(
#         input('What is the bill period? E.g. December 2022: '), '%B %Y')
# )
# household.add_bill(bill=bill)
#
# add_flatmate = True
# while add_flatmate:
#     name = input('Flatmates name: ')
#     flatmate = Flatmate(
#         name=name,
#         days_in_house=int(input(f'How many days did {name} stay in da house?: '))
#     )
#     household.add_flatmate(flatmate)
#     if len(household.flatmates) > 1 and \
#             input('To add next flatmate type: Y, type any other character to generate the report. Y/n: ').capitalize() \
#             != 'Y':
#         add_flatmate = False
#
#
# pdf = PdfReport(filename=f"household_report_{bill.period.month}_{bill.period.year}.pdf")
# pdf.generate(household=household)
