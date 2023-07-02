import os
import requests
import urllib3


class BDTB:  # 百度贴吧爬虫类
    # 初始化&#xff0c;传入基地址&#xff0c;是否只看楼主的参数
    def __init__(self, baseUrl, seeLZ):
        self.baseURL = baseUrl
        self.seeLZ = '?see_lz=' + str(seeLZ)

    # 传入页码&#xff0c;获取该页帖子的代码
    def getPage(self, pageNum):
        http = urllib3.PoolManager()
        url = self.baseURL + self.seeLZ + '&pn=' + str(pageNum * 50)
        for i in range(0, pageNum):
            params = {
                'ie': 'utf-8',
                'kw': '%E6%95%B0%E5%AD%A6%E5%88%86%E6%9E%90',
                'pn': str(i * 50)
            }
            response = requests.get(url)
            with open('./百度贴吧/历史吧/历史吧第%s页.html' % (i + 1), 'w', encoding='utf-8') as file:
                file.write(response.content.decode('utf-8'))
    # return


baseURL = 'https://tieba.baidu.com/f?ie=utf-8&kw=%E6%95%B0%E5%AD%A6%E5%88%86%E6%9E%90'
dirname = './百度贴吧/历史吧/'
pageNum = 1
bDTB=BDTB(baseURL,True);
if not os.path.exists(dirname):
    os.makedirs(dirname)
bDTB.getPage(1)