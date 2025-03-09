from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Note, Department, NoteType
from import_export import resources
from django.contrib.auth.hashers import make_password


from import_export.admin import ImportExportModelAdmin, ExportActionMixin
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget, DateTimeWidget

# class CustomUserAdmin(UserAdmin):
#     fieldsets = UserAdmin.fieldsets + (
#         (None, {'fields': ('phone_number',)}),
#     )

# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import User

# class CustomUserAdmin(UserAdmin):
#     def get_readonly_fields(self, request, obj=None):
#         # Make 'is_superuser' read-only for non-superusers
#         if not request.user.is_superuser:
#             return self.readonly_fields + ('is_superuser',)
#         return self.readonly_fields

# admin.site.unregister(User)
# admin.site.register(User, CustomUserAdmin)


class NoteTypeResource(resources.ModelResource):
    class Meta:
        model = NoteType 
        permissions = (('import_notetype', 'Can import'), ('export_notetype', 'Can export'))

@admin.register(NoteType)
class NoteTypeAdmin(ImportExportModelAdmin, ExportActionMixin):
    resource_classes = [NoteTypeResource]



class DepartmentResource(resources.ModelResource):
    class Meta:
        model = Department 
        permissions = (('import_department', 'Can import'), ('export_department', 'Can export'))

@admin.register(Department)
class DepartmentAdmin(ImportExportModelAdmin, ExportActionMixin):
    resource_classes = [DepartmentResource]



class CustomUserResource(resources.ModelResource):

    def before_import_row(self, row, **kwargs):
        value = row.get('password')
        row['password'] = make_password(value)

    class Meta:
        model = CustomUser 

@admin.register(CustomUser)
class CustomUserAdmin(ImportExportModelAdmin, ExportActionMixin):
    list_display = ('username', 'designation', 'phone_number')
    search_fields = ('username', 'designation', 'phone_number')
    resource_classes = [CustomUserResource]

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        
        # Check if the logged-in user is not a superuser
        if not request.user.is_superuser:
            # Filter out unwanted fields
            filtered_fieldsets = []
            for name, options in fieldsets:
                fields = options.get("fields", [])
                # Exclude specific fields
                filtered_fields = [
                    field for field in fields 
                    if field not in ("groups", "user_permissions", "is_superuser", "is_staff", "email", "last_login", 'date_joined')
                ]
                # Add back only non-excluded fields
                if filtered_fields:
                    filtered_fieldsets.append((name, {"fields": filtered_fields}))
            return tuple(filtered_fieldsets)
        
        return fieldsets



class NoteResource(resources.ModelResource):
    concerned_department = fields.Field(
        column_name = "concerned_department",
        attribute = "concerned_department",
        widget = ForeignKeyWidget(Department, 'name')
    )

    class Meta:
        model = Note 
        permissions = (('import_note', 'Can import'), ('export_note', 'Can export'))


@admin.register(Note)
class NoteAdmin(ImportExportModelAdmin, ExportActionMixin):
    list_display = ('file_number', 'subject' ,'type', 'concerned_department', 'date')
    search_fields = ('file_number', 'concerned_department')
    list_filter = ('file_number', 'concerned_department')
    resource_classes = [NoteResource]