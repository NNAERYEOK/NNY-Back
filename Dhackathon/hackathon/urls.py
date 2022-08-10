"""hackathon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin
from django.urls import path
from nny.views import *

urlpatterns = [
    #path('admin/', admin.site.urls),
    path("create/", UserCreateAPIView.as_view(), name=""),
    path("login/", LoginAPIView.as_view(), name=""),
    path("logout/", LogoutAPIView.as_view(), name=""),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),
    path("profile" ,ProfileAPIview.as_view(),name="profile"),
    path("update_profile/", ProfileUpdateAPIview.as_view(), name="update_profile"),
    path('warning_list/', WarningListView.as_view(), name = 'auth_warning_list'),
    path('warning/',WarningView.as_view(), name = 'auth_warning'),
    path('usedeye_list/', UsedEyeListView.as_view(), name = 'auth_usedeye_list'),
    path('usedeye/',UsedEyeView.as_view(), name = 'auth_usedeye'),
    path('eye_list/', EyeListView.as_view(), name = 'auth_eye_list'),
    path('eye/',EyeView.as_view(), name = 'auth_eye'),
]
