from django.urls import path
from . import views


my_app = 'home'
urlpatterns = [
    path('', views.home_page, name='home_page'),
]
