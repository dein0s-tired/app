from flask_wtf import Form
from wtforms import SubmitField
from wtforms.fields.html5 import DateTimeField, DateField
# from wtforms.widgets.html5 import DateTimeInput


class SearchForm(Form):
    frame_start = DateTimeField('From:')
    frame_end = DateTimeField('To:')
    submit = SubmitField('Search')
