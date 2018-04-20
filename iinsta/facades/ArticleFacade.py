from iinsta.entities.Article import Article
from mongoengine.queryset import DoesNotExist
from iinsta.mongo import db


class ArticleFacade(object):
    @staticmethod
    def get_by_ids(ids):
        return db.page.find({
            '_id': {'$in': ids}
        })

    @staticmethod
    def get(**kwargs):
        try:
            return Article.objects.get(**kwargs)
        except DoesNotExist:
            return None

    @staticmethod
    def get_all(query={}, order_by='-created_at'):
        return Article.objects(**query).order_by(order_by)

    @staticmethod
    def create(**kwargs):
        c = Article(**kwargs)
        c.save()

        return c

    @staticmethod
    def exists(**kwargs):
        try:
            return Article.objects.get(**kwargs) is not None
        except DoesNotExist:
            return False
