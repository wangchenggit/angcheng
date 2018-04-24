# angcheng
python
1此项目为伯乐在线的scrapy分布式,线下实测数据没问题,redis和mysql也成功入库
2相关环境配置在requirement文件中,只多不少,文件实在项目环境(最好有镜像的情况下)中一条命令生成
            生成命令:pip freeze >requirements.txt
            解压成环境:pip install -r requirements.txt
            原文引自:https://blog.csdn.net/loyachen/article/details/52028825
3本项目核心是:scrapy-redis借用了redis请求队列管理(queue),ulr去重(指纹文件)不做坠述
            scrapy图片下载,json序列化,loder机制
            redis主从同步分布多机ip
            mysql转存redis数据减轻内存压力亲测适用其他项目
其他就不多说了请看代码注释
