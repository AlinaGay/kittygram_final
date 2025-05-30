"""
App configuration for the cats application.

This module defines the configuration class for the cats app,
including default settings such as the auto field type and app name.
"""


from django.apps import AppConfig


class CatsConfig(AppConfig):
    """Configuration class for the cats application."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cats'
