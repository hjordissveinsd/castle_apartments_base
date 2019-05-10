from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
    path('', views.profile, name="profile"),
    path('messages', views.messages, name="messages"),
    path('settings', views.settings, name="settings"),
    path('log-in', views.createOrLogIn, name="createOrLogIn"),
    path('createOrLogIn', views.createOrLogIn, name="createOrLogIn"),
    path('loggedIn', LoginView.as_view(template_name='Profile/loggedIn.html'), name='Login'),
    #path('loggedIn', views.loggedIn, name="loggedIn"),
    path('notLoggedIn', views.notLoggedIn, name="notLoggedIn"),
    ##############raggi##############################
    path('register', views.register, name="register"),
    path('login/', LoginView.as_view(template_name='Profile/login.html'), name='login'),
    #path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile')
]
