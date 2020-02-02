# apis/urls.py
from django.urls import path

from .views import SignupView, LoginView

urlpatterns = [
    path('signup', SignupView.as_view()),
    path('login', LoginView.as_view()),
    # path('<int:pk>/', DetailTodo.as_view()),
]
