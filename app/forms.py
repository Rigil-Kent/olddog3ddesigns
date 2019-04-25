from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, FileField, SubmitField
from wtforms.validators import DataRequired


class ContactForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired()])
    userfile = FileField('.stl or .obj file')
    details = TextAreaField('Additional Information')
    submit = SubmitField('Submit')