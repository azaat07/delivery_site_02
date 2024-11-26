from .views import *
from rest_framework import routers
from django.urls import path, include


router = routers.SimpleRouter()
router.register(r'user', UserProfileViewSet, basename='user_list')
router.register(r'product', ProductViewSet, basename='product_list')
router.register(r'combo', ProductComboViewSet, basename='combo_list')
router.register(r'store_review', StoreReviewViewSet, basename='store_review_list')
router.register(r'courier_review', CourierReviewViewSet, basename='courier_review_list')
router.register(r'cart', CartViewSet, basename='cart_list')
router.register(r'cart_item', CarItemViewSet, basename='cart_item_list')
router.register(r'order', OrderViewSet, basename='order_list')
router.register(r'courier', CourierViewSet, basename='courier_list')


urlpatterns = [
    path('', include(router.urls)),
    path('store/', StoreListApiView.as_view(), name='store_list'),
    path('store/<int:pk>/', StoreDetailApiView.as_view(), name='store_detail'),
]