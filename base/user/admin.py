from django.contrib import admin

from user.models import User

admin.site.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username','avatar','email', 'password']