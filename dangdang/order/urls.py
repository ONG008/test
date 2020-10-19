from django.urls import path
from order import views

app_name = 'order'

urlpatterns = [
    path('indent/', views.indent, name='indent'),
    path('address/', views.address, name='address'),
    path('indent_ok/', views.indent_ok, name='indent_ok'),
]