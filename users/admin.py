from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.forms import ModelForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField

# Formulár pre vytvorenie usera v admin rozhraní
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# Register your models here.


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'full_name')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'full_name', 'is_active',
                  'is_staff', 'is_superuser')


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = ('email', 'full_name', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'full_name', 'password')}),
        ('Práva', {'fields': ('is_staff',
         'is_superuser', 'groups', 'user_permissions')}),
        ('Dôležité dátumy', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'password1', 'password2', 'is_staff', 'is_superuser')}
         ),
    )
    search_fields = ('email', 'full_name')
    ordering = ('email',)


# Registrácia modelu v admine
admin.site.register(CustomUser, CustomUserAdmin)
