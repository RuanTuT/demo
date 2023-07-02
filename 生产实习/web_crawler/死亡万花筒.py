import requests  # 用来抓取网页的html源码
import random  # 取随机数
from bs4 import BeautifulSoup  # 用于代替正则式 取源码中相应标签中的内容
import sys
import time  # 时间相关操作


class downloader(object):
    def __init__(self):
        self.server = 'http://www.biqukan.com'
        self.target = 'http://www.biqukan.com/48_48010/'
        self.names = []  # 章节名
        self.urls = []  # 章节链接
        self.nums = 0  # 章节数

    """    获取html文档内容    """

    def get_content(self, url):
        header = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Connection': 'keep-alive',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-cn',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1 Safari/605.1.15'
        }
        timeout = random.choice(range(80, 180))
        while True:
            try:
                req = requests.get(url=url, headers=header, timeout=timeout)
                break
            except Exception as e:
                print('3', e)
                time.sleep(random.choice(range(8, 15)))
        return req.text

    """    获取下载的章节目录    """

    def get_download_catalogue(self, url):
        html = self.get_content(url)
        bf = BeautifulSoup(html, 'html.parser')
        texts = bf.find_all('div', {'class': 'listmain'})
        div = texts[0]
        a_s = div.find_all('a')
        self.nums = len(a_s[12:13])
        for each in a_s[12:13]:
            self.names.append(each.string)
            self.urls.append(self.server + each.get('href'))

    """    获取下载的具体章节  """

    def get_download_content(self, url):
        html = self.get_content(url)
        bf = BeautifulSoup(html, 'html.parser')
        texts = bf.find_all('div', {'class': 'showtxt', 'id': 'content'})
        text = texts[0].text.replace('\xa0' * 7, '\n\n')  # \xa0表示连续的空白格
        return text

    """    将文章写入文件    """


    def writer(self, name, path, text):
      write_flag = True
      with open(path, 'a', encoding='utf-8') as f:
        f.write(name + '\n')
        f.writelines(text)
        f.write('\n\n')


if __name__ == '__main__':
    dl = downloader()
    dl.get_download_catalogue(dl.target)
    for i in range(dl.nums):
        dl.writer(dl.names[i], '死亡万花筒.txt', dl.get_download_content(dl.urls[i]))
        print("已下载：%.2f%%" % float((i + 1) / dl.nums * 100) + '\r')
    print('下载完成！')
