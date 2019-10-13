# -*- coding: utf-8 -*-
import scrapy
import json

from weibo.items import WeiboItem


class WeibouserSpider(scrapy.Spider):
    name = 'weibouser'
    allowed_domains = ['api.weibo.cn']
    base_url = "https://api.weibo.cn/2/profile/statuses/tab?gsid=_2A25wmzS4DeRxGeNL6VUQ9SnOzzWIHXVR8c9wrDV6PUJbgdAKLUynkWpNSQ_IgT6nKRYAmA76Efq5w30wURBsCIZb&sensors_mark=0&wm=3333_2001&sensors_is_first_day=false&from=1099393010&b=0&c=iphone&networktype=wifi&skin=default&v_p=76&v_f=1&s=23036b81&sensors_device_id=924ED248-6C49-46C4-856B-FB150546F494&lang=zh_CN&sflag=1&ua=iPhone10,3__weibo__9.9.3__iphone__os12.4.1&ft=11&aid=01A82CL_2in9r1iJhUF3ol4vC-66hJP1iC8Om692CpUdcD33E.&oriuicode=10000011_10000011_10000198&page_interrupt_enable=0&moduleID=pagecard&orifid=1005055527157249_-_new%24%24231093_-_selffollowed%24%24230283{user}&count=200&luicode=10000198&containerid=230413{user}_-_WEIBO_SECOND_PROFILE_WEIBO_VIDEO&fid=230413{user}_-_WEIBO_SECOND_PROFILE_WEIBO_VIDEO&uicode=10000011&need_head_cards=0&feed_mypage_card_remould_enable=1&need_new_pop=1&page={page}&client_key=75e2c9bcd65d13ac61c877ddaa458060_1a24&lfid=230283{user}&sourcetype=page&lcardid=more_weibo"

    custom_settings = {
        'DOWNLOAD_DELAY': 5,
    }

    def start_requests(self):
        users = [
            '5525226559',
            '6343583387',
        ]
        page = 1
        for user in users:
            url = self.base_url.format(user=user, page=page) 
            yield scrapy.Request(url=url, callback=self.parse, meta={"page":page, "user":user})

    def parse(self, response):
        try:
            jsobj = json.loads(response.body) 
            user = response.meta['user']
            page = int(response.meta['page'])
            # JSON.cards[3].mblog.page_info.media_info
            if not jsobj["cards"]:
                return

            for i in jsobj["cards"]:
                try:
                    item = WeiboItem()
                    item["user"] = user
                    item["page"] = page
                    item["media_id"] = i["mblog"]["page_info"]["media_info"]["media_id"]
                    item["title"] = i["mblog"]["page_info"]["media_info"]["next_title"]
                    item["duration"] = i["mblog"]["page_info"]["media_info"]["duration"]
                    item["sd_url"] = i["mblog"]["page_info"]["media_info"]["mp4_sd_url"]
                    item["file_urls"] = [i["mblog"]["page_info"]["media_info"]["mp4_sd_url"]]
                    item["hd_url"] = i["mblog"]["page_info"]["media_info"]["mp4_hd_url"]
                    print("item:",item)
                    yield item
                except Exception as e:
                    print(e)

            page += 1
            url = self.base_url.format(user=user, page=page)
            yield scrapy.Request(url=url, callback=self.parse, meta={"page":page, "user":user})
        except Exception as e:
            print(e)

        
        

    
