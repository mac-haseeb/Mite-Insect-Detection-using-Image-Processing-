from django.urls import path
from . import views


my_app = 'user'
urlpatterns = [
    path('signup/', views.signup, name='signup'),  # URL for the signup page
    path('signup/success/', views.signup_success, name='signup_success'),
]
