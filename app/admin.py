from django.contrib import admin
from .models import RoomMember
# Register your models here.

# class RoomMemberAdmin(admin.ModelAdmin):
    
admin.site.register(RoomMember)