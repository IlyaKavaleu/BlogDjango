from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    path('', include('django.contrib.auth.urls'), name='login'),
    path('logout/', views.logout, name='logged_out'),
    path('register/', views.register, name='register'),
]
