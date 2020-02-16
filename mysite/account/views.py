# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required 
from django.shortcuts import render
from .models import Image
from myAPI.pageAPI import djangoPage, PAGE_NUM

# http://localhost:8000/
#@login_required
def index(request):           
    meg = '最简单代码，实现图像文件上传。 <br>登录Admin后台, 上传图像文件并在前台显示图像。<br>\
        用户名/密码： admin/admin'
    return render(request, 'account/index.html', context=locals()) 

# 显示图片 http://localhost:8000/upload/pic/
def upload_pic(request, page):
    pic_list = Image.objects.all()
    pic_list, pageList, num_pages, page = djangoPage(pic_list, page, PAGE_NUM)
    offset = PAGE_NUM * (page - 1)
    return render(request,'account/image.html', context=locals())   