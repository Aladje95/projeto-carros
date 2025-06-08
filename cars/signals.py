from django.db.models.signals import post_save, post_delete, pre_save
from django.db.models import Sum
from django.dispatch import receiver
from .models import Car, CarInventory
# from openai_api.cliente import get_car_ai_bio
# from django.db.models.signals import pre_save, post_save, pre_delete, post_delete


# @receiver(pre_save, sender=Car)
# def car_pre_save(sender, instance, **kwargs):
#     print(f"Pre-save signal triggered for {instance}")
#     print(f"Instance data: {instance.__dict__}")


def car_inventory_update():
    cars_count = Car.objects.all().count()
    cars_price = Car.objects.aggregate(total_price=Sum('price'))['total_price']

    CarInventory.objects.create(
        cars_count=cars_count,  # Count of all cars
        cars_price=cars_price   # Total price of all cars
    )


@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    if not instance.bio:
        instance.bio = 'Bio gerada automaticamente'  # Placeholder for AI-generated bio


# isto é um exemplo de como você poderia usar o OpenAI para gerar uma biografia de carro
# @receiver(pre_save, sender=Car)
# def car_pre_save(sender, instance, **kwargs):
#     if not instance.bio:
#         ai_bio = get_car_ai_bio(
#             instance.model, instance.brand, instance.model_year
#         )
#     instance.bio = ai_bio


@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    car_inventory_update()
    # cars_count = Car.objects.all().count()
    # cars_price = Car.objects.aggregate(total_price=Sum('price'))['total_price']

    # CarInventory.objects.create(
    #     cars_count=cars_count,  # Count of all cars
    #     cars_price=cars_price   # Total price of all cars
    # )

    # print(f"Post-save signal triggered for {instance}")
    # print(f"Instance data: {instance.__dict__}")


# @receiver(pre_delete, sender=Car)
# def car_pre_delete(sender, instance, **kwargs):
#     print(f"Pre-delete signal triggered for {instance}")
#     print(f"Instance data: {instance.__dict__}")


@receiver(post_delete, sender=Car)
def car_pos_delete(sender, instance, **kwargs):
    car_inventory_update()
    # cars_price = Car.objects.aggregate(total_price=Sum('price'))['total_price']

    # CarInventory.objects.create(
    #     cars_count=cars_count,  # Count of all cars
    #     cars_price=cars_price   # Total price of all cars
    # )
    # print(f"Post-delete signal triggered for {instance}")
    # print(f"Instance data: {instance.__dict__}")
