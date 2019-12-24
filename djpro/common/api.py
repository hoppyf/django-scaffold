import copy
import functools

from rest_framework.response import Response
from rest_framework.views import exception_handler


class R:
    """
    返回基类，错误码和错误内容在此处定义
    """
    ERROR = {
        'auth_required': (401, '身份认证错误'),
        'permission_denied': (403, '权限不足'),
        'not_found': (404, '内容不存在'),
        'sys_error': (500, '系统错误')
    }

    @classmethod
    def success(cls, data=''):
        return Response({'code': 0, 'msg': '成功', 'data': data})

    @classmethod
    def error(cls, error_type):
        """
        用于返回标准类别的http错误码或自定义的无参文本内容
        :param error_type:
        :return:
        """
        return Response({'code': cls.ERROR[error_type][0], 'msg': cls.ERROR[error_type][1], 'data': ''})

    @classmethod
    def warn(cls, warn_code, warn_msg):
        """
        用于返回自定义的code和带参的文本内容
        :param warn_code: 错误码
        :param warn_msg: 错误信息
        :return:
        """
        return Response({'code': warn_code, 'msg': warn_msg, 'data': ''})


def custom_exception_handler(exc, context):
    """
    rest framework默认返回的钩子，用于标准api接口输出
    :param exc:
    :param context:
    :return:
    """
    response = exception_handler(exc, context)
    if response is not None:
        response.data = {
            'code': response.status_code,
            'msg': response.data['detail'] if 'detail' in response.data else response.data,  # 兼容jwt自定义错误返回
            'data': ''
        }
    response.status_code = 200  # 视情况使用与否
    return response


def validate(serializer):
    """
    用法
    @validate(TestSerializer)
    def post(self, request):
        cls.objects.create(**request.value)
        return R.success()
    """

    def wrapper(func):
        @functools.wraps(func)
        def handle(*args, **kwargs):
            request = args[1]
            s = serializer(data=request.data)
            if s.is_valid():
                request.value = s.data
                request.serializer = s
                return func(*args, **kwargs)

        return handle

    return wrapper
