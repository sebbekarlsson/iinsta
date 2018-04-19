from mongoengine import (
    Document,
    StringField,
    ReferenceField,
    BooleanField,
    ListField
)
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
    followers = ListField(ReferenceField('User'))

    def follow(self, user):
        if user not in self.followers:
            self.followers.append(user)
            self.save()

    def unfollow(self, user):
        if user in self.followers:
            self.followers.remove(user)
            self.save()
