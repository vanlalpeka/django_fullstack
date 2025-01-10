from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Note
from import_export import resources


from import_export.admin import ImportExportModelAdmin, ExportActionMixin
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget, DateTimeWidget

# class CustomUserAdmin(UserAdmin):
#     fieldsets = UserAdmin.fieldsets + (
#         (None, {'fields': ('phone_number',)}),
#     )



class CustomUserResource(resources.ModelResource):

    class Meta:
        model = CustomUser 

@admin.register(CustomUser)
class CustomUserAdmin(ImportExportModelAdmin, ExportActionMixin):
    list_display = ('username', 'email', 'phone_number')
    search_fields = ('username', 'email', 'phone_number')
    resource_classes = [CustomUserResource]



class NoteResource(resources.ModelResource):

    class Meta:
        model = Note 

@admin.register(Note)
class NoteAdmin(ImportExportModelAdmin, ExportActionMixin):
    list_display = ('title', 'content', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('title', 'content')
    resource_classes = [NoteResource]