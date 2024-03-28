"""Bids module for displaying arts"""
from django.apps import AppConfig

class BidConfig(AppConfig):
    """Class for poststing Bids"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bid'
