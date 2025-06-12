from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from user.models import User

admin.site.register(User, UserAdmin)
class CastomUserAdmin(admin.ModelAdmin):
    list_display = ['username','avatar','email', 'password']