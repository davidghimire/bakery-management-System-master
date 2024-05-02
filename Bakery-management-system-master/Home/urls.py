from django.urls import include, path
from . import views
from accounts.views import login_view,register_view,logout_view
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("",views.home,name="index"),
    path("about/",views.about,name="about"),
    path("contact/",views.contact,name="contact"),
    path("shop/",views.shop,name="shop"),
    path('shop/<str:category>/', views.product_list, name='product_list'),
    path("shop/<int:product_id>",views.product_detail,name="product"),
    path("account/",views.account,name="acccount"),
    path("cart/",views.cart ,name="cart"),

    path("billing/",views.billingDetails,name="billing"),
    path("ordersummary/",views.orderSummary,name="ordersummary"),
    path("update_item/",views.updateItem,name="updateitem"),

    path("payment/",views.payment,name="payment"),
    path('payment/success/', views.payment_success, name='payment_success'),

    path('khalti-request',views.khalti_payment,name="khalti"),

    path('generate_bill/<int:order_id>/', views.generate_bill, name='generateBill'),
    
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),

    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='password_reset_form.html',
        success_url='/password_reset/done/'
    ), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'
    ), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html',
        success_url='/reset/done/'
    ), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='password_reset_complete.html'
    ), name='password_reset_complete'),

]