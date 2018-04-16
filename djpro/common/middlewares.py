import json

import logging
from django.http import HttpResponse

logger = logging.getLogger('app_info')


class ErrorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # do something ...
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        logger.error(
            'path:{} method:{} user:{} --> why:{}'.format(request.path, request.method, request.user, exception))
        return HttpResponse(json.dumps({'code': '500', 'msg': '系统异常', 'data': ''}, ensure_ascii=False),
                            content_type='application/json;charset=utf-8')
