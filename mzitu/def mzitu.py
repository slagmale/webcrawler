import requests
from bs4 import BeautifulSoup
import os


class mzitu():
    def __init__(self):
        self.headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
        }

    def request(self, url):
        content = requests.get(url, headers=self.headers)
        return content

    def all_url(self, url):
        html = requests.get(url)
        all_a = BeautifulSoup(html.text,'lxml').find('div', class_='all').find_all('a')
        all_a.pop(0)
        for a in all_a:
            title = a.get_text()
            print('开始保存:',title)
            path = str(title).replace('?','_')
            self.mkdir(path)
            href = a['href']
            self.html(href)

    # 处理套图地址获得图片地址
    def html(self,href):
        html = self.request(href)
        self.headers['referer'] = href
        max_span = BeautifulSoup(html.text, 'lxml').find('div', class_='pagenavi').find_all('span')[-2].get_text()
        for page in range(1, int(max_span) + 1):
            page_url = href + '/' + str(page)
            self.img(page_url)  ##调用img函数

    # 处理图片页面地址获得图片实际地址
    def img(self,page_url):
        img_html = self.request(page_url)
        img_url = BeautifulSoup(img_html.text, 'lxml').find('div', class_='main-image').find('img')['src']
        self.save(img_url)

    # 保存图片
    def save(self,img_url):
        name = img_url[-9:-4]
        img = self.request(img_url)
        f = open(name + '.jpg','ab')
        f.write(img.content)
        f.close()

    #创建文件夹
    def mkdir(self,path):
        path = path.strip()
        isExists = os.path.exists(os.path.join("D:\mzitu", path))
        if not isExists:
            #u:表示unicode字符串 中文, 必须表明所需编码, 否则一旦编码转换就会出现乱码。
            print(u'建了一个名字叫做', path, u'的文件夹！')
            os.makedirs(os.path.join("D:\mzitu", path))
            os.chdir(os.path.join("D:\mzitu", path))  ##切换到目录
            return True
        else:
            print(u'名字叫做', path, u'的文件夹已经存在了！')
            return False



Mzitu = mzitu() ##实例化
Mzitu.all_url('http://www.mzitu.com/all') ##给函数all_url传入参数  你可以当作启动爬虫（就是入口）
