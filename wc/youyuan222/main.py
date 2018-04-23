from scrapy.cmdline import execute
import sys
import os
#dirname获取父目录,abspath获取当前目录
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
print(123)
execute(["scrapy","crawl","jobbole"])