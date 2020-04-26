from django.urls import path,include
from .views import *
from knox import views as knox_views
urlpatterns = [
    path('auth',include('knox.urls')),
    path('auth/register',RegisterAPI.as_view()),
    path('auth/login',LoginAPI.as_view(),name = "login"),
    path('auth/home',UserAPI.as_view(),name="home"),
    path('auth/logout',knox_views.LogoutView.as_view(), name="knox_logout")
]
