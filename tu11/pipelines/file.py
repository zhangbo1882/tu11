__author__ = 'Aaron'
import hashlib
import os
from scrapy.http.request import Request
from scrapy.pipelines.images import ImagesPipeline
import traceback
class Tu11Pipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        requests = [Request(x) for x in item.get("image_urls", [])]
        for request in requests:
            request.meta['item']=item
        return requests

    def file_path(self, request, response=None, info=None):
        dir_name = request.meta['item']['image_name']
        media_guid = hashlib.sha1(request.url).hexdigest()  # change to request.url after deprecation
        media_ext = os.path.splitext(request.url)[1]  # change to request.url after deprecation
        return '%s/%s%s' % (dir_name, media_guid, media_ext)