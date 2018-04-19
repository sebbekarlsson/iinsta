from iinsta.entities.Asset import Asset
from mongoengine.queryset import DoesNotExist
from iinsta.mongo import db


class AssetFacade(object):
    @staticmethod
    def get_by_ids(ids):
        return db.page.find({
            '_id': {'$in': ids}
        })

    @staticmethod
    def get(**kwargs):
        try:
            return Asset.objects.get(**kwargs)
        except DoesNotExist:
            return None

    @staticmethod
    def get_all():
        return Asset.objects().order_by('name')

    @staticmethod
    def create(**kwargs):
        c = Asset(**kwargs)
        c.save()

        return c

    @staticmethod
    def exists(**kwargs):
        try:
            return Asset.objects.get(**kwargs) is not None
        except DoesNotExist:
            return False
