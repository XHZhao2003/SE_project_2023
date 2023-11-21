from django.urls import path
from AppUser import views

app_name = 'Appuser'

urlpatterns = [
    path('', views.AppUserView.as_view()),
]
