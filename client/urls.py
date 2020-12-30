from django.urls import path
from client import views

urlpatterns = [
    path('sendmail/', views.PostEmail.as_view()),
]
