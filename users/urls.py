# users/views.py
from django.urls import path
from .controllers import getUsersByAdmin, register, login, verify

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('verify/', verify, name='verify'),
    path('getUsersByAdmin/', getUsersByAdmin, name='getUsersByAdmin')
]
