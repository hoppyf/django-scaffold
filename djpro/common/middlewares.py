class ErrorMiddleware:
    """
    异常处理中间件，可以hack异常处理，之前用于hack 500的情况，现在弃用
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # do something ...
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        ...
