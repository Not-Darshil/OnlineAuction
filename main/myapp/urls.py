#created this file manually
from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('',views.home,name=''),
    path('homepage',views.homepage,name='homepage'),
    path('pricing',views.pricing,name='pricing'),
    path('about',views.about,name='about'),
    path('register',views.register,name='register'),
    path('my_login',views.my_login,name='my_login'),
    path('logout',views.logout,name='logout'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('create',views.create,name='create'),
    # path('profile/<username>', views.profile, name='profile'),

]