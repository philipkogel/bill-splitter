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
        for flatmate in bill_form.flatmates:
            household.add_flatmate(
                Flatmate(
                    name=flatmate.data['flatmate_name'],
                    days_in_house=flatmate.data['days_in_house']
                )
            )
        return render_template(
            'results_page.html',
            household=household
        )
