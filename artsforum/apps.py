"""Artsforum module for displaying arts"""
from django.apps import AppConfig

class ArtsforumConfig(AppConfig):
    """Class for application - landing page and posting of arts"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'artsforum'
