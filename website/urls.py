from . import views

"""
URL configuration for stock_ms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include

app_name = "website"

urlpatterns = [
    path('', views.home, name='home'),
    path('products', views.productsView, name='products'),
    path('products/<str:title>', views.singleProductView, name='single-product'),
    path('about-us', views.about, name='about-us'),
    path('admin/', admin.site.urls),
     path("__reload__/", include("django_browser_reload.urls")),
    # auth urls
    path('auth/login', views.login_view, name='login'),
    path('auth/logout', views.logout_view, name='logout'),
    path('auth/register', views.register_view, name='register'),

    # dashboard
    path('dashboard', views.dashboard, name='dashboard'),
    path('dashboard/account', views.user_account, name='user_account'),
    path('dashboard/settings', views.user_setting, name='user_setting'),
    path('dashboard/orders', views.user_orders, name='user_orders'),

    # manage products
    path('dashboard/products', views.products_dashboard_view, name='products_dashboard'),
    path('dashboard/products/add-product', views.add_product_view, name='add_product'),

]
