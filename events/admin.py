from django.contrib import admin
from .models import Event
# Register your models here.


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("date","event","prioryt")
    list_display_links = ("event",)
    list_filter = ("date","prioryt")
    list_editable = ("prioryt",)
    search_fields = ("event","date")

