from django.urls import path
from . import views

urlpatterns = [
    path('', views.visitor_checkin, name='checkin'),
]