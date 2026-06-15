from django.contrib import admin
from .models import About

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_description', 'updated_at')
    readonly_fields = ('updated_at',)