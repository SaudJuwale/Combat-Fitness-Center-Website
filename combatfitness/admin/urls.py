from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('cfcadmin',views.admin,name='cfcadmin'),
    path('approval',views.approval,name='approval'),
    path('confirmlist',views.confirmlist,name='confirmlist'),
    path('waitinglist',views.waitinglist,name='waitinglist'),
    path('adminsignin',views.adminsignin,name='adminsignin'),
    path('adminlogout',views.adminlogout,name='adminlogout'),
]

