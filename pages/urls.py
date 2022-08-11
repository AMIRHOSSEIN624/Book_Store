from django.urls import path
from .views import BookList, detail_page, favorite_book, favorite_list, search_bar, like_view, CreateBook, UpdateBook, \
    DeleteBook, category_filter,filter_by

urlpatterns = [
    path('', BookList.as_view(), name='home'),
    path('<int:pk>/', detail_page, name='detail_page'),
    path('<int:pk>/favorite/', favorite_book, name='favorite_book'),
    path('list/favorite/', favorite_list, name='favorite_list'),
    path('serch/', search_bar, name='search'),
    path('<int:pk>/likes/', like_view, name='like_book'),
    path('add/book/', CreateBook.as_view(), name='create_book'),
    path('<int:pk>/update/', UpdateBook.as_view(), name='update_book'),
    path('<int:pk>/delete/', DeleteBook.as_view(), name='delete'),
    path('filter/', filter_by , name='filter_list'),
    path('category/<str:cats>/', category_filter, name='category'),

]
