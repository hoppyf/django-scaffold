from django.db import models

"""
所有model的基类，包含创建时间和最后修改时间和软删除标志
视情况可加入创建人和修改人字段
常用查询处理了软删除逻辑
meta中不推荐加入排序规则，是影响查询效率的
"""


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    del_flag = models.BooleanField(default=False)

    @classmethod
    def get(cls, *args, **kwargs):
        return cls.objects.get(del_flag=False, *args, **kwargs)

    @classmethod
    def filter(cls, *args, **kwargs):
        return cls.objects.filter(del_flag=False, *args, **kwargs)

    @classmethod
    def create(cls, **kwargs):
        return cls.objects.create(**kwargs)

    @classmethod
    def all(cls, *args, **kwargs):
        return cls.objects.filter(del_flag=False, *args, **kwargs)

    def s_delete(self):
        self.del_flag = True
        self.save()
        return self

    class Meta:
        abstract = True
