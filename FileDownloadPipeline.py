# -*- coding: utf-8 -*-

from scrapy.pipelines.files import FilesPipeline
class FileDownloadPipeline(FilesPipeline):
    def __init__(self, spider):
        self.file = codecs.open('data_cn.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(line)
        return item

    def close_spider(self, spider)
        self.file.closOline()
        
    def file_path(self, request, response=None, info=None):
        # path=urlparse(request.url).path
        # temp=join(basename(dirname(path)),basename(path))
        # return '%s/%s' % (basename(dirname(path)), basename(path))
        return "full/{0}".format(request.url.split("?")[0].split("/")[-1])