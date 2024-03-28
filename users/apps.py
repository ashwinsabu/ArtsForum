"""Users module for login and signup"""
from django.apps import AppConfig

class UsersConfig(AppConfig):
    """Class for application - user sign up and login"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
