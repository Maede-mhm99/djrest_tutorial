from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from store import views


product_router = routers.SimpleRouter() # instantiate a router 
product_router.register('products', views.CollectionViewSet, basename="product") # register parent resource and map it to it's viewset

# instantiating a nested router given three arguments:
# 1- parent router instancr
# 2- parent prefix
# 3- lookup -> prefix for domain_pk
review_router = routers.NestedSimpleRouter(product_router, parent_prefix='products', lookup='products')
# registering child resource into nested router
review_router.register(prefix='review', viewset=views.ReviewViewSet, basename='product-review')


urlpatterns = [
    path("", include(product_router.urls)),
    path("", include(review_router.urls))
]


# end points
# create a cart: cart/
# delete a cart: cart/{cart_pk} 
# list a cart items and adding a new item: cart/{cart_pk}/items/
# deleting an item and updating quantity of an item : cart/{cart_pk}/items/{item_pk}/ 