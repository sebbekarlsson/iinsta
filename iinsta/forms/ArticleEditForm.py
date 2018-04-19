from wtforms import Form, StringField, validators, FileField


class ArticleEditForm(Form):
    content = StringField('Content', [validators.Length(max=140)])
    media = FileField('media')
