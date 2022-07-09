from django.urls import path
from .views import BookList,detail_page

urlpatterns = [
    path('', BookList.as_view(), name='home'),
    path('<int:pk>/', detail_page, name= 'detail_page'),

]
