from django.urls import path
from .views import *

producturls = [
    path("addproduct", addProduct, name="addProduct"),
    path("signup", signup, name="signup"),
    path("signin", signin, name="signin"),
    path("logout", logoutUser, name="logout"),
    path("products", productList, name="products"),
    path("editproduct/<int:id>", editProduct, name="editProduct"),
    path("deleteproduct/<int:id>", deleteProduct, name="deleteProduct"),
    path("product/<int:id>", productDetail, name="productDetail"),
    path("addtocart/<int:id>", addToCart, name="addtocart"),
    path("cart", cart, name="cart"),
    path("removefromcart/<int:id>", removeFromCart, name="removefromcart"),
    path("increasequantity/<int:id>", increaseQuantity, name="increasequantity"),
    path("decreasequantity/<int:id>", decreaseQuantity, name="decreasequantity"),
    path("checkout", checkout, name="checkout"),
    path("ordersuccess", orderSuccess, name="ordersuccess"),
    path("orders", orders, name="orders"),
    path("updateorderstatus/<int:order_id>", updateOrderStatus, name="updateOrderStatus"),
    path("location", location, name="location"),
]
