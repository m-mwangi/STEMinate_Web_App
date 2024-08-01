from django.urls import path
from . import views  # Import views from the communication app

urlpatterns = [
    path('', views.send_message, name='send_message'),  # Route /send/ to the send_message view
    path('inbox/', views.inbox, name='inbox'),  # Route /send/inbox/ to the inbox view
]
