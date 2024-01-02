from django.db import models

# Create your models here.

    

class Juice(models.Model):
    juice_name = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='juice/')

    def __str__(self):
        return self.juice_name
    

class Ingredients(models.Model):
    name = models.ForeignKey(Juice, on_delete=models.CASCADE, related_name='juices')
    ingredient = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.ingredient


ORDER_CHECK = (
    ('Order Place', 'Order Place'),
    ('Order Confirm', 'Order Confirm'),
    ('Order Delivered', 'Order Delivered')
)

class Room(models.Model):
    juice = models.ForeignKey(Juice, on_delete=models.CASCADE, related_name='juicess')
    room_number = models.CharField(max_length=10)
    order_check = models.CharField(max_length=100, choices=ORDER_CHECK, default='Order Place')

    def __str__(self):
        return self.room_number