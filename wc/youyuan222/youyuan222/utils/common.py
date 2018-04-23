#常用函数模块化
import hashlib
def get_md5(url):
    #判断url是否是unicode码
    if isinstance(url,str):
        url=url.encode("utf-8")
    m=hashlib.md5()
    m.update(url)
    return m.hexdigest()#抽取摘要

if __name__=="__main__":
    print(get_md5("http://python.jobbole.com/all-posts/".encode("utf-8")))