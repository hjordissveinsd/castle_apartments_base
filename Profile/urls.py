from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
    path('', views.profile, name="profile"),
    path('settings', views.settings, name="settings"),
    path('log-in', views.create_or_log_in, name="createOrLogIn"),
    path('createOrLogIn', views.create_or_log_in, name="createOrLogIn"),
    path('loggedIn', LoginView.as_view(template_name='Profile/loggedIn.html'), name='Login'),
    path('notLoggedIn', views.not_logged_in, name="notLoggedIn"),
    path('register', views.register, name="register"),
    path('login/', LoginView.as_view(template_name='Profile/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('browsingHistory/', views.browsing_history, name="browsingHistory"),
    path('searchHistory/', views.search_history, name="searchHistory")
]