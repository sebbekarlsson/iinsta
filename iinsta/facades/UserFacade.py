from iinsta.entities.User import User
from mongoengine.queryset import DoesNotExist
from iinsta.mongo import db


class UserFacade(object):
    @staticmethod
    def get_by_ids(ids):
        return db.page.find({
            '_id': {'$in': ids}
        })

    @staticmethod
    def get(**kwargs):
        try:
            return User.objects.get(**kwargs)
        except DoesNotExist:
            return None

    @staticmethod
    def get_all(query={}):
        return User.objects(**query).order_by('name')

    @staticmethod
    def create(**kwargs):
        c = User(**kwargs)
        c.save()

        return c

    @staticmethod
    def exists(**kwargs):
        try:
            return User.objects.get(**kwargs) is not None
        except DoesNotExist:
            return False
