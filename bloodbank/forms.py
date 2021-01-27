from flask_wtf import Form
from wtforms import TextField, TextAreaField, SubmitField, validators, ValidationError
from flask_bootstrap import Bootstrap

class ContactForm(Form):
  name = TextField("Name", [validators.Required()])
  email = TextField("Email", [validators.Required()])
  subject = TextField("Subject", [validators.Required()])
  message = TextAreaField("Message", [validators.Required()])
  submit = SubmitField("Send", [validators.Required()])
