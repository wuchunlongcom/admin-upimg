# -*- coding: utf-8 -*-

import os
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver 
from django.conf import settings
    
# 上传图片  设置media以显示图片
class Image(models.Model):
    pic_name = models.CharField('图片名称', max_length=40)
    pic_path = models.ImageField('选择图片', upload_to="pic_folder/", default='')
    
    
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