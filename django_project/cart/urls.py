from django.urls import path
from . import views

urlpatterns = [
    path("", views.cart_index, name="cart_index"),
    path("add/<int:pk>/", views.add_to_cart, name="add_to_cart"),
    path("delete/<int:pk>/", views.delete_cart, name="delete_cart"),
    path("delete_one/<int:pk>/", views.delete_one_from_cart, name="delete_one_from_cart"),
]