#created this file manually
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name=''),
    path('homepage',views.homepage,name='homepage'),
    path('register',views.register,name='register'),
    path('my_login',views.my_login,name='my_login'),
    path('user_logout',views.user_logout,name='user_logout'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    # path('profile/<username>', views.profile, name='profile'),

]