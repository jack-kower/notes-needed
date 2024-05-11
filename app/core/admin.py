from django.contrib import admin
from core.models import User, Note


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'is_active', 'is_staff']
    search_fields = ['email']
    list_filter = ['is_active', 'is_staff']

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'created_at', 'updated_at']
    search_fields = ['title']
    list_filter = ['created_at', 'updated_at']
