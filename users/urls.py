from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('', views.home,name="home"),
    path('register/', views.register,name="register"),
    path('profile/', views.profile,name="profile"),
    path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    
    # forget password mechanism
    path('reset_password/', auth_view.PasswordResetView.as_view(template_name='users/password_reset.html'), name="reset_password"),
    path('reset_password_sent/', auth_view.PasswordResetDoneView.as_view(template_name='users/password_reset_sent.html'), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirmation.html'), name="password_reset_confirm"),
    path('reset_password_complete/', auth_view.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name="password_reset_complete"),
]
