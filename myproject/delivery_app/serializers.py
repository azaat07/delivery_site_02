from rest_framework import serializers
from .models import *


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileSimpleSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'username']


class UserProfileReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']



class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']





class ContactInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = ['contact_info']



class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_name', 'product_image', 'price', 'description']



class ProductComboSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductCombo
        fields = ['combo_name', 'combo_image', 'price', 'description']



class CartSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'



class CarItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = CarItem
        fields = '__all__'



class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'



class CourierSerializers(serializers.ModelSerializer):
    class Meta:
        model = Courier
        fields = '__all__'



class CourierReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = CourierReview
        fields = '__all__'



class StoreReviewSerializers(serializers.ModelSerializer):
    client = UserProfileReviewSerializers()
    created_date = serializers.DateTimeField(format=('%d-%m-%Y %H:%M'))
    class Meta:
        model = StoreReview
        fields = ['client', 'rating', 'comment', 'created_date']


class StoreListSerializers(serializers.ModelSerializer):
    category = CategorySerializers()
    avg_rating = serializers.SerializerMethodField()
    count_people = serializers.SerializerMethodField()
    count_good_grade = serializers.SerializerMethodField()

    class Meta:
        model = Store
        fields = ['id', 'store_name', 'store_image', 'category', 'avg_rating',
                  'count_people', 'count_good_grade']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_count_people(self, obj):
        return obj.get_count_people()

    def get_count_good_grade(self, obj):
        return obj.get_count_good_grade()

class StoreDetailSerializers(serializers.ModelSerializer):
    category = CategorySerializers()
    contacts = ContactInfoSerializers(many=True, read_only=True)
    owner = UserProfileSimpleSerializers()
    products = ProductSerializers(many=True, read_only=True)
    combos = ProductComboSerializers(many=True, read_only=True)
    store_review = StoreReviewSerializers(many=True, read_only=True)

    class Meta:
        model = Store
        fields = ['store_name', 'store_image', 'category', 'description', 'address', 'owner', 'contacts',
                    'products', 'combos', 'store_review']


class StoreSerializers(serializers.ModelSerializer):

    class Meta:
        model = Store
        fields = ['store_name', 'store_name', 'category', 'description', 'address', 'owner']