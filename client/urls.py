from django.urls import path
from client import views

urlpatterns = [
    path('api/sendmail/', views.PostEmail.as_view()),
]
