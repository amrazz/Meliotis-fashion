from django.urls import path
from . import views


# Admin_app urls

urlpatterns = [
    path("shop_cart/", views.shop_cart, name="shop_cart"),
    path("add_to_cart/<int:pro_id>/", views.add_to_cart, name="add_to_cart"),
    path(
        "delete_cart_items/<int:pro_id>/",
        views.delete_cart_items,
        name="delete_cart_items",
    ),
    path("check_stock/", views.check_stock, name="check_stock"),
    path("update_total_price/", views.update_total_price, name="update_total_price"),
    path("checkout/", views.checkout, name="checkout"),
    path("place_order/", views.place_order, name="place_order"),
    path("payment/success/", views.payment_success, name="payment_success"),
    path("order_detail/", views.order_detail, name="order_detail"),
    path("view_order/<int:ord_id>/", views.view_order, name="view_order"),
    path("view_status/<int:order_id>/", views.view_status, name="view_status"),
    path("wishlist_view/", views.wishlist_view, name="wishlist_view"),
    path("wishlist_add/<int:pro_id>/", views.wishlist_add, name="wishlist_add"),
    path("wishlist_del/<int:pro_id>/", views.wishlist_del, name="wishlist_del"),
    path(
        "request_cancel_order/<int:order_id>/",
        views.request_cancel_order,
        name="request_cancel_order",
    ),
    path(
        "request_return_product/<int:order_id>/",
        views.request_return_product,
        name="request_return_product",
    ),
    path("view_all_order/", views.view_all_order, name="view_all_order"),
    path("payment_failure/", views.payment_failure, name="payment_failure"),
    path("add_address_checkout/", views.add_address_checkout, name="add_address_"),
    path("retry-payment/", views.retry_payment, name="retry_payment"),
]
