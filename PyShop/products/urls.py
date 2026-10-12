from django.urls import path

from . import views  # to import the views model from products to mapp the views and urls together

#connect the urls various url to their functions
#/products

urlpatterns = [
    path(' ', views.index, name='index'), #the empty string is used to identify the /mapp the current root app to the link
    path('new', views.new)
]

# if you create a path that is a new page, you use the views function to add a request
# then you map it in the url.py for django to access it, basically store it in it's own address,
# since you already created the /connected the products app to the django urls,
# there will not be need to start the process all over again because you told django that whenever a urls starts with products,
# just open it to its desired address/ mapped out address.
