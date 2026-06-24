from django.contrib import admin
from .models import contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'message', 'created_at')
    search_fields = ('name', 'message')


admin.site.register(contact, ContactAdmin)
