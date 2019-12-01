from rest_framework.exceptions import APIException

"""
用于直接抛出异常
作用于view中调用其他方法需要快速抛出错误达到返回标准api输出的情况
该异常会被api.py中custom_exception_handler捕获处理
"""


class ObjDoesNotExistException(APIException):
    status_code = 404
    default_detail = '请求内容不存在'
