from rest_framework import serializers
from .models import User, Product, Category, Review, Order, OrderItem


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


from django.db.models import Avg

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = "__all__"

    def get_average_rating(self, obj):
        return obj.reviews.aggregate(avg=Avg("rating"))["avg"]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

class OrderItemSerializer(serializers.ModelSerializer):
    # Use an explicit PrimaryKeyRelatedField to bypass hidden validation issues
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']

# serializers.py

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Order
        fields = ['id', 'user', 'total_amount', 'address', 'full_name', 'items', 'created_at']

    def create(self, validated_data):
        items_data = validated_data.pop('items', [])
        order = Order.objects.create(**validated_data)
        
        for item_data in items_data:
            # item_data['product'] is the Product object because of the Serializer validation
            product = item_data['product']
            
            # THE FIX: Manually assign the price from the product to the order item
            OrderItem.objects.create(
                order=order, 
                product=product,
                quantity=item_data['quantity'],
                price=product.price  # Grabbing the current price of the product
            )
            
        return order
      
from .models import Wishlist


class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = "__all__"
