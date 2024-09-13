# django/contrib/auth/admin.py

from django.contrib import admin
from .models import Customuser

# Register User and Group models
admin.site.register(Customuser)