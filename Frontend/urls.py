from django.urls import path
from Frontend import views

urlpatterns = [
    path('shop_index/',views.shop_index,name="shop_index"),
    path('product_page/',views.product_page,name="product_page"),
    path('product_filter/<cat_name>/',views.product_filter,name="product_filter"),
    path('single_product/<int:pro_id>/',views.single_product,name="single_product"),
    path('about_us',views.about_us,name="about_us"),
    path('contact_us/',views.contact_us,name="contact_us"),
    path('contactdata/',views.contactdata,name="contactdata"),

    path('signup_user/',views.signup_user,name="signup_user"),
    path('signupdata/',views.signupdata,name="signupdata"),
    path('login_user/',views.login_user,name="login_user"),
    path('Userlogin/',views.Userlogin,name="Userlogin"),
    path('Userlogout/',views.Userlogout,name="Userlogout"),

    path('cartdata/',views.cartdata,name="cartdata"),
    path('cart_page/',views.cart_page,name="cart_page"),
    path('checkout_page/',views.checkout_page,name="checkout_page"),
    path('bookingdata/',views.bookingdata,name="bookingdata"),
    path('payment_product/',views.payment_product,name="payment_product"),

    path('delete_cart/<int:pro_id>/',views.delete_cart,name="delete_cart"),
]