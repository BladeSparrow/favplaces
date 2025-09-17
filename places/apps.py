from django.apps import AppConfig

<<<<<<< HEAD

class PlacesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'places'
=======
class PlacesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'places'

    def ready(self):
        try:
            from favplaces.__init__ import cleanup_on_start
            cleanup_on_start()
        except Exception:
            pass
>>>>>>> 05b0b54 (Lab implementation: models, views, templates, cleanup)
