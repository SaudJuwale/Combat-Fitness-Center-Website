from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('achievements',views.achievements,name='achievements'),
    path('admission',views.admission,name='admission'),
    path('auth',views.auth,name="auth"),
    path('signup',views.signup,name="signup"),
    path('signin',views.signin,name="signin"),
    path('logout',views.logout,name="logout"),
]

