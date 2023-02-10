from django.contrib import admin
from apps.ping_app.models import Ping

@admin.register(Ping)
class PingAdmin(admin.ModelAdmin):
    search_fields = ('host', 'created_at')
    list_display = ( 'host', 'created_at')

