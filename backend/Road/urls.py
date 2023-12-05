from django.urls import path
from Road import views

app_name = 'Road'

urlpatterns = [
    path('', views.RoadView.as_view()),
]
