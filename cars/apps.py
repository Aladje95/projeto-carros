from django.apps import AppConfig


class CarsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "cars"

    def ready(self):
        # Import signals to ensure they are registered
        import cars.signals
