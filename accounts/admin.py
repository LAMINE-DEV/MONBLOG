from django.contrib import admin
from accounts.models import Profile

# Register your models here.
@admin.register(Profile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('telephone','photo')
    search_fields = ('telephone','user')
