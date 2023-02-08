from flask import render_template
from flask.views import MethodView

class HomePage(MethodView):
    def get(self):
        return render_template('index.html')
