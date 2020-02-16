# -*- coding: utf-8 -*-
from django.db import models
    
# 上传图片  设置media以显示图片
class Image(models.Model):
    pic_name = models.CharField('图片名称', max_length=40)
    pic_path = models.ImageField('选择图片', upload_to="pic_folder/", default='')