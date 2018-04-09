from rest_framework.serializers import ModelSerializer
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    # call framework's default response
    response = exception_handler(exc, context)
    if response is not None:
        response.data['code'] = response.status_code
        response.data['msg'] = response.data['detail']
        response.data['data'] = ''
        del response.data['detail']

    return response


class MySerializer(ModelSerializer):
    # noinspection PyTypeChecker
    def __init__(self, *args, **kwargs):
        super(MySerializer, self).__init__(*args, **kwargs)
        fields = getattr(self.Meta, 'fields', None)
        exclude = getattr(self.Meta, 'exclude', None)
        read_only_fields = getattr(self.Meta, 'read_only_fields', ('id', 'created_at', 'updated_at'))
        read_only_fields = tuple(read_only_fields) + ('id', 'created_at', 'updated_at')
        setattr(self.Meta, 'read_only_fields', tuple(set(read_only_fields)))
        if fields is None and exclude is None:
            setattr(self.Meta, 'exclude', ('id', 'created_at', 'updated_at', 'del_flag'))
        elif exclude:
            e = tuple(exclude) + ('id', 'created_at', 'updated_at')
            setattr(self.Meta, 'exclude', tuple(set(e)))
