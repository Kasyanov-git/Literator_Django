from django.urls import path
from . import views

urlpatterns = [
    path('', views.try_home, name='try_home'),
    path('try_1', views.try_1, name='try_1'),
    path('try_2', views.try_2, name='try_2'),
    path('try_3', views.try_3, name='try_3'),
    path('genre', views.genre, name='genre'),
    path('results', views.results, name='results'),
    path('buttonClick', views.buttonClick),
    path('get_query_book_1', views.get_query_book_1),
    path('get_query_book_2', views.get_query_book_2),
    path('get_query_book_3', views.get_query_book_3),
]