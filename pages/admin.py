from django.contrib import admin
from .models import *
# Register your models here.
from django.utils.html import format_html

class teamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius:50%;" />'.format(object.photo.url))
    thumbnail.short_description ='Image'
    list_display = ['id','thumbnail','first_name','designation','created_date']
    list_display_links = ['first_name','id','thumbnail']
    search_fields =['first_name','last_name','designation']
    list_filter=['designation']

admin.site.register(Team,teamAdmin)