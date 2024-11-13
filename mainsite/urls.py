from django.urls import path
from . import views


app_name = 'mainsite'

urlpatterns = [
    path('', views.home, name="home"),
    path('realisations/', views.realisations, name="realisations"),
    path('services/', views.services, name="services"),
    path('cv/', views.show_cv_in_pdf, name="show_cv_in_pdf"),
    # path('contact/', views.contact, name="contact"),
]
