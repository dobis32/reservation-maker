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
    path('django/admin', admin.site.urls),
    path('reservations', views.Reservations.as_view(), name='reservations'),
    path('reservations/confirm/success', views.reservation_confirm_success, name='reservation_confirm_success'),
    path('reservations/missing', views.resource_404, name='resource_404'),
    path('reservations/confirm', views.reservation_confirm.as_view(), name='reservation_confirm'),
    path('reservations/scheduled', views.reservation_scheduled, name='reservation_scheduled'),
    path('clients/verify', views.client_verify.as_view(), name='client_verify'),
    path('admin/', views.redirect_to_admin_login, name='redirect_to_admin_login'),
    path('admin/login', views.admin_login.as_view(), name='admin_login'),
    path('admin/dashboard', views.admin_dashboard.as_view(), name='admin_dashboard'),
    path('admin/validate', views.verify_admin, name='verify_admin'),
    path('admin/reservations', views.admin_reservations.as_view(), name="admin_reservations"),
    path('admin/reservations/upcoming', views.admin_upcoming_reservations.as_view(), name='admin_upcoming_reservations'),
    path('admin/reservations/dismiss', views.dismiss_notification, name='dismiss_notification')
]
