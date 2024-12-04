from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import *
from .models import *
from .permission import CheckCreateStore, CheckEditStore, CheckOwner


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers



class StoreListApiView(generics.ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreListSerializers



class StoreDetailApiView(generics.RetrieveAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreDetailSerializers
    permission_classes = [CheckOwner]

    def perform_create(self, serializer):
        return serializer.save(owner=object.request.user)




class StoreCreateApiView(generics.CreateAPIView):
    serializer_class = StoreSerializers
    permission_classes = [CheckCreateStore]


class StoreUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializers
    permission_classes = [CheckCreateStore, CheckEditStore]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class ProductCreateApiView(generics.CreateAPIView):
    serializer_class = ProductSerializers
    permission_classes = [CheckCreateStore]



class ProductComboViewSet(viewsets.ModelViewSet):
    queryset = ProductCombo.objects.all()
    serializer_class = ProductComboSerializers



class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializers



class CarItemViewSet(viewsets.ModelViewSet):
    queryset = CarItem.objects.all()
    serializer_class = CarItemSerializers



class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers



class CourierViewSet(viewsets.ModelViewSet):
    queryset = Courier.objects.all()
    serializer_class = CourierSerializers



class CourierReviewViewSet(viewsets.ModelViewSet):
    queryset = CourierReview.objects.all()
    serializer_class = CourierReviewSerializers



class StoreReviewViewSet(viewsets.ModelViewSet):
    queryset = StoreReview.objects.all()
    serializer_class = StoreReviewSerializers
