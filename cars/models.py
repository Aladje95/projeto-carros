from django.db import models

# Create your models here.


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    brand = models.ForeignKey(
        Brand, on_delete=models.PROTECT, related_name='car_brand')
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    plate = models.CharField(max_length=20, blank=True, null=True)
    photo = models.ImageField(
        upload_to='cars/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.model} {self.model_year}"


class CarInventory(models.Model):
    cars_count = models.IntegerField(default=0)
    cars_price = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Inventory at {self.created_at} - Count: {self.cars_count}, Total Price: {self.cars_price}"
