from django.db import models
from django.utils import timezone
from extentions.utils import jalali_convertor

# tagmanagers


class PostManager(models.Manager):
    def published(self):
        return self.filter(status='p')

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان دسته بندی")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="آدرس")
    status = models.BooleanField(
        default=True, verbose_name="آیا نمایش داده شود؟")
    position = models.IntegerField(verbose_name="پوزیشن")

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
        ordering = ['position']

    def __str__(self):
        return self.title


class Post(models.Model):
    STATUS_CHOICES = [
        ('d', 'پیش نویس'),
        ('p', 'منتشر شده'),
    ]
    title = models.CharField(max_length=100, verbose_name="عنوان")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="آدرس")
    category = models.ManyToManyField(
        Category, verbose_name="دسته بندی", related_name="postcat")
    description = models.TextField(verbose_name="توضیحات")
    thumbnail = models.ImageField(
        upload_to="imgpost", height_field=None, width_field=None, max_length=None, verbose_name="تصویر")
    publish = models.DateTimeField(
        default=timezone.now, verbose_name="زمان انتشار")
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="زمان ایجاد")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="زمان بروزرسانی")
    status = models.CharField(
        max_length=1, choices=STATUS_CHOICES, verbose_name="وضعیت")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "پست"
        verbose_name_plural = "پست ها"

    def jpublish(self):
        return jalali_convertor(self.publish)
    jpublish.short_description = "زمان انتشار"
    objects = PostManager()
    def caegorty_published(self):
        return self.category.filter(status=True)


# slide moodels
class Slider(models.Model):
    STATUS_CHOICES = [('d', 'عدم نمایش'),('p', 'نمایش'), ]
    title = models.CharField(max_length=100, verbose_name="عنوان")
    link = models.CharField(max_length=100, verbose_name="آدرس دکمه")
    image = models.ImageField(upload_to="imgslider", verbose_name="تصویر")
    status = models.CharField(
        max_length=1, choices=STATUS_CHOICES, verbose_name="وضعیت",default='p')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "اسلایدر صفحه اصلی"
        verbose_name_plural = "اسلایدر صفحه اصلی"


class Weblog_setting(models.Model):
    about_me = models.TextField(verbose_name="درباره من")
    STATUS_CHOICES = [
        ('d', 'عدم نمایش'),
        ('p', 'نمایش'),

    ]
    status = models.CharField(
        max_length=1, default='1', choices=STATUS_CHOICES, verbose_name="وضعیت")

    class Meta:
        verbose_name = "تنظیمات سایت"
        verbose_name_plural = "تنظیمات سایت"

    def __str__(self):
        return self.about_me



