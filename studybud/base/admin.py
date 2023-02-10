from django.contrib import admin
from .models import Room, Topic, Message


class RoomAdmin(admin.ModelAdmin):
    list_display = ('name','description')


admin.site.register(Room, RoomAdmin)
admin.site.register(Topic)
admin.site.register(Message)


