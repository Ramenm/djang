import sys
from django.apps import AppConfig

class HnewsConfig(AppConfig):
    name = 'hnews'

"""
    def ready(self):
        if 'runserver' not in sys.argv:
            return True


        from threading import Thread
        from .parser import post_parse_and_create

        t = Thread(target=post_parse_and_create)
        t.start()
"""
