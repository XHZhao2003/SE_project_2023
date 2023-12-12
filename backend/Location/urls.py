from django.urls import path
from Location import views

app_name = 'Location'

urlpatterns = [
    path('', views.LocationView.as_view()),
]
