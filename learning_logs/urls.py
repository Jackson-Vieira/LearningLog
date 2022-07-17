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

    #Add a new Topic
    path('new_topic/', views.new_topic, name='new_topic'),

    #Add a new Entry
    path('new_entry/<topic_id>/', views.new_entry, name='new_entry'),

    #Edit a existent Entry
    path('edit_entry/<entry_id>/', views.edit_entry, name='edit_entry')
]
