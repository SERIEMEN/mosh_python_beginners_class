"""
URL configuration for PyShop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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

from .asgi import application

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls') )
]
# this arguments any urls that starts with admin connect it to the respective urls
# same any urls that start with products direct it to the specific url(reference it)
# plus use the include function from django.urls import include as well to include the products application
