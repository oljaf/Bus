from django.urls import path
from .views import *
urlpatterns=[
    path('',Home,name='home'),
    path('',allcar,name='allcar'),
    path('',create,name='create'),
]