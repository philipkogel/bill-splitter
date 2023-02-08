from wtforms import Form, IntegerField, DateField, StringField, SubmitField

class BillForm(Form):
    amount = IntegerField('Amount', description="asd")
    issue_date = DateField('Issue Date')

    name1 = StringField('Name')
    days_in_house1 = IntegerField('Days in house')

    name2 = StringField('Name')
    days_in_house2 = IntegerField('Days in house')

    button = SubmitField('Calculate')
