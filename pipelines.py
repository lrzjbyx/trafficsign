# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import os
from scrapy.pipelines.images import ImagesPipeline
from urllib import request
from trafficsign import settings
import re


class TrafficsignPipeline(ImagesPipeline):
    def get_media_requests(self,item,info):
            #   这个方法是在发送下载请求之前调用
        #   其实这个方法本身就是去发送下载请求的
        request_objs = super(TrafficsignPipeline,self).get_media_requests(item,info)
        for request_obj in request_objs:
            request_obj.item = item
        return request_objs

    def file_path(self, request, response=None, info=None):
        # super 返回的路径
        path = super(TrafficsignPipeline,self).file_path(request,response,info)
        url = request.url
        category = request.item.get("category")
        names =  request.item.get('names')
        urls = request.item.get('image_urls')
        u_index = int(re.search(r'\w{2}(\d+)\.jpg',url).group(1))-1
        # 获取文件名称
        file_name = names[u_index]
        # 删除不必要字符
        file_name = re.sub(r'[、\.,，!！]+',"",file_name)
        
        images_store = settings.IMAGES_STORE
        category_path = os.path.join(images_store,category)
        if not os.path.exists(category_path):
            os.mkdir(category_path)

        image_name = re.sub(r"full/[\d\w-]+",file_name,path)
        image_path = os.path.join(category_path,image_name)
        print(image_path)
        return image_path
