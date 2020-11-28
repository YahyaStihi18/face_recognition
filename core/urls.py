from django.urls import path,include
from .views import *


urlpatterns = [
    path('', index, name= 'index'),
    path('ajax/', ajax, name= 'ajax'),
    path('scan/',scan,name='scan'),
    path('profile/', profile, name= 'profile'),
    path('details/', details, name= 'details'),

    path('clear_history/',clear_history,name='clear_history'),
    path('reset/',reset,name='reset'),


]
