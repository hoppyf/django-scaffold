from django.urls import path

from product.views import BookListView, BookView

urlpatterns = [
    path('book/', BookListView.as_view()),
    path('book/<int:pk>/', BookView.as_view()),
]
