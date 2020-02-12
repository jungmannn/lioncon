# Generated by Django 2.2.3 on 2019-07-24 11:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='genre',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='image/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='notice',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='rating',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='save_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Movie Release date'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]