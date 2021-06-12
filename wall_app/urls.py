from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('message', views.message),
    path('comment', views.comment),
    path('logout', views.logout),
    path('delete', views.delete),
]