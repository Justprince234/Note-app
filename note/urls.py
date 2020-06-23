from django.urls import path

from . import views



app_name = 'note'

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name = 'search'),
    path('add_topic/', views.add_topic, name='add_topic'),
    path('delete/<int:topic_id>/', views.delete, name='delete'),
    path('topic/<int:topic_id>/add_note/', views.add_note, name='add_note'),
    path('topic_view/<int:topic_id>/', views.topic_view, name='topic_view'),
    path('update_note/<int:note_id>/', views.update_note, name='update_note'),
]