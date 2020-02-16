# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required 
from django.shortcuts import render
from .models import Image

# http://localhost:8000/
#@login_required
def index(request):           
    meg = '最简单代码，实现图像文件上传。 <br>登录Admin后台, 上传图像文件并在前台显示图像。<br>\
        用户名/密码： admin/admin'
    return render(request, 'account/index.html', context=locals()) 

# 显示图片 http://localhost:8000/upload/pic/
def upload_pic(request):
    pic_list = Image.objects.all()
    return render(request,'home/image.html',{'pic_list' : pic_list})   