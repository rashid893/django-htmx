from django.contrib import admin
from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    # Display as table columns
    list_display = (
        'id',
        'name',
        'created_at',
    )

    # Right-side filters
    list_filter = (
        'created_at',
    )

    # Top search box
    search_fields = (
        'name',
        'description',
    )

    # Default ordering
    ordering = (
        '-created_at',
    )

    # Read-only fields
    readonly_fields = (
        'created_at',
    )
