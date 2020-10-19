from django.urls import path
from user import views

app_name = 'user'
urlpatterns = [
    path('login/',  views.login, name='login'),
    path('login_logic/',  views.login_logic, name='login_logic'),
    path('logout/',  views.logout, name='logout'),
    path('register/',  views.register, name='register'),
    path('register_logic/',  views.register_logic, name='register_logic'),
    path('getcaptcha/', views.getcaptcha, name='getcaptcha'),
    path('checkcaptcha/', views.checkcaptcha, name='checkcaptcha'),
    path('registerok/', views.registerok, name='registerok'),
    path('checkusername/', views.checkusername, name='checkusername'),
    path('checkregister/', views.checkregister, name='checkregister'),
]
