"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('reservations', views.Reservations.as_view(), name='reservations'),
    path('reservations/confirm/success', views.reservation_confirm_success, name='reservation_confirm_success'),
    path('reservations/missing', views.resource_404, name='resource_404'),
    path('reservations/confirm', views.reservation_confirm, name='reservation_confirm'),
    path('reservations/scheduled', views.reservation_scheduled, name='reservation_scheduled'),
    path('clients/verify', views.client_verify.as_view(), name='client_verify'),
    path('manage/', views.admin_login.as_view(), name='admin_login'),
    path('manage/login', views.admin_login.as_view(), name='admin_login'),
]
