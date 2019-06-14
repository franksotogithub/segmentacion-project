from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth.models import Group
from usuarios.models import Usuario
from usuarios.forms import UserChangeForm,UserCreationForm
# Register your models here.


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username','nombres','apellidos','dni','email','rol', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),

    )

    add_fieldsets = (
        (None, {'fields': ('username','nombres','apellidos','dni','email','rol', 'password1','password2')}),
        #('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
        #                               'groups', 'user_permissions')}),
    )

    form =UserChangeForm
    add_form = UserCreationForm
    change_password_form = auth_admin.AdminPasswordChangeForm
    ordering = ('username',)
    list_display = ('username','nombres','apellidos','dni',)
    search_fields = ('username',)
    pass
admin.site.unregister(Group)