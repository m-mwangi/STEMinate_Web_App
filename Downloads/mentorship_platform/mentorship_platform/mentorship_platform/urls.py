from django.contrib import admin
from django.urls import path, include
from user_management import views  # Import views from the user_management app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('users/', include('user_management.urls')),
    path('profiles/', include('profiles.urls')),
    path('accounts/', include('account.urls')),
    path('send/', include('communication.urls')),  # Include communication URLs
    path('find_match/', include('matching.urls')),  # Include matching URLs
    path('resources/', include('resources.urls')),
]
