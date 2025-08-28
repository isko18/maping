from django.contrib import admin
from .models import Visitor, Image

@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    list_display = ("ip_address", "latitude", "longitude", "visited_at", "user_agent")
    list_filter = ("visited_at",)
    search_fields = ("ip_address", "user_agent")

admin.site.register(Image)