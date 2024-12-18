from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Notification


class NotificationAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "message_preview", "created_at", "is_read")
    search_fields = ("user__username", "message")
    list_filter = ("is_read", "created_at")
    ordering = ("-created_at",)

    def message_preview(self, obj):
        return (
            obj.message[:30] + "..." if len(obj.message) > 30 else obj.message
        )

    message_preview.short_description = _("Предварительный просмотр сообщения")

    @admin.action(
        description=_("Отметить выбранные уведомления как прочитанные")
    )
    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)

    actions = [mark_as_read]


admin.site.register(Notification, NotificationAdmin)
