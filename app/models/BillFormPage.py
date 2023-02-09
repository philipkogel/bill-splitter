from flask import render_template
from flask.views import MethodView
from .BillForm import BillForm


class BillFormPage(MethodView):
    def get(self):
        bill_form = BillForm()
        return render_template("bill_form_page.html", bill_form=bill_form)
