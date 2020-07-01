from django.urls import path

from . import views



app_name = 'note'

urlpatterns = [
    path('',views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('home/', views.home, name='home'),
    path('home/<int:topic_id>/delete/', views.delete, name='delete'),
    path('search/', views.search, name = 'search'),
    path('add_topic/', views.add_topic, name='add_topic'),
    path('topic/<int:topic_id>/add_note/', views.add_note, name='add_note'),
    path('topic_view/<int:topic_id>/', views.topic_view, name='topic_view'),
    path('update_note/<int:note_id>/', views.update_note, name='update_note'),
]