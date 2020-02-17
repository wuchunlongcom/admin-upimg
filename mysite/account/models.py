# -*- coding: utf-8 -*-

import os
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver 
from django.conf import settings
from django.utils.html import format_html

    
# 上传图片  设置media以显示图片
class Image(models.Model):
    pic_name = models.CharField('名称', max_length=40)
    pic_path = models.ImageField('图片 url', upload_to="pic_folder/", default='')

    def image_data(self):
        """ admin 不是显示图片url路径，直接显示图片   """
        return format_html(
            '<img src="{}" width="100px"/>',
            self.pic_path.url,
        )
    image_data.short_description = u'图片'
    
    
@receiver(post_delete, sender=Image)
def delete_upload_files(sender, instance, **kwargs):   
    """
    admin 删除数据库记录，同时也删除图像文件
    """
    files = getattr(instance, 'pic_path', '')
    if not files:
        return 
    fname = os.path.join(settings.MEDIA_ROOT, str(files))
    if os.path.isfile(fname):
        os.remove(fname)