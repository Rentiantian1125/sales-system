"""sales_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from sales import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sign_in/', views.sign_in),
    path('add_user/', views.add_user),
    path('get_user_list/', views.get_user_list),
    path('get_purchase_list/', views.get_purchase_list),
    path('add_purchase/', views.add_purchase),
    path('update_purchase/', views.update_purchase),
    path('get_sell_list/', views.get_sell_list),
    path('add_sell/', views.add_sell),
    path('update_sell/', views.update_sell),
    path('get_reserve/', views.get_reserve),
    path('get_goods_list/', views.get_goods_list),
    path('change_goods_price/', views.change_goods_price),
    path('put_in_reserve/', views.put_in_reserve),
    path('out_reserve/', views.out_reserve),
]
