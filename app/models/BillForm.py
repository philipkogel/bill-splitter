from wtforms import Form, IntegerField, DateField

class BillForm(Form):
    amount = IntegerField('Amount')
    period = DateField('Issue Date')
