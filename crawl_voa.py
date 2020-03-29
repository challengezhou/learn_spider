#!/usr/bin/env python3


from lxml import etree
import req


# xpath //*[@id="Right_Content"]/div[3]/ul/li
# <li><a href="/Technology_Report_1.html" target="_blank">[ Technology Report ] </a>  <a href="/VOA_Special_English/top-video-calling-apps-for-learning-work-and-social-connections-84179.html" target="_blank">Top Video Calling Apps for Learning, Work, Social Connections  (2020/3/26)</a></li>

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}


def get_content():
    url = 'https://www.51voa.com/VOA_Special_English/'
    resp = req.req(url, headers=headers)
    return resp


if __name__ == "__main__":
    # htmlStr = get_content().text
    # selector = etree.HTML(htmlStr)
    # lis = selector.xpath('//*[@id="Right_Content"]/div[3]/ul/li')
    # datas = []
    # for li in lis:
    #     categroy = li.xpath('a[1]/text()')
    #     title = li.xpath('a[last()]/text()')
    #     href = li.xpath('a[last()]/@href')
    #     info = {}
    #     info['categroy'] = categroy
    #     info['href'] = href
    #     info['title'] = title
    #     datas.append(info)
    # print(datas)
    url = 'https://www.51voa.com/VOA_Special_English/new-pearl-jam-album-heavy-on-climate-activism-84192.html'
    r = req.req(url)
    with open('new-pearl-jam-album-heavy-on-climate-activism-84192.html', 'wb') as f:
        f.write(r.content)
