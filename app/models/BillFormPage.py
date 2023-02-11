from flask import request, render_template
from flask.views import MethodView
from .BillForm import BillForm
from .Bill import Bill
from .Household import Household
from .Flatmate import Flatmate
from .PdfReport import PdfReport


class BillFormPage(MethodView):
    def get(self):
        bill_form = BillForm()
        return render_template("bill_form_page.html", bill_form=bill_form)

    def post(self):
        bill_form = BillForm(request.form)
        bill = Bill(amount=bill_form.amount.data, period=bill_form.issue_date.data)
        household = Household(bill=bill)
        for flatmate in bill_form.flatmates:
            household.add_flatmate(
                Flatmate(
                    name=flatmate.data['flatmate_name'],
                    days_in_house=flatmate.data['days_in_house']
                )
            )
        pdf = PdfReport(filename=f"household_report_{bill.period.month}_{bill.period.year}.pdf")
        pdf.generate(household=household)
        return render_template(
            'results_page.html',
            household=household
        )
