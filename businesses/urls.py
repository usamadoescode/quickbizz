from django.contrib import admin
from django.urls import path
from django.views import *
from quickbizz import settings, views
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('business_index/', views.business_index,name='business_index'),
    path('business_signup/', views.business_register, name='business_register'),
    path('business_signin/',views.business_login,name='business_login'),
    path('business_dashboard/', views.business_dashboard,name='business_dashboard'),
    path('logout/', views.business_logout, name='business_logout'),
    path('profile/<str:username>/', views.business_profile_view, name='business_profile_view'),
    path('add_product/',views.add_product, name='add_product'),
    path('products_list/',views.products_list, name='products_list'),
    path('<str:username>/products/', views.view_business_products, name='view_business_products'),
]