from django.urls import path
from . import views

urlpatterns = [
  path('', views.enroll, name='enroll'),
  path('adminpage/', views.adminpage, name='adminpage'),
  path('adminpage/adminlogin/', views.adminlogin, name='adminlogin'),
  path('index/', views.index, name='index'),
  path('add/', views.add, name='add'),
  path('add/addrecord/', views.addrecord, name='addrecord'),
  path('delete/<int:id>', views.delete, name='delete'),
  path('index/update/<int:id>', views.update, name='update'),
  path('index/update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
]




