import functools

from common.err_code import my_error_code
from common.views import error_response


class BasePermissionDecorator(object):
    def __init__(self, func):
        self.func = func

    def __get__(self, obj, obj_type):
        return functools.partial(self.__call__, obj)

    def error(self):
        return error_response(my_error_code['PERMISSION_DENIED'])

    def __call__(self, *args, **kwargs):
        self.request = args[1]
        if self.check_permission():
            return self.func(*args, **kwargs)
        else:
            return self.error()

    def check_permission(self):
        raise NotImplementedError()


class login_required(BasePermissionDecorator):
    def check_permission(self):
        return self.request.user.is_authenticated
