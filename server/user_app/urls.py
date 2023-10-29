from django.urls import path, re_path
from user_app import views

urlpatterns = [
    re_path('login/', views.LoginView.as_view()),
]