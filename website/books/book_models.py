from website import db
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, DateTimeField, IntegerField, TextField
from wtforms.validators import DataRequired, InputRequired, Length, EqualTo
from datetime import datetime

categories=['Apache', 'Bank', 'Brampton', 'Business', 'Canada', 'Car', 'Communication', 'ComputerSales', 'Daddyji', 'Education',
'Efficiency', 'Entertainment', 'Food', 'Finance', 'Government', 'HomeImprovement', 'HTML', 'Java', 'Jojo', 'Linux',
'Meher', 'MQ', 'MicroSoft', 'Music', 'MySQL', 'OpenSource', 'Oracle', 'Others', 'Perl', 'Personal',
'Python', 'RealEstate', 'Rental', 'Research', 'Security', 'Shopping', 'Sol10', 'SysAdmin', 'Tax', 'Virtualization',
'Weblogic', 'Websphere']


class Bookmarks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    catagory = db.Column(db.String(40), unique=False, nullable=False)
    details = db.Column(db.String(100), unique=False, nullable=False)
    inserttime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    url = db.Column(db.String(120), unique=True)
    def __init__(self, catagory, details, url):
        self.catagory = catagory
        self.details = details
        self.url = url
    def __repr__(self):
        return '<Bookmarks %r>' % self.details



class BookmarksForm(FlaskForm):
    id = IntegerField('ID', validators=[DataRequired()])
    # catagory = StringField('Category', validators=[DataRequired()])
    catagory = SelectField('Category', choices=[(c1,c1) for c1 in categories], validators=[DataRequired()] )
    details = StringField('Details', validators=[DataRequired()])
    inserttime = StringField('Insert time', validators=[DataRequired()])
    url = TextField('URL', validators=[DataRequired()])
    submit=SubmitField('Accept')
