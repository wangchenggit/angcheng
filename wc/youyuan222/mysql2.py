#process_youyuan_mysql.py

# -*- coding: utf-8 -*-

import json
import redis
import pymysql

def main():
    # 指定redis数据库信息
    rediscli = redis.client.StrictRedis(host='127.0.0.1', port = 6379)
    # 指定mysql数据库
    mysqlcli = pymysql.connect(host='127.0.0.1', user='root', passwd='自己密码', db = 'jobboel', port=3306, use_unicode=True,charset="utf8")

    while True:
        # FIFO模式为 blpop，LIFO模式为 brpop，获取键值
        source, data = rediscli.blpop(["jobbole:items"])
        #由于断掉爬虫后会出现未爬的显示不是bytes类型判断一下数据库中content较长字段类型应改为:中text或longtext
        if isinstance(data,bytes):
            item = json.loads(data.decode('ascii'))

            # 使用cursor()方法获取操作游标
            cur = mysqlcli.cursor()
            # 使用execute方法执行SQL INSERT语句

            cur.execute("INSERT INTO jobbole(url, url_md5, img_url, img_path, title, create_time, zan_num, cang_num, ping_num,content,tags) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )", [item['url'], item['url_md5'], item['img_url'], item['img_path'], item['title'], item['create_time'], item['zan_num'], item['cang_num'], item['ping_num'],item['content'],item['tags']])
            # 提交sql事务
            mysqlcli.commit()
            #关闭本次操作
            cur.close()
            print ("inserted %s" % item['img_url'])
if __name__ == '__main__':
    main()



