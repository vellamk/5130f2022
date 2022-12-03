from django.contrib import admin

# Register your models here.
from .models import OverAll
from .models import LogIn

admin.site.register(LogIn)