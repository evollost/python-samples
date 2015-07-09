#-*-coding:utf-8-*-
'''
基本百度图片简单爬虫,直接正则采集,且未采用线程,队列等
1.爬取<img>标签内图片地址,存放于extra_img.txt
2.爬取搜索结果的展示前十页的图片地址,存放于real_img.txt
3.爬取所有<a>标签的地址信息,存放于a_href.txt
'''
import re
import urllib2

class BaiduImgSpider():
    def __init__(self):
        self.url = "http://pic.baidu.com/search/index?tn=baiduimage&ie=utf-8&word=%E6%B1%BD%E8%BD%A6"
        self.eimg = {}
        self.rimg = {}
        self.ahref = {}

    def get_page(self):
        try:
            page = urllib2.urlopen(self.url).read()
        except urllib2.URLError, e:
            if hasattr(e, "code"):                       
                print "The server couldn't fulfill the request."
                print "Error code: ", e.code
            elif hasattr(e, "reason"):
                print "Failed to reach the server."
                print "Reason: ", e.reason
        return page
    
    def find_a_href(self, page):
        '''
        舍弃href="#"以及href="javascript(...)"的结果
        '''
        pattern = re.compile(r'<a.*?href="((?!javascript:)(?!\#).*?)"')
        list_ahref = pattern.findall(page , re.S)
        self.ahref = set(list_ahref)
        save_result(self.ahref, "a_href.txt")
     
    def find_img_src(self, page):
        pattern = re.compile(r'<img.*?src="(.*?)"')
        list_imgsrc = pattern.findall(page, re.S)
        self.imgsrc = set(list_imgsrc)
        save_result(self.imgsrc, "extra_img.txt")
    
    def find_real_img(self, page):
        pattern = re.compile(r'"hoverURL":"(.*?)"')
        list_realimg = pattern.findall(page, re.S)
        self.realimg = set(list_realimg)
        save_result(self.realimg, "real_img.txt")

    def start_spider(self):
        page = self.get_page()
        self.find_a_href(page)
        self.find_img_src(page)
        self.find_real_img(page)

def save_result(data, name):
    file_name = name
    with open(file_name, 'w') as result_file:
        for element in data:
            result_file.write(element + '\n')

def main():
    spider = BaiduImgSpider()
    spider.start_spider()
    print "成功抓取href链接数: ", len(spider.ahref)
    print "成功抓取图片地址数: ", len(spider.imgsrc)
    print "成功抓取真实图片数: ", len(spider.realimg)

if __name__ == "__main__":
    main()
