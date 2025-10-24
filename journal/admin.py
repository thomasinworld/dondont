from django.contrib import admin
from .models import DoDont, DailyEntry


@admin.register(DoDont)
class DoDontAdmin(admin.ModelAdmin):
    list_display = ['text', 'item_type', 'is_active', 'order', 'created_at']
    list_filter = ['item_type', 'is_active']
    search_fields = ['text']
    ordering = ['order', 'created_at']


@admin.register(DailyEntry)
class DailyEntryAdmin(admin.ModelAdmin):
    list_display = ['date', 'dodont', 'completed']
    list_filter = ['date', 'completed', 'dodont__item_type']
    date_hierarchy = 'date'
    ordering = ['-date']

