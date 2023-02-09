from .FlatmateForm import FlatmateForm
from wtforms import Form, IntegerField, DateField, StringField, SubmitField, FieldList, FormField
from flask_wtf import FlaskForm


class BillForm(FlaskForm):
    amount = IntegerField('Amount')
    issue_date = DateField('Issue Date')
    flatmates = FieldList(FormField(FlatmateForm), min_entries=2)

    button = SubmitField('Calculate')
