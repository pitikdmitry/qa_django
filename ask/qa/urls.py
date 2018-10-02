from django.urls import path

from . import views

app_name = 'qa'
urlpatterns = [
    path('login/', views.index, name='login'),
    path('signup/', views.index, name='signup'),
    path('question/<int:question_id>/', views.get_question_by_id, name='get_question_by_id'),
    path('ask/', views.index, name='ask'),
    path('popular/', views.popular_questions, name='popular'),
    path('new/', views.index, name='new'),
    path('', views.latest_questions, name='index'),
]
