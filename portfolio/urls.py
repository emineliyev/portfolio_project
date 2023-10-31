from django.urls import path
from .views import ServiceView

app_name = 'portfolio'
urlpatterns = [
    path('', ServiceView.as_view(), name='index'),
]