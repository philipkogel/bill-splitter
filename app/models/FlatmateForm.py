from wtforms import Form, IntegerField, StringField


class FlatmateForm(Form):
    name = StringField('Name')
    days_in_house = IntegerField('Days in house')
