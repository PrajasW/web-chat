from . import views
from django.urls import path

urlpatterns = [
    path('',views.home),
    path('add',views.addMessage),
]