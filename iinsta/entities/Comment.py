from mongoengine import Document, StringField, ReferenceField
from iinsta.entities.User import User


class Comment(Document):
    content = StringField(max_length=140)
    user = ReferenceField(User)
