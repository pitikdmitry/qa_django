from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.index, name='index'),
    path('signup/', views.index, name='index'),
    path('question/(?P<id>[^/]+)/', views.index, name='index'),
    path('ask/', views.index, name='index'),
    path('popular/', views.index, name='index'),
    path('new/', views.index, name='index'),
    path('', views.index, name='index'),
]
