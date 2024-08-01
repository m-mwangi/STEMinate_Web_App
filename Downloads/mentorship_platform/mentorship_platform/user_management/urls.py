from django.urls import path
from .views import register, update_profile

urlpatterns = [
    path('register/', register, name='register'),
    path('profile/update/', update_profile, name='update_profile'),
]
