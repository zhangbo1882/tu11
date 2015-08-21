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
    """
    def media_downloaded(self, response, request, info):
        referer = request.headers.get('Referer')
        if response.status != 200:
            logger.warning(
                'File (code: %(status)s): Error downloading file from '
                '%(request)s referred in <%(referer)s>',
                {'status': response.status,
                 'request': request, 'referer': referer},
                extra={'spider': info.spider}
            )
            raise FileException('download-error')

        if not response.body:
            logger.warning(
                'File (empty-content): Empty file from %(request)s referred '
                'in <%(referer)s>: no-content',
                {'request': request, 'referer': referer},
                extra={'spider': info.spider}
            )
            raise FileException('empty-content')

        status = 'cached' if 'cached' in response.flags else 'downloaded'

        logger.debug(
            'File (%(status)s): Downloaded file from %(request)s referred in '
            '<%(referer)s>',
            {'status': status, 'request': request, 'referer': referer},
            extra={'spider': info.spider}
        )

        self.inc_stats(info.spider, status)

        try:
            path = self.file_path(request, response=response, info=info)
            checksum = self.file_downloaded(response, request, info)
        except FileException as exc:
            logger.warning(
                'File (error): Error processing file from %(request)s '
                'referred in <%(referer)s>: %(errormsg)s',
                {'request': request, 'referer': referer, 'errormsg': str(exc)},
                extra={'spider': info.spider}, exc_info=True
            )
            raise
        except Exception as exc:
            logger.error(
                'File (unknown-error): Error processing file from %(request)s '
                'referred in <%(referer)s>',
                {'request': request, 'referer': referer},
                exc_info=True, extra={'spider': info.spider}
            )
            raise FileException(str(exc))

        return {'url': request.url, 'path': path, 'checksum': checksum}
    """