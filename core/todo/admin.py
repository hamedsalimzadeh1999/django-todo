from django.contrib import admin
from .models import task
# Register your models here.
@admin.register(task)
class Admin(admin.ModelAdmin):
    pass
