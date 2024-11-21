# users/views.py
from django.urls import path
from .controllers import getAllCodes, insertEntryAndExit

urlpatterns = [
    path('getallcodes/', getAllCodes, name='getAllCodes'),
    path('insertentryandexit/', insertEntryAndExit, name='insertEntryAndExit'),
]
