from django.urls import path

from . import views

urlpatterns = [
    path('scanner/', views.scanner, name='scanner'),
    path('scanner/login/', views.login_view, name='login'),
	path('', views.index, name='bio'),
]
