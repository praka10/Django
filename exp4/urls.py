from django.urls import path
from . import views

urlpatterns = [
    path('sendMail/', views.send_email, name='sendMail'),
]

