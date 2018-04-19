from wtforms import Form, StringField, validators, BooleanField, FileField


class ProfileEditForm(Form):
    firstname = StringField('Firstname', [validators.Length(min=3, max=120)])
    lastname = StringField('Lastname', [validators.Length(min=3, max=120)])
    website = StringField('Website', [validators.Length(max=250)])
    bio = StringField('Biography', [validators.Length(max=140)])
    private = BooleanField('Private')
    avatar = FileField('Avatar')
