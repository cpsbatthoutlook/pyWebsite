from website import db
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, DateTimeField, IntegerField, TextField
from wtforms.validators import DataRequired, InputRequired, Length, EqualTo
from datetime import datetime

class EffortsForm(FlaskForm):
    id = IntegerField('ID', validators=[])
    category = StringField('Category', validators=[DataRequired()])
    subcategory = StringField('Sub Category', validators=[DataRequired()])
    subject = StringField('Subject', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    inserttime = DateTimeField('Insert Time')
    submit = SubmitField('Add')

class efforts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    journal = db.Column(db.String(200), unique=False, nullable=False)
    xxx = db.Column(db.Integer, default=0)
    yyy = db.Column(db.Integer, default=0)
    sitting = db.Column(db.Integer, default=0)
    inserttime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    wisdom = db.Column(db.String(200), unique=False, nullable=False)