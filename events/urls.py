from django.urls import path
from . import view

urlpatterns = [
    path('',view.index, name='agenda-events-index')

]