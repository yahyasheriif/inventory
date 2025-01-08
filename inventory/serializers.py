from rest_framework import serializers
from .models import InventoryItem , InventoryChangeLog
from django.contrib.auth.models import User


# InventoryItemSerializer:
#     - Serializes InventoryItem model.
#     - Includes a read-only field for the owner's username.
#     - Validates that price and quantity are greater than 0 and name is not empty.

class InventoryItemSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = InventoryItem
        fields = '__all__'
    def validate(self, data):
        if data.get('price') <=0:
            raise serializers.ValidationError("Price must be greater than 0")
        if data['quantity'] <= 0:
            raise serializers.ValidationError("Quantity must be greater than 0")
        if data['name'] == "":
            raise serializers.ValidationError("Name cannot be empty")
        return data

# UserSerializer:
#     - Serializes User model.
#     - Includes related inventory items as primary key related fields.

class UserSerializer(serializers.ModelSerializer):
    inventory_items = serializers.PrimaryKeyRelatedField(many=True, queryset=InventoryItem.objects.all())
    class Meta:
        model = User
        fields = ['id', 'username', 'inventory_items']
        
# InventoryChangeLogSerializer:
#     - Serializes InventoryChangeLog model.
#     - Includes a read-only field for the username of the user who made the change.

class InventoryChangeLogSerializer(serializers.ModelSerializer):
    changed_by = serializers.ReadOnlyField(source='changed_by.username')
    class Meta:
        model = InventoryChangeLog
        fields = '__all__'