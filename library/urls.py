from django.urls import path
from . import views

app_name = "library"

urlpatterns = [
   # path('',views.authors_list, name="list"),
    path('authors/',views.authors_list, name="list"),
    path('edit-author/<author_id>',views.edit_author,name="edit"),
    path('add-author/',views.add_author,name="add"),
    path('delete-author/<author_id>',views.delete_author,name="delete"),
    path('books/<author_id>',views.book_list,name="books"),
    path('add-book/<author_id>',views.add_book,name="add-book"),
    path('edit-book/<book_id>',views.edit_book,name="edit-book"),
    path('delete-book/<book_id>',views.delete_book,name="delete-book"),
]
