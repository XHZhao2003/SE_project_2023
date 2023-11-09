from django.urls import path
from . import views

urlpatterns = [
    path('', views.toLoginView, name='toLoginView'),
    path('index/', views.loginView, name='loginView'),
    path('toregister/', views.toRegisterView, name='toRegisterView'),
    path('register/', views.registerView, name='registerView'),
]
