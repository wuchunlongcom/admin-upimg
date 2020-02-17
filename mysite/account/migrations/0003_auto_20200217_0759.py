# Generated by Django 2.2.6 on 2020-02-16 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20200216_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='pic_name',
            field=models.CharField(max_length=40, verbose_name='图片名称'),
        ),
        migrations.AlterField(
            model_name='image',
            name='pic_path',
            field=models.ImageField(default='', upload_to='pic_folder/', verbose_name='选择图片'),
        ),
    ]