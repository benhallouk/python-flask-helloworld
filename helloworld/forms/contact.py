from flask_wtf import Form
from wtforms.fields import StringField
from flask.ext.wtf.html5 import EmailField
from wtforms.validators import DataRequired, email

class ContactForm(Form):
    name = StringField('name', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired(), email()])
    message = StringField('message', validators=[DataRequired()])

    def validate(self):
        #put the custom validation here
        if not Form.validate(self):
            return False        
        return True