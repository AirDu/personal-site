from django.contrib import admin
from .models import UserProfile


class UPAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(UserProfile, UPAdmin)
