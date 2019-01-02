import functools

from common.views import serializer_error


def validate_serializer(serializer):
    """
    @validate_serializer(TestSerializer)
    def post(self, request):
        return self.success(request.value)
    """

    def validate(func):
        @functools.wraps(func)
        def handle(*args, **kwargs):
            request = args[1]
            s = serializer(data=request.data)
            if s.is_valid():
                request.value = s.data
                request.serializer = s
                return func(*args, **kwargs)
            else:
                return serializer_error(s)

        return handle

    return validate
