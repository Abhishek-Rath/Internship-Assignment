from django.db import models

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length = 50)
    description = models.TextField()
    price = models.IntegerField(default = 0)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check = models.Q(price__gte = 1),
                name = "Price >= 1"
            )
        ]

    def __str__(self):
        return f"Name: {self.item_name}\nDescription: {self.description}\nPrice: {self.price}\n"


class Invoice(models.Model):
    quantity = models.IntegerField(default = 0)
    item = models.ForeignKey('Item', related_name = 'item', on_delete = models.CASCADE)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check = models.Q(quantity__gte = 1),
                name = "Quantity >= 1"
            )
        ]

    def __str__(self):
        return f"Item: {self.item.item_name} Quantity: {self.quantity}"
    