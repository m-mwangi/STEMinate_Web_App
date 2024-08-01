from django.urls import path
from .views import forum_list, topic_list

urlpatterns = [
    path('forums/', forum_list, name='forum_list'),
    path('forums/<int:forum_id>/', topic_list, name='topic_list'),
]
