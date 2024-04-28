# authentication/urls.py

from django.urls import path
from .views import login_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    # Add URLs for registration and password reset if needed
]
