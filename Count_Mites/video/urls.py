from django.urls import path
from . import views


my_app = 'video'
urlpatterns = [
    path('video/', views.upload_video, name='upload_video'),
]

