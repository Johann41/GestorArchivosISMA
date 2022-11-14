from django.urls import path
from . import views


urlpatterns = [
    path('', views.login_view, name='auth_login'),
    path('logout/', views.logout_view, name="auth_logout"),
    path('signup/', views.signup_view, name='auth_signup'),
    path('password/', views.password_view, name='auth_password'),
]
