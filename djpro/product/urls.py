from django.urls import path

from product.views import BookListView, BookView, TasksView

urlpatterns = [
    path('book/', BookListView.as_view()),
    path('book/<int:pk>/', BookView.as_view()),
    path('task/', TasksView.as_view()),
]
