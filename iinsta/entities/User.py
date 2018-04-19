from mongoengine import Document, StringField, ReferenceField, BooleanField
from iinsta.entities.Asset import Asset


class User(Document):
    name = StringField(max_length=120, unique=True)
    firstname = StringField(max_length=120)
    lastname = StringField(max_length=120)
    password = StringField(min_length=5)
    avatar = ReferenceField(Asset)
    private = BooleanField(default=False)
    bio = StringField(max_length=140)
    website = StringField(max_length=250)
