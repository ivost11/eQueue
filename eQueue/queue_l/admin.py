from django.contrib import admin
from .models import QueueL


class QueueAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')


admin.site.register(QueueL, QueueAdmin)
