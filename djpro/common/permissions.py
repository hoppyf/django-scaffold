import functools

from common.api import R

"""
权限定义及相关处理逻辑
用于APIView的permission_classes中
"""


class BasePermissionDecorator:
    def __init__(self, func):
        self.func = func

    def __get__(self, obj, obj_type):
        return functools.partial(self.__call__, obj)

    def error(self):
        return R.error('permission_denied')

    def __call__(self, *args, **kwargs):
        self.request = args[1]
        if self.check_permission():
            return self.func(*args, **kwargs)
        else:
            return self.error()

    def check_permission(self):
        raise NotImplementedError


class LoginRequired(BasePermissionDecorator):
    def check_permission(self):
        return self.request.user.is_authenticated
