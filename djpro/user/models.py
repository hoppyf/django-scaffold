from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from common.models import BaseModel
from user.managers import MyUserManager

"""
自定义django user模块，已在settings中注册
与django权限，用户组挂钩可以直接使用权限相关
"""


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    phone = models.CharField('手机号', max_length=11, unique=True)
    username = models.CharField('用户名', max_length=200, null=True, blank=True)
    is_staff = models.BooleanField('职员', default=False)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []
    objects = MyUserManager()

    def __str__(self):
        return self.phone

    def is_auth(self):
        return self.is_authenticated()

    def get_short_name(self):
        return self.phone
