from django.urls import path
from ShopApp import views

urlpatterns = [

    path('index_page/',views.index_page,name="index_page"),
    path('cat_add/',views.cat_add,name="cat_add"),
    path('catdata/',views.catdata,name="catdata"),
    path('cat_display/',views.cat_display,name="cat_display"),
    path('cat_edit/<int:dataid>/',views.cat_edit,name="cat_edit"),
    path('update_cat/<int:dataid>/',views.update_cat,name="update_cat"),
    path('delete_cat/<int:dataid>/',views.delete_cat,name="delete_cat"),


    path('product_add/',views.product_add,name="product_add"),
    path('productdata/',views.productdata,name="productdata"),
    path('product_display/',views.product_display,name="product_display"),
    path('product_edit/<int:dataid>/',views.product_edit,name="product_edit"),
    path('product_update/<int:dataid>/',views.product_update,name="product_update"),
    path('product_delete/<int:dataid>/',views.product_delete,name="product_delete"),

    path('admin_user/',views.admin_user,name="admin_user"),
    path('adminuser/',views.adminuser,name="adminuser"),
    path('admin_logout/',views.admin_logout,name="admin_logout"),

    path('contact_suggestion/',views.contact_suggestion,name="contact_suggestion"),
    path('bookingsss/',views.bookingsss,name="bookingsss"),
    path('contact_suggestion_delete/<int:del_id>/',views.contact_suggestion_delete,name="contact_suggestion_delete"),
]