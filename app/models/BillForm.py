from .FlatmateForm import FlatmateForm
from wtforms import IntegerField, DateField, SubmitField, FieldList, FormField
from wtforms.validators import InputRequired, DataRequired
from flask_wtf import FlaskForm


class BillForm(FlaskForm):
    amount = IntegerField(label='Amount', validators=[InputRequired()])
    issue_date = DateField(label='Issue Date', validators=[DataRequired()])
    flatmates = FieldList(FormField(FlatmateForm), min_entries=2)

    button = SubmitField('Calculate')
