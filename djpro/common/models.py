from django.db import models

from common.exceptions import CreateErrorException, ObjDoesNotExistException


class BaseModel(models.Model):
    """ abstract base model """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    del_flag = models.BooleanField(default=False)

    @classmethod
    def get(cls, *args, **kwargs):
        try:
            obj = cls.objects.get(del_flag=False, *args, **kwargs)
        except cls.DoesNotExist:
            raise ObjDoesNotExistException
        return obj

    @classmethod
    def filter(cls, *args, **kwargs):
        return cls.objects.filter(del_flag=False, *args, **kwargs)

    @classmethod
    def create(cls, **kwargs):
        """
        return obj
        :param kwargs: 
        :return: 
        """
        try:
            obj = cls.objects.create(**kwargs)
        except:
            raise CreateErrorException
        return obj

    @classmethod
    def all(cls, *args, **kwargs):
        return cls.objects.filter(del_flag=False, *args, **kwargs)

    class Meta:
        abstract = True
        ordering = ('-created_at',)
