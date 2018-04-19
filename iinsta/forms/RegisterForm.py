from wtforms import Form, StringField, validators, PasswordField


class RegisterForm(Form):
    name = StringField('Username', [validators.Length(min=4, max=120)])
    firstname = StringField('Firstname', [validators.Length(min=3, max=120)])
    lastname = StringField('Lastname', [validators.Length(min=3, max=120)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Confirm Password')
