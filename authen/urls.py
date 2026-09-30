from django.urls import path
from . import views
from .views import SignupAPI, SigninAPI

urlpatterns = [
    path('signin/', SigninAPI.as_view(), name='signin_api'),
    path('signup/', SignupAPI.as_view(), name='signup_api'),

    path('profile/', views.profile, name='profile'),
    path('signout/', views.signout, name='signout'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('update_password/', views.update_password, name='update_password'),
]