from django.contrib import admin
from .models import *
# Register your models here.

# header admin panel title
admin.site.site_header ="مدیریت وبلاگ امیر نبوی"

def make_published(modeladmin, request, queryset):
    rows_pub = queryset.update(status='p')
    if rows_pub == 1:
        message_bit="منتشر شد."
    else:
        message_bit = "وضعیت {} پست به حالت منتشر شده تغییر داده شد.".format(rows_pub)
    modeladmin.message_user(request, message_bit)
make_published.short_description = "تغییر به وضعیت منتشر شده"

def make_draft (modeladmin, request, queryset):
    rows_drft = queryset.update(status='d')
    if rows_drft == 1:
        message_bit = "پیشنویس شد."
    else:
        message_bit = "وضعیت {} پست به حالت پیشنویس تغییر داده شدند.".format(
            rows_drft)
    modeladmin.message_user(request, message_bit)

make_draft.short_description = "تغییر به وضعیت پیش نویس"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'slug','parent', 'status')
    list_filter = (['status'])
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('img_tag', 'title','author', 'slug',
                    'jpublish', 'status', 'cat_to_str')
    list_filter = ('status', 'publish', 'author')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-publish',)
    actions = [make_published, make_draft]

    def cat_to_str(self,obj):
        return ", ".join([category.title for category in obj.category.active()])
    cat_to_str.short_description ="دسته بندی"



class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'link')


class Weblog_settingAdmin(admin.ModelAdmin):
    list_display = ('about_me',)

admin.site.register(Slider, SliderAdmin)

admin.site.register(Weblog_setting, Weblog_settingAdmin)

