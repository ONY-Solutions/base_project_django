from django.apps import AppConfig

class DefaultModuleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'src.application.default'

    def ready(self):
        import src.application.default.signals