import xlsxwriter
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup

url = 'https://tieba.baidu.com/f?kw=' + urllib.parse.quote('历史') + '&ie=utf-8&pn='
herders = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
    'Referer': 'https://tieba.baidu.com/', 'Connection': 'keep-alive'}
data = []


def getList(url):
    req = urllib.request.Request(url, headers=herders)
    response = urllib.request.urlopen(req)
    htmlText = response.read().decode("utf-8").replace("<!--", "").replace("-->", "")
    html = BeautifulSoup(htmlText, "lxml")
    thread_list = html.select(".j_thread_list")
    for thread in thread_list:
     title = thread.select(".j_th_tit")[0].get_text()
     author = thread.select(".frs-author-name")[0].get_text()
     time = thread.select(".is_show_create_time")[0].get_text()
     print(title)  # 打印标签
     data.append([title, author, time])


def getPage(url, p=50):
    for i in range(2):
        link = url + str(i * 50)
        getList(link)


def main():
    getPage(url, 50)


if __name__ == '__main__':
    main()
