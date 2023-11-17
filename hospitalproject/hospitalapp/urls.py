from django.urls import path
from hospitalapp import views

urlpatterns = [
    path('', views.demo,name='demo'),
    path('register/', views.register,name='register'),
    path('login', views.login,name='login'),
    path('logout', views.logout,name='logout'),
    path('about/', views.about,name='about'),
    path('contact/', views.contact,name='contact'),
    path('department/', views.department,name='department'),
    path('doctor/', views.doctor,name='doctor'),
    path('medicine/', views.medicine,name='medicine'),
    path('booking/', views.booking,name='booking'),
]   
