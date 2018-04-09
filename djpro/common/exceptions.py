from rest_framework.exceptions import APIException


class CreateErrorException(APIException):
    """
    create obj error exception
    """
    status_code = 400
    default_detail = '参数异常'


class ObjDoesNotExistException(APIException):
    """
    cls `get` method doesn't exist exception
    """
    status_code = 404
    default_detail = '请求内容不存在'
