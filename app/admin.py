from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Note

# class CustomUserAdmin(UserAdmin):
#     fieldsets = UserAdmin.fieldsets + (
#         (None, {'fields': ('phone_number',)}),
#     )

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_number')

admin.site.register(CustomUser, CustomUserAdmin)


class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('title', 'content')

admin.site.register(Note, NoteAdmin)