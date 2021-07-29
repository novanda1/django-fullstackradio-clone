from django.contrib import admin
from .models import Episode, Host
from cms.admin.placeholderadmin import PlaceholderAdminMixin, FrontendEditableAdminMixin


@admin.register(Episode)
class EpisodeAdmin(FrontendEditableAdminMixin, PlaceholderAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'host')
    list_filter = ('created',)
    frontend_editable_fields = ('excerpt', 'podcast')


@admin.register(Host)
class HostAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name',)
