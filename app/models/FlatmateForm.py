from wtforms import Form, IntegerField, StringField


class FlatmateForm(Form):
    flatmate_name = StringField(label='Name')
    days_in_house = IntegerField(label='Days in house')
