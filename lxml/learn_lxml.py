from lxml import etree
import os

base_url = 'https://www.51voa.com/'

datas = []


with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'new-pearl-jam-album-heavy-on-climate-activism-84192.html'), encoding='utf-8') as f:
    str = f.read()
    selector = etree.HTML(str)


def print_text(x):
    for t in x:
        print(t.text)

# xpath list
# title //*[@id="Right_Content"]/div[@class=title]
# content //*[@id="Right_Content"]/div[@class="Content"]

if __name__ == '__main__':
    # if use etree.HTML default add /html/body
    # lis = selector.xpath('//*[@id="Right_Content"]/div[3]/ul/li')
    # for li in lis:
    #     categroy = li.xpath('a[1]/text()')
    #     title = li.xpath('a[last()]/text()')
    #     href = li.xpath('a[last()]/@href')
    #     info = {}
    #     info['categroy'] = categroy
    #     info['href'] = href
    #     info['title'] = title
    #     print(info)
    title = selector.xpath('//*[@id="Right_Content"]/div[@class="title"]')
    print(title[0].xpath('string()'))
    content = selector.xpath('//*[@id="Right_Content"]/div[@class="Content"]/p')
    for p in content:
        print(p.xpath('string()'))
        print()
