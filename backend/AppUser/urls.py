from django.urls import path
from AppUser import views

app_name = 'article'

urlpatterns = [
    path('', views.appuser_list, name='list'),
    path('register/', views.RegisterAppUser, name='registeruser')
]
