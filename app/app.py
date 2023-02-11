"""Main console app file"""
import datetime

from flask import Flask

from models import (
    HomePage,
    BillFormPage,
)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill', view_func=BillFormPage.as_view('bill_form_page'))
