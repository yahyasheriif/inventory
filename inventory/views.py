from rest_framework import viewsets, permissions ,generics , filters
from .models import InventoryItem , InventoryChangeLog
from .serializers import InventoryItemSerializer, UserSerializer , InventoryChangeLogSerializer
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny

# UserCreateAPIView:
#- queryset: All User objects.
#- permission_classes: Allow any user to create a new user.

class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny] 

# IsOwnerOrReadOnly:
#- has_object_permission: Check if the request user is the owner of the object.
class IsOwnerOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

# InventoryItemViewSet:
#- queryset: All InventoryItem objects.
#- permission_classes: Allow authenticated users to view and edit, and only owners to edit.
#- perform_create: Save the owner of the inventory item as the request user.
#- filterset_fields: Fields that can be filtered.
#- ordering: Default ordering by name.
class InventoryItemViewSet(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        previous_quantity = instance.quantity
        response = super().update(request, *args, **kwargs)
        if 'quantity' in request.data:
            new_quantity = int(request.data['quantity'])
        quantity_changed = new_quantity - previous_quantity
        if quantity_changed != 0:
            InventoryChangeLog.objects.create(
                item=instance,
                changed_by=request.user,
                quantity_changed=quantity_changed,
            )
        return response
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['category', 'price', 'quantity']
    ordering_fields = ['name', 'quantity', 'price', 'date_added']
    ordering = ['name'] 

# UserViewSet:
#- queryset: All User objects.
#- serializer_class: Serializer for User objects.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
# InventoryChangeLogViewSet
#- serializer_class: Serializer for InventoryChangeLog objects.
#- permission_classes: Allow only authenticated users to view change logs.
class InventoryChangeLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = InventoryChangeLog.objects.all()
    serializer_class = InventoryChangeLogSerializer
    permission_classes = [permissions.IsAuthenticated]