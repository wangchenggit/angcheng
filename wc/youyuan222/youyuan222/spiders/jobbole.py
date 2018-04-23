# -*- coding: utf-8 -*-
import scrapy
# import re
# import datetime
# from scrapy.loader import ItemLoader
from urllib import parse
# from scrapy.xlib.pydispatch import dispatcher
from youyuan222.items import JobboleItem,Jobboleloder
from youyuan222.utils.common import get_md5
from scrapy_redis.spiders import RedisSpider

class JobboleSpider(RedisSpider):
    name = 'jobbole'
    allowed_domains = ['python.jobbole.com']
    # start_urls = ['http://python.jobbole.com/all-posts/']
    redis_key = "jobbole:start_urls"
    # handle_httpstatus_list = [404]
    #
    # def __init__(self):
    #     self.fail_urls = []
    #     dispatcher.connect(self.handle_spider_closed, signals.spider_closed)
    #
    # def handle_spider_closed(self, spider, reason):
    #     self.crawler.stats.set_value("failed_urls", ",".join(self.fail_urls))
    def parse(self, response):
        # if response.status==404:
        #     self.fail_urls.append(response.url)
        #     self.crawler.stats.inc_value("failed_url")
        #找出详情页,图片url回调详情函数处理
        content_nodes=response.xpath("//div[@id='archive']/div[@class='post floated-thumb']/div[@class='post-thumb']")
        for content_node in content_nodes:
            img_url=content_node.xpath(".//img/@src").extract_first("")
            content_url=content_node.xpath("./a/@href").extract_first("")
            yield scrapy.Request(url=parse.urljoin(response.url,content_url),meta={"img_url":img_url},callback=self.parse_detail)
        #下一列表页url，回调本身直至为空（有规律）
        next_url=response.xpath("//a[@class='next page-numbers']/@href").extract_first("")
        # print(next_url)
        if next_url:
            yield scrapy.Request(url=parse.urljoin(response.url,next_url),callback=self.parse)
    def parse_detail(self,response):
        item=JobboleItem()
        # #标题
        # title=response.xpath("//div[@class='entry-header']/h1/text()").extract_first("")
        # #发布时间
        # create_time=response.xpath("//p[@class='entry-meta-hide-on-mobile']/text()").extract()[0].strip().split(" ",1)[0]
        # # print(create_time)
        # create_time=create_time.strip().split(" ",1)[0]
        # #点赞数
        # zan_num=response.xpath("//span[contains(@class,'vote-post-up')]/h10/text()").extract()[0]
        # # print(zan)
        # #收藏数
        # cang_num=response.xpath("//span[contains(@class,'bookmark-btn')]/text()").extract()[0]
        # # print(type(cang_num))
        # cang_num=cang_num.strip().split(" ",1)[0]
        # if not re.findall(r"\d+\d*",cang_num):
        #     cang_num=0
        # # print(cang_num)
        # ping_num=response.xpath("//a[@href='#article-comment']/span/text()").extract()[0]
        # ping_num=ping_num.strip().split(" ",1)[0]
        # if not re.findall(r"\d+\d*",ping_num):
        #     ping_num=0
        # # print(ping_num)
        # #正文html
        # content=response.xpath("//div[@class='entry']").extract()[0]
        # # print(content)
        # #去掉评论的类别
        # tag_list=response.xpath("//p[@class='entry-meta-hide-on-mobile']/a/text()").extract()
        # tag_list=[x for x in tag_list if not x.strip().endswith("评论")]
        # tags=",".join(tag_list)
        img_urls=[]
        img_url=response.meta.get("img_url","")

        # # print(tag_list)
        # item["url"]=response.url
        # item["url_md5"]=get_md5(response.url)
        # item["img_url"]=[img_url]
        # item["title"] = title
        # #处理时间方便数据库插入
        # try:
        #     create_time=datetime.datetime.strptime(create_time,"%Y/%m/%d").date()
        # except Exception as e:
        #     create_time=datetime.datetime.now()
        # item["create_time"] = create_time
        # item["zan_num"] = zan_num
        # item["cang_num"] = cang_num
        # item["ping_num"] = ping_num
        # item["content"] = content
        # item["tags"] = tags

        item_loder=Jobboleloder(item=JobboleItem(),response=response)
        # item_loder.add_css()

        item_loder.add_value("url",response.url)
        item_loder.add_value("url_md5",get_md5(response.url))
        img_urls.append(img_url)
        item_loder.add_value("img_url", [img_urls])
        item_loder.add_xpath("title", "//div[@class='entry-header']/h1/text()")
        item_loder.add_xpath("create_time", "//p[@class='entry-meta-hide-on-mobile']/text()")
        item_loder.add_xpath("zan_num", "//span[contains(@class,'vote-post-up')]/h10/text()")
        item_loder.add_xpath("cang_num", "//span[contains(@class,'bookmark-btn')]/text()")
        item_loder.add_xpath("ping_num", "//a[@href='#article-comment']/span/text()")
        item_loder.add_xpath("content", "//div[@class='entry']")
        item_loder.add_xpath("tags", "//p[@class='entry-meta-hide-on-mobile']/a/text()")
        item=item_loder.load_item()
        yield item
