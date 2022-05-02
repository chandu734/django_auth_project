from django.urls import path
from authapp import views

urlpatterns = [
    path('',views.indexView,name='home'),
    path('/about',views.aboutView,name='about'),
    path('/login',views.loginView,name='login'),
]