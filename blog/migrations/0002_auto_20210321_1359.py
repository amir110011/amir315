# Generated by Django 3.1.7 on 2021-03-21 10:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان دسته بندی')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='آدرس')),
                ('status', models.BooleanField(default=True, verbose_name='آیا نمایش داده شود؟')),
                ('position', models.IntegerField(verbose_name='پوزیشن')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
                'ordering': ['position'],
            },
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'پست', 'verbose_name_plural': 'پست ها'},
        ),
        migrations.AlterModelOptions(
            name='slider',
            options={'verbose_name': 'اسلایدر صفحه اصلی', 'verbose_name_plural': 'اسلایدر صفحه اصلی'},
        ),
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد'),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان انتشار'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=200, unique=True, verbose_name='آدرس'),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('d', 'پیش نویس'), ('p', 'منتشر شده')], max_length=1, verbose_name='وضعیت'),
        ),
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(upload_to='imgpost', verbose_name='تصویر'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='زمان بروزرسانی'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=models.ImageField(upload_to='imgslider', verbose_name='تصویر'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='link',
            field=models.CharField(max_length=100, verbose_name='آدرس دکمه'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='title',
            field=models.CharField(max_length=100, verbose_name='عنوان'),
        ),
    ]