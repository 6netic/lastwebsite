from django.urls import path
from . import views


app_name = "madishop"

urlpatterns = [
    path('', views.home, name="home"),
    path('all_prds', views.list_all_prds, name="list_all_prds"),
    path('display_cart/', views.display_cart, name="display_cart"),
    path('add_to_cart/', views.add_to_cart, name="add_to_cart"),
    path('remove_item/', views.remove_item, name="remove_item"),
    path('checkout/', views.checkout, name="checkout"),
    path('signup/', views.signup, name="signup"),
    path('connect/', views.connect, name="connect"),
    path('disconnect/', views.disconnect, name="disconnect"),
    path('<str:category>/', views.list_prds_in_category, name="list_prds_in_category"),
    path('detail/<str:category>/<int:article_id>/', views.prd_detail, name="prd_detail"),
    # path('test/', views.test, name="test"),
]
