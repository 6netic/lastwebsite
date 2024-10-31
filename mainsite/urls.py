from django.urls import path
from . import views


app_name = 'mainsite'

urlpatterns = [
    path('', views.home, name="home"),
    path('realisations/', views.realisations, name="realisations"),
    path('services/', views.services, name="services"),
    # path('contact/', views.contact, name="contact"),
]
