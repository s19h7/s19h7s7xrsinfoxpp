from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class S1gh7ts7txrAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'get_html_img', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("title",)}
    fields = ('title', 'slug', 'cat', 'content', 'photo', 'get_html_img', 'is_published', 'time_create','time_update')
    readonly_fields = ('time_create','time_update', 'get_html_img')

    def get_html_img(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=150")
    get_html_img.short_description = 'img'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(S1gh7ts7txr, S1gh7ts7txrAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'admin'
admin.site.site_header = 'admin'