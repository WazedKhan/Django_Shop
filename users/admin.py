from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from users.models import UserInfo

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class UserInLine(admin.StackedInline):
    model = UserInfo
    can_delete: False
    verbose_name_plural = 'users'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (UserInLine,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)