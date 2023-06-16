from django.urls import path
from . import views


urlpatterns=[
    path('',views.login_form,name='login'),
    path('signup/',views.signup,name='signup'),
    path('dashboard/',views.dashbaord,name='dashboard'),
    path('logout',views.user_logout, name='logout'),
]