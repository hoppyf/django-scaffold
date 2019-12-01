from rest_framework.serializers import ModelSerializer


class MySerializer(ModelSerializer):
    """
    用于处理ModelSerializer需要重复写基类字段的麻烦
    author: timest
    """

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
