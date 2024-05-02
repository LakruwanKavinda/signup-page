from django.urls import path
from .views import UserSignupView, UserLoginView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', include('users.urls'),
                basename='user')  # Add 'basename='user''

urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
]
