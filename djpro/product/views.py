from rest_framework.views import APIView

from common.views import success_response, serializer_error_reason, serializer_error
from product.models import Book
from product.serializers import BookSerializer, BookUpdateSerializer


class BookListView(APIView):
    def get(self, request):
        queryset = Book.filter()
        serializer = BookSerializer(queryset, many=True)
        return success_response({'list': serializer.data})

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return success_response()
        else:
            return serializer_error(serializer)


class BookView(APIView):
    def get(self, request, pk):
        book_obj = Book.get(pk=pk)
        serializer = BookSerializer(book_obj)
        return success_response(serializer.data)

    def put(self, request, pk):
        book_obj = Book.get(pk=pk)
        serializer = BookUpdateSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            for k, v in data.items():
                if hasattr(book_obj, k):
                    setattr(book_obj, k, v)
            book_obj.save()
            return success_response()
        else:
            print(serializer_error_reason(serializer))
            return serializer_error(serializer)

    def delete(self, request, pk):
        book_obj = Book.get(pk=pk)
        book_obj.del_flag = True
        book_obj.save()
        return success_response()
