from mongoengine import Document, StringField, ReferenceField, DateTimeField
import datetime
from iinsta.entities.User import User


class Comment(Document):
    content = StringField(max_length=140)
    user = ReferenceField(User)
    created_at = DateTimeField(default=datetime.datetime.now())
