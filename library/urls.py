from django.urls import path
from library import views

urlpatterns = [
    path('books/', views.book_list, name='books'),
    path('books/<int:pk>', views.book_detail, name='book_detail'),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:pk>', views.edit_book, name='edit_book'),
    path('book/delete/<int:pk>', views.confirm_delete, name='book_delete_confirm'),
    path('book/delete/confirm/<int:pk>', views.delete_book, name="book_delete")
]
