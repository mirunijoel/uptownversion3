from django.urls import path

from . import views

urlpatterns = [
    # Leave as empty string for base url
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('product/<int:pk>/', views.product_view, name="product"),
    path('checkout/', views.checkout, name="checkout"),
    path('checkout-review/', views.checkout_review, name="checkout_review"),
    path('update_item/', views.updateItem, name="update_item"),

]
