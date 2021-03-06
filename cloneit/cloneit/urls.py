"""cloneit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from cloneapp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.signupuser,name='signupuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('home/',views.home, name='home'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('laptop/', views.laptop, name='laptop'),
    path('speaker/', views.speaker, name='speaker'),
    path('mobile/', views.mobile, name='mobile'),
    path('keyboard/', views.keyboard, name='keyboard'),
    path('detail/<int:product_id>', views.detail, name='detail'),
    path('cart/',views.add_to_cart,name='cart'),
    path('cart_increment/',views.cart_increment,name='cart_increment'),
    path('cart_decrement/',views.cart_decrement,name='cart_decrement'),
    path('cart_delete/',views.cart_delete,name='cart_delete'),
    path('profile/',views.profileview,name='profileview'),
    path('profiledit/',views.profiledit,name='profiledit'),
    path('gameview/',views.gameview,name='gameview'),
]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
