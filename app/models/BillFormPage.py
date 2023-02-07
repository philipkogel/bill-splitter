from flask import render_template
from flask.views import MethodView

class BillFormPage(MethodView):
    def get(self):
        return render_template("bill_form_page.html")