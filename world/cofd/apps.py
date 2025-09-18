from django.apps import AppConfig


class CofdConfig(AppConfig):
    """
    Configuration for the Chronicles of Darkness (CofD) app.
    This app handles all CofD-specific game mechanics, models, and data.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'world.cofd'
    label = 'cofd'
    verbose_name = 'Chronicles of Darkness'

    def ready(self):
        """
        This method is called when Django starts.
        You can use it to register signals or perform other initialization.
        """
        pass 