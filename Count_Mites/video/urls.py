from django.urls import path
from . import views


my_app = 'video'
urlpatterns = [
    path('video/', views.upload_video, name='upload_video'),
    path('videos/', views.user_uploaded_videos, name='user_uploaded_videos'),
]


