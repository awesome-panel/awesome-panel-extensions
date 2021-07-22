"""Provides the Application and Site"""
from .models import Application, User
from .site import Site
from .site_config import SiteConfig

site = Site()
