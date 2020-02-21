# Generated by Django 2.2.6 on 2020-02-21 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20200217_0759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='pic_name',
            field=models.CharField(max_length=40, verbose_name='名称'),
        ),
        migrations.AlterField(
            model_name='image',
            name='pic_path',
            field=models.ImageField(default='', upload_to='pic_folder/', verbose_name='图片 url'),
        ),
    ]
