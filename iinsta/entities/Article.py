from mongoengine import Document, StringField, ReferenceField, ListField
from iinsta.entities.Asset import Asset
from iinsta.entities.User import User
from iinsta.entities.Comment import Comment


class Article(Document):
    media = ReferenceField(Asset, required=True)
    content = StringField(max_length=140)
    user = ReferenceField(User, required=True)
    likers = ListField(ReferenceField(User))
    comments = ListField(ReferenceField(Comment))

    def like(self, user):
        if user not in self.likers:
            self.likers.append(user)
            self.save()

    def unlike(self, user):
        if user in self.likers:
            self.likers.remove(user)
            self.save()

    def comment(self, user, content):
        comment = Comment(user=user, content=content)
        comment.save()
        self.comments.append(comment)
        self.save()
