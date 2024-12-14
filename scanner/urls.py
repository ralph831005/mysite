from django.urls import path

from . import views

urlpatterns = [
    path('', views.scanner, name='scanner'),
    path('login/', views.login_view, name='login'),
]
