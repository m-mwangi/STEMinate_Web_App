# profiles/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('update_profile/', views.update_profile, name='update_profile'),
    path('profile/', views.profile, name='profile'),
    # other URL patterns...
]
