from mongoengine import (
    Document,
    StringField,
    ReferenceField,
    ListField,
    DateTimeField
)
import datetime
from iinsta.entities.Asset import Asset
from iinsta.entities.User import User
from iinsta.entities.Comment import Comment


class Article(Document):
    media = ReferenceField(Asset, required=True)
    content = StringField(max_length=140)
    user = ReferenceField(User, required=True)
    likers = ListField(ReferenceField(User))
    comments = ListField(ReferenceField(Comment))
    tags = ListField(StringField(max_length=140))
    created_at = DateTimeField(default=datetime.datetime.now)

    def save(self, *args, **kwargs):
        for tag in self.get_tags_from_content():
            self.tags.append(tag.replace('#', ''))

        return super(Article, self).save(*args, **kwargs)

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

    def get_tags_from_content(self):
        return filter(lambda x: '#' in x, self.content.lower().split(' '))

    def get_rendered_content(self):
        words = self.content.split(' ')

        for i, word in enumerate(words):
            if word.replace('#', '') in self.tags:
                words[i] = '<a href="/feed/tag/{}">{}</a>'\
                    .format(word.replace('#', ''), word)

        return ' '.join(words)
