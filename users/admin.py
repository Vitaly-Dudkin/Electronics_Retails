from django.contrib import admin

from users.models import User


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'city', 'avatar', 'is_staff', 'is_superuser', 'is_active')
    list_filter = ('city',)
    search_fields = ('email', 'phone')
    filter_horizontal = ('groups',)
