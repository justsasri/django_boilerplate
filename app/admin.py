from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from .models import Category


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    pass
