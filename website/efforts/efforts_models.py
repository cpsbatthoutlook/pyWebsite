from website import db
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, DateTimeField, IntegerField, TextField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, InputRequired, Length, EqualTo
from datetime import datetime

#https://docs.sqlalchemy.org/en/13/orm/tutorial.html#querying  ## Query hints
class efforts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sitting = db.Column(db.Integer, unique=False, default=0)
    siteven = db.Column(db.Integer, unique=False, default=0)
    sitoth = db.Column(db.Integer, unique=False, default=0)
    anger = db.Column(db.Integer, unique=False, default=0)
    harsh = db.Column(db.Integer, unique=False, default=0)
    abusive = db.Column(db.Integer, unique=False, default=0)
    readb = db.Column(db.Boolean, default=False, nullable=False)
    s_e = db.Column(db.Boolean, default=False, nullable=False)
    x = db.Column(db.Integer, unique=False, default=0)
    y = db.Column(db.Integer, unique=False, default=0)
    y = db.Column(db.Integer, unique=False, default=0)
    journal = db.Column(db.Text, unique=False, nullable=False)
    wisdom = db.Column(db.String(200), unique=False, nullable=True)
    help_good = db.Column(db.String(200), unique=False, nullable=True)
    inserttime = db.Column(db.Date, nullable=False,unique=True, default=datetime.now )
    waketime = db.Column(db.Time, nullable=False, default=datetime.now )
    sleeptime = db.Column(db.Time, nullable=False, default=datetime.now )
    bother= db.Column(db.String(200), unique=False, nullable=True)

    def __repr__(self):
        return f"efforts('{self.inserttime}', '{self.waketime} ', '{self.sleeptime} ', '{self.sitting} ', ' {self.wisdom} ' ) "

class EffortsForm(FlaskForm):
    id = IntegerField('ID', validators=[])
    journal = TextAreaField('Daily Journal', validators=[DataRequired(message="How did you day go?")])
    wisdom = StringField('Wisdom', validators=[DataRequired(message="Learnt anything new?")])    
    bother = StringField('Bother', validators=[DataRequired(message="What was bothering during meditation?")])    
    inserttime = DateTimeField('Date', validators=[DataRequired(message="defaults to date of enter")])
    # waketime = DateTimeField('Wake up ' , validators=[DataRequired(message="What time you left bed?")])
    # sleeptime = DateTimeField('Went to bed' , validators=[DataRequired(message="What time you went to bed?")])
    waketime = DateTimeField('Wake up ' , validators=[])
    sleeptime = DateTimeField('Went to bed' , validators=[])
    sitting = IntegerField('How long did you sit in morning?')
    siteven = IntegerField('How long did you sit in evening?')
    sitoth = IntegerField('How long did you sit at any other time?')
    x = IntegerField('XX', validators=[DataRequired()])
    y = IntegerField('YY', validators=[DataRequired()])
    help_good = StringField('Angels in this world:')
    submit = SubmitField('Add')
    anger = IntegerField('Anger?')
    harsh = IntegerField('Harsh?')
    abusive = IntegerField('Abusive?')
    readb = BooleanField('Read spiritual literature?')
    s_e = BooleanField('s_e?')
    


def createDB():
    return db.create_all()

def dropDB():
    return db.drop_all()

def addDB():
    db.session.add(efforts(sitting=0, x=0,y=1,journal="First Test entry", wisdom=" learning  "))
    db.session.commit()
    return  efforts.query.all()
    