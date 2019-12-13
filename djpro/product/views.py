from rest_framework.views import APIView

from common.api import R, validate
from product.models import Book
from product.serializers import BookSerializer, BookUpdateSerializer


class BookListView(APIView):
    def get(self, request):
        queryset = Book.filter()
        serializer = BookSerializer(queryset, many=True)
        return R.success({'list': serializer.data})

    @validate(BookSerializer)
    def post(self, request):
        book_obj = Book.objects.create(**request.value)
        return R.success(book_obj.dict())


class BookView(APIView):
    def get(self, request, pk):
        book_obj = Book.get(pk=pk)
        serializer = BookSerializer(book_obj)
        return R.success(serializer.data)

    def put(self, request, pk):
        book_obj = Book.get(pk=pk)
        serializer = BookUpdateSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            for k, v in data.items():
                if hasattr(book_obj, k):
                    setattr(book_obj, k, v)
            book_obj.save()
            return R.success()
        else:
            return R.warn(serializer.errors)

    def delete(self, request, pk):
        book_obj = Book.get(pk=pk)
        book_obj.del_flag = True
        book_obj.save()
        return R.success()
