from django.urls import path
from .views import BookList, detail_page, favorite_book, favorite_list, search_bar,like_view

urlpatterns = [
    path('', BookList.as_view(), name='home'),
    path('<int:pk>/', detail_page, name='detail_page'),
    path('<int:pk>/favorite/', favorite_book, name='favorite_book'),
    path('list/favorite/', favorite_list, name='favorite_list'),
    path('serch/', search_bar, name='search'),
    path('<int:pk>/likes/', like_view, name='like_book'),

]
