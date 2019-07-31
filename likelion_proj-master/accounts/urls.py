from django.urls import path
from . import views

urlpatterns = [
    path('login/signup/', views.signup, name = 'signup'),
    path('login/', views.login, name='login'),
]