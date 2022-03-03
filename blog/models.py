from django.db import models
from django.urls import reverse
from django.utils import timezone
from extentions.utils import jalali_convertor
from django.utils.html import format_html
from account.models import User

# tagmanagers


class PostManager(models.Manager):
    def published(self):
        return self.filter(status='p')


class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)

# Create your models here.


class Category(models.Model):
    parent = models.ForeignKey('self', default=None, null=True, blank=True,
                               on_delete=models.SET_NULL, related_name='children', verbose_name='زیر دسته')
    title = models.CharField(max_length=100, verbose_name="عنوان دسته بندی")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="آدرس")
    status = models.BooleanField(
        default=True, verbose_name="آیا نمایش داده شود؟")
    position = models.IntegerField(verbose_name="پوزیشن")

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
        ordering = ['parent__id', 'position']

    def __str__(self):
        return self.title
    objects = CategoryManager()


class Post(models.Model):
    STATUS_CHOICES = [
        ('d', 'پیش نویس'),
        ('p', 'منتشر شده'),
    ]
    title = models.CharField(max_length=100, verbose_name="عنوان")
    author = models.ForeignKey(
        User, null=True, on_delete=models.SET_NULL, related_name='post', verbose_name="نویسنده")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="آدرس")
    category = models.ManyToManyField(
        Category, verbose_name="دسته بندی", related_name="postcat")
    short_description = models.CharField(
        max_length=200, verbose_name="توضیحات کوتاه", null=True)
    description = models.TextField(
        blank=True, null=True, verbose_name="توضیحات")
    thumbnail = models.ImageField(upload_to="imgpost", height_field=None,
                                  width_field=None, max_length=None, verbose_name="تصویر")
    publish = models.DateTimeField(
        default=timezone.now, verbose_name="زمان انتشار")
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="زمان ایجاد")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="زمان بروزرسانی")
    status = models.CharField(
        max_length=1, choices=STATUS_CHOICES, verbose_name="وضعیت")
    is_special = models.BooleanField(default=False, verbose_name="مقاله ویژه")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "پست"
        verbose_name_plural = "پست ها"

    def jpublish(self):
        return jalali_convertor(self.publish)
    jpublish.short_description = "زمان انتشار"

    objects = PostManager()

    def img_tag(self):
        return format_html("<img src='{}' width=80 height=50>".format(self.thumbnail.url))
    img_tag.short_description = "تصویر"

    def category_to_str(self):
        return ", ".join([category.title for category in self.category.active()])
    category_to_str.short_description = "دسته بندی"

    def get_absolute_url(self):
        return reverse('account:home')

# slide moodels


class Slider(models.Model):
    STATUS_CHOICES = [('d', 'عدم نمایش'), ('p', 'نمایش'), ]
    title = models.CharField(max_length=100, verbose_name="عنوان")
    description = models.TextField(
        null=True, blank=True, verbose_name="توضیحات")
    btn_txt = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="عنوان دکمه")
    link = models.CharField(max_length=100, verbose_name="آدرس دکمه")
    image = models.ImageField(upload_to="imgslider", verbose_name="تصویر")
    status = models.CharField(
        max_length=1, choices=STATUS_CHOICES, verbose_name="وضعیت", default='p')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "اسلایدر صفحه اصلی"
        verbose_name_plural = "اسلایدر صفحه اصلی"


class Weblog_setting(models.Model):
    about_me = models.TextField(verbose_name="درباره من")

    class Meta:
        verbose_name = "تنظیمات سایت"
        verbose_name_plural = "تنظیمات سایت"

    def __str__(self):
        return self.about_me
