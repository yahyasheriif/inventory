from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InventoryItemViewSet, UserViewSet
from .views import InventoryChangeLogViewSet

# Routes:
# - 'items/': Routes to InventoryItemViewSet for managing inventory items.
# - 'users/': Routes to UserViewSet for managing users.
# - 'change_logs/': Routes to InventoryChangeLogViewSet for managing inventory change logs.
router = DefaultRouter()
router.register(r'items', InventoryItemViewSet)
router.register(r'users', UserViewSet)
router.register(r'change_logs', InventoryChangeLogViewSet)
urlpatterns = [
    path('', include(router.urls)),
]