from website import db
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, DateTimeField, IntegerField, TextField, TextAreaField
from wtforms.validators import DataRequired, InputRequired, Length, EqualTo
from datetime import datetime

class knowledgebase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(30), unique=False, nullable=False)
    subcategory = db.Column(db.String(30), unique=False, nullable=False)
    subject = db.Column(db.String(100), unique=False, nullable=False)
    description = db.Column(db.Text, unique=False, nullable=True)
    inserttime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow )

    def __repr__(self):
        return f"knowledgebase('{self.category}', '{self.subcategory} ', '{self.subject} ', ' {self.inserttime} ' ) "


class KnowledgebaseForm(FlaskForm):
    id = IntegerField('ID', validators=[])
    category = StringField('Category', validators=[DataRequired()])
    subcategory = StringField('Sub Category', validators=[DataRequired()])    
    subject = StringField('Subject', validators=[DataRequired()])    
    description = StringField('Description', validators=[DataRequired()])    
    inserttime = DateTimeField('Insert Time')
    submit = SubmitField('Add')
    
    