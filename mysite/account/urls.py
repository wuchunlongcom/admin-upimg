# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [ 
    url(r'index/$', views.index, name='index'),      
    url(r'upload/pic/$', views.upload_pic, name='upload_pic'),
    url(r'', views.index, name='index'),   #必须放在最后
]
