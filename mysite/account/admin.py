# -*- coding: utf-8 -*-
import os
from django.contrib import admin
from .models import  Image
from django.contrib import messages

IMG_SIZE = 1024*300 # 设定上传图片大小300K

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):    
    list_display = ('id','pic_name','pic_path', 'image_data')
    readonly_fields = ('image_data',)

    def save_model(self, request, obj, form, change):
        # 图片大小设定值 不保存
        if obj.pic_path and obj.pic_path.size > IMG_SIZE:
            messages.set_level(request, messages.ERROR)
            messages.error(request, 'The picture\'s too large. \
            It\'s supposed smaller than %sK.' %str(IMG_SIZE/1024))
        else:
            obj.save()


  
  
