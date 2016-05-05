from django.apps import AppConfig


class ConfigurationConfig(AppConfig):
    name = 'configuration'

    def ready(self):
        # from .helpers import get_cbr_info
        # get_cbr_info()
        pass