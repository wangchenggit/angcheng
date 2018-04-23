# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
#scrapy 提供许多文件处理方式
from scrapy.exporters import JsonItemExporter
import codecs
import json
import pymysql
import pymysql.cursors
from twisted.enterprise import adbapi


class Youyuan222Pipeline(object):
    def process_item(self, item, spider):
        return item
#处理图片
class JobboleImagesPipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
        image_file_paths=[]
        #重写pipline更改图片路径传回item
        for ok,value in results:
            image_file_path=value["path"]
            image_file_paths.append(image_file_path)
        item["img_path"]=image_file_paths

        return item
#自定义保存json 本地文件处理
class JsonWithEncodingPipeline(object):

    def __init__(self):
        self.file=codecs.open("youyuan.json","w",encoding="utf-8")#避免编码问题
    def process_item(self, item, spider):
        lines=json.dumps(dict(item),ensure_ascii=False)+"\n"
        self.file.write(lines)
        return item
    def spider_close(self,spider):
        self.file.close()
class JsonExporterPipPipeline(object):
    #调用scrapy的json exporter导出json文件还提供xml,csv
    def __init__(self):
        self.file=open("youyuanexporter.json","wb")
        self.exporter=JsonItemExporter(self.file,encoding="utf-8",ensure_ascii=False)
        self.exporter.start_exporting()
    def close_spider(self,spider):
        self.exporter.finish_exporting()
        self.file.close()
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
#同步数据库插入
class MysqlPipPipeline(object):
    def __init__(self):
        self.coon= pymysql.connect(host="localhost", user="root",password="123456", db="test", port=3307,charset="utf-8",use_unicode=True)


        # 使用cursor()方法获取操作游标
        self.cur = self.coon.cursor()

    def process_item(self, item, spider):
        insert_sql="""
                insert into
        """
        self.cur.execute(insert_sql,(item["title"],item["url"]))
        self.coon.commit()
#twisted异步插入数据库
class MysqltwistedPipPipeline(object):
    def __init__(self,dbpool):
        self.dbpool=dbpool
    @classmethod
    def form_settings(cls,settings):
        dbparms=dict(
            host=settings["MYSQL_HOST"],
            db=settings["MYSQL_DBNAME"],
            user = settings["MYSQL_USER"],
            passwd = settings["MYSQL_POSSWORD"],
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor,
            use_unicode=True,
        )
        #twisted连接池
        dbpool=adbapi.ConnectionPool("pymysql",**dbparms)
        return cls(dbpool)
    #执行插入操作
    def process_item(self, item, spider):
        query=self.dbpool.runInteraction(self.do_insert,item)
        query.addErrback(self.handle_error(),item,spider)
    #处理异步插入的异常,item,spider参数可有可不有
    def handle_error(self,failure,item,spider):
        print(failure)
    def do_insert(self, cursor, item):
        insert_sql = """
                insert into
        """
        cursor.execute(insert_sql, (item["title"], item["url"]))
