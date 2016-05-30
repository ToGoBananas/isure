from django.apps import AppConfig


class PoliciesConfig(AppConfig):
    name = 'policies'

    def ready(self):
        from . import signals