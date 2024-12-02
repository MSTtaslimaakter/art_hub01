# accounts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registration_view, name='registration_view'),
    path('login/', views.login_view, name='login'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('artist_dashboard/', views.artist_dashboard, name='artist_dashboard'),
    path('consumer_dashboard/', views.consumer_dashboard, name='consumer_dashboard'),
]
