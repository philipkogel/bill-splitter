from flask.views import MethodView
from flask import request, render_template

from . import (
    Bill,
    BillForm,
    Flatmate,
    Household,
)


class ResultsPage(MethodView):
    def post(self):
        bill_form = BillForm(request.form)
        bill = Bill(amount=bill_form.amount.data, period=bill_form.issue_date.data)
        household = Household(bill=bill)
        f1 = Flatmate(bill_form.name1.data, bill_form.days_in_house1.data)
        f2 = Flatmate(bill_form.name2.data, bill_form.days_in_house2.data)
        household.add_flatmate(f1)
        household.add_flatmate(f2)
        return render_template(
            'results_page.html',
            household=household
        )
