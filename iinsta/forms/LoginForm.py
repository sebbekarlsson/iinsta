from wtforms import Form, StringField, validators, PasswordField


class LoginForm(Form):
    name = StringField('Username', [validators.Length(min=4, max=120)])
    password = PasswordField('Password')
