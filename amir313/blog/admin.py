from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'slug', 'status')
    list_filter = (['status'])
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'jpublish', 'status', 'cat_to_str')
    list_filter = ('status', 'publish')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-publish',)
    
    def cat_to_str(self,obj):
        return ", ".join([category.title for category in obj.caegorty_published()])
    cat_to_str.short_description ="دسته بندی"


class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'link')


class Weblog_settingAdmin(admin.ModelAdmin):
    list_display = ('about_me',)

admin.site.register(Slider, SliderAdmin)

admin.site.register(Weblog_setting, Weblog_settingAdmin)

