from django.contrib import admin
from .models import Teams
from django.utils.html import format_html
# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html(f'<img src={object.photo.url} width=40 style="border-radius:300%" />')
    thumbnail.short_description = 'photo'
    list_display = ('id','first_name','last_name','thumbnail','created_date')
    list_display_links = ('id','thumbnail','first_name')
    search_fields = ['first_name','designation']
    list_filter = ('designation',)
    
admin.site.register(Teams,TeamAdmin)