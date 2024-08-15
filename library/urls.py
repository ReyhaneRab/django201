from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='books'),
    path('books/<int:pk>', views.book_detail, name='book_detail'),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:pk>', views.edit_book, name='edit_book'),
]