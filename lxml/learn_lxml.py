from lxml import etree
import os

base_url = 'https://www.51voa.com/'

datas = []
info = {}

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'test.html')) as f:
    str = f.read()
    selector = etree.HTML(str)


def print_text(x):
    for t in x:
        print(t.text)


if __name__ == '__main__':
    # if use etree.HTML default add /html/body
    lis = selector.xpath('//*[@id="Right_Content"]/div[3]/ul/li')
    for li in lis:
        categroy = li.xpath('a[1]/text()')
        title = li.xpath('a[last()]/text()')
        href = li.xpath('a[last()]/@href')
        info.
        print('%s%s\nhref: %s' % (categroy[0], title[0], href[0]))
    
