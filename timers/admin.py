from django.contrib import admin
from .models import Timer


@admin.register(Timer)
class TimerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'start_time', 'end_time', 'is_active', 'created_at')
    list_filter = ('is_active', 'user')
    search_fields = ('name', 'user__email')
    readonly_fields = ('created_at', 'updated_at')
    raw_id_fields = ('user',)