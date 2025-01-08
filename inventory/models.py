from django.db import models
from django.contrib.auth.models import User

class InventoryItem(models.Model):
    name = models.CharField(max_length=255,unique=True)
    description = models.TextField(blank=True)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, related_name='inventory_items', on_delete=models.CASCADE)

    def str(self):
        return self.name
    
class InventoryChangeLog(models.Model):
    item = models.ForeignKey(InventoryItem, related_name='change_logs', on_delete=models.CASCADE)
    changed_by = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity_changed = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f'{self.item.name} changed by {self.changed_by.username}'