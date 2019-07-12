from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'search',views.search_titles,name='search_titles'),
    path('movie/<int:num>/',views.result,name='result'),
]