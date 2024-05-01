from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('auth/', include('authentication.urls')),
]
