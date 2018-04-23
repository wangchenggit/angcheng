# -*- coding: utf-8 -*-
import os
# import scrapy
# Scrapy settings for youyuan222 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'youyuan222'

SPIDER_MODULES = ['youyuan222.spiders']
NEWSPIDER_MODULE = 'youyuan222.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'youyuan222 (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'youyuan222.middlewares.Youyuan222SpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'youyuan222.middlewares.Youyuan222DownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
SCHEDULER_PERSIST = True
REDIS_URL="redis://127.0.0.1@127.0.0.1:6379"
REDIS_START_URLS_KEY = '%(name)s:start_urls'
# REDIS_PASS = 'redisP@ssw0rd'
#图片存储
ITEM_PIPELINES = {
   'scrapy_redis.pipelines.RedisPipeline': 300,
   'youyuan222.pipelines.Youyuan222Pipeline': 300,
   # 'youyuan222.pipelines.JsonWithEncodingPipeline': 2,#自定义json本地化
   'youyuan222.pipelines.JsonExporterPipPipeline': 2,#scrapy提供的json本地化
   # 'youyuan222.pipelines.MysqlPipPipeline': 1,#mysql数据库插入
   # 'youyuan222.pipelines.MysqltwistedPipPipeline': 2,#数据库异步插入
    #图片管道
   # 'scrapy.pipelines.images.ImagesPipeline':1,
   'youyuan222.pipelines.JobboleImagesPipeline': 1,#自己定制处理图片的管道

}
IMAGES_URLS_FIELD="img_url"#与item进行连接字段
imgs_dir=os.path.abspath(os.path.dirname(__file__))#获取图片路径
IMAGES_STORE=os.path.join(imgs_dir,"images")#将下载的图片放入指定的位置
# #设置下载图片的宽高
# IMAGES_MIN_HEIGHT=100
# IMAGES_MIN_WIDTH=100
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
#
# MYSQL_HOST="127821"
# MYSQL_DBNAME="KUMING"
# MYSQL_USER="ROOT"
# MYSQL_POSSWORD="1271"
#
