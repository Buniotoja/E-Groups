from django.contrib import admin
from .models import Meeting, MeetingChatMessage
from django.utils.html import format_html


class MessagesInline(admin.TabularInline):
    model = MeetingChatMessage


@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'date']
    list_filter = ['date']
    inlines = [MessagesInline]


@admin.register(MeetingChatMessage)
class MeetingChatMessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'text'[:20]]
    list_filter = ['meeting_id']
