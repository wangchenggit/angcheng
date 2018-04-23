# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
import datetime
import scrapy
import re
from scrapy.loader.processors import MapCompose,TakeFirst
from scrapy.loader import ItemLoader
class Youyuan222Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


def add_jobbole(value):
    return value+"jobbole"


def date_convert(value):
    try:
        create_time = datetime.datetime.strptime(value, "%Y/%m/%d").date()
    except Exception as e:
        create_time = datetime.datetime.now()
    return create_time
def nums(value):
    value = value.strip().split(" ", 1)[0]
    if not re.findall(r"\d+\d*",value):
        value = 0
    return value
class Jobboleloder(ItemLoader):
    default_output_processor =TakeFirst()
class JobboleItem(scrapy.Item):
    url=scrapy.Field() #路由
    url_md5=scrapy.Field() #加密成定长路由
    
    img_url = scrapy.Field()  # 图片
    img_path=scrapy.Field()  # 图片本地路径
    title = scrapy.Field(
        input_processor=MapCompose(lambda x:x+"-body",add_jobbole)
    )  # 标题
    create_time = scrapy.Field(
        input_processor=MapCompose( date_convert)
    )  # 发布时间
    zan_num = scrapy.Field(
        input_processor=MapCompose()
    )  # 赞数
    cang_num = scrapy.Field(
        input_processor=MapCompose(nums)
    )  # 收藏数
    ping_num = scrapy.Field(
        input_processor=MapCompose(nums)
    )  # 评论数
    content = scrapy.Field()  # 文章内容html
    tags = scrapy.Field()  # 除去评论所属类别

