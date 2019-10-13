# -*- coding: utf-8 -*-

from scrapy.pipelines.files import FilesPipeline
from urlparse import urlparse
from os.path import basename,dirname,join
class FileDownloadPipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None):
        # path=urlparse(request.url).path
        # temp=join(basename(dirname(path)),basename(path))
        # return '%s/%s' % (basename(dirname(path)), basename(path))
        return request.url.split("?")[0].split("/")[-1]