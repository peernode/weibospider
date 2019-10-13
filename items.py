# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# {
#     "video_orientation": "vertical",
#     "name": "陳登炫的微博视频",
#     "stream_url": "http://f.video.weibocdn.com/002pXtxplx07xJyfYzLW010412001RGw0E010.mp4?label=mp4_ld&template=360x640.24.0&trans_finger=81b11b8c5ffb62d33ceb3244bdd17e7b&Expires=1570971485&ssig=jFAHpMwfbU&KID=unistore,video",
#     "stream_url_hd": "http://f.video.weibocdn.com/003W7duWlx07xJyglFAc0104120038sv0E010.mp4?label=mp4_hd&template=576x1024.24.0&trans_finger=7c347e6ee1691b93dc7e5726f4ef34b3&Expires=1570971485&ssig=oATsLfehXq&KID=unistore,video",
#     "h5_url": "https://video.weibo.com/show?fid=1034:4426625366834041",
#     "mp4_sd_url": "http://f.video.weibocdn.com/002pXtxplx07xJyfYzLW010412001RGw0E010.mp4?label=mp4_ld&template=360x640.24.0&trans_finger=81b11b8c5ffb62d33ceb3244bdd17e7b&Expires=1570971485&ssig=jFAHpMwfbU&KID=unistore,video",
#     "mp4_hd_url": "http://f.video.weibocdn.com/003W7duWlx07xJyglFAc0104120038sv0E010.mp4?label=mp4_hd&template=576x1024.24.0&trans_finger=7c347e6ee1691b93dc7e5726f4ef34b3&Expires=1570971485&ssig=oATsLfehXq&KID=unistore,video",
#     "h265_mp4_hd": "",
#     "h265_mp4_ld": "",
#     "inch_4_mp4_hd": "",
#     "inch_5_mp4_hd": "",
#     "inch_5_5_mp4_hd": "",
#     "mp4_720p_mp4": "",
#     "hevc_mp4_720p": "",
#     "prefetch_type": 1,
#     "prefetch_size": 263804,
#     "act_status": 1,
#     "protocol": "general",
#     "media_id": "4426625366834041",
#     "origin_total_bitrate": 0,
#     "duration": 8,
#     "next_title": "当你跳的那一刻，我彻底失去了自我！",
#     "video_details": [
#         {
#             "size": 747503,
#             "bitrate": 667,
#             "label": "mp4_hd_url",
#             "prefetch_size": 263804
#         },
#         {
#             "size": 444696,
#             "bitrate": 396,
#             "label": "mp4_sd_url",
#             "prefetch_size": 160363
#         },
#         {
#             "size": 596177,
#             "bitrate": 532,
#             "label": "hevc_mp4_hd",
#             "prefetch_size": 209374
#         }
#     ],
#     "hevc_mp4_hd": "http://f.video.weibocdn.com/003lXrowgx07xJyhlM11010412002v5L0E010.mp4?label=hevc_mp4_hd&template=576x1024.28.0&trans_finger=f3bbcfd7f9a29628e813964123dca97d&Expires=1570971485&ssig=r5xx8fK9Ez&KID=unistore,video",
#     "play_completion_actions": [
#         {
#             "type": "1",
#             "icon": "http://img.t.sinajs.cn/t6/style/images/face/feed_c_r.png",
#             "text": "重播",
#             "link": "",
#             "btn_code": 1000,
#             "show_position": 1,
#             "actionlog": {
#                 "oid": "2304444426625366834041",
#                 "act_code": 1221,
#                 "act_type": 0,
#                 "source": "video"
#             }
#         }
#     ],
#     "video_publish_time": 1570873198,
#     "play_loop_type": 0,
#     "titles": [
#         {
#             "default": true,
#             "title": "当你跳的那一刻，我彻底失去了自我！上下波动。"
#         }
#     ],
#     "author_mid": "4426631315401013",
#     "author_name": "陳登炫",
#     "extra_info": {
#         "sceneid": "feed"
#     },
#     "has_recommend_video": 1,
#     "video_download_strategy": {
#         "abandon_download": 0
#     },
#     "online_users": "1.2万次观看",
#     "online_users_number": 12098,
#     "ttl": 3600,
#     "storage_type": "oss",
#     "is_keep_current_mblog": 0
# }
class WeiboItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    media_id = scrapy.Field()
    title = scrapy.Field()
    duration = scrapy.Field()
    sd_url = scrapy.Field()
    hd_url = scrapy.Field()
