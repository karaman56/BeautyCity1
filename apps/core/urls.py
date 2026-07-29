from django.urls import path
from apps.core import views

# Если у тебя задан app_name:
# app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('service/', views.service, name='service'),
    path('service-finally/', views.service_finally, name='service_finally'),
    path('notes/', views.notes, name='notes'),
    path('dashboard/', views.admin_panel, name='admin'),
]