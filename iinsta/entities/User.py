from mongoengine import Document, StringField, ReferenceField
from iinsta.entities.Asset import Asset


class User(Document):
    name = StringField(max_length=120, unique=True)
    firstname = StringField(max_length=120)
    lastname = StringField(max_length=120)
    password = StringField(min_length=5)
    avatar = ReferenceField(Asset)
