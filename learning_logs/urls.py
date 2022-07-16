from django.urls import path
from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Home Page
    path('', views.index, name='index'),

    # Topics
    path('topics/', views.topics, name='topics'),

    #Details Topics
    path('topics/<topic_id>/', views.topic, name='topic'),
]
