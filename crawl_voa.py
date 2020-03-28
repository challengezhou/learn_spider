#!/usr/bin/env python3

import requests
# from lxml import etree

# xpath //*[@id="Right_Content"]/div[3]/ul/li

# <li><a href="/Technology_Report_1.html" target="_blank">[ Technology Report ] </a>  <a href="/VOA_Special_English/top-video-calling-apps-for-learning-work-and-social-connections-84179.html" target="_blank">Top Video Calling Apps for Learning, Work, Social Connections  (2020/3/26)</a></li>

def get_content():
    url = 'https://www.51voa.com/VOA_Special_English/'
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
    resp = requests.get(url, headers=headers, timeout=10)
    resp.encoding = resp.apparent_encoding
    return resp


if __name__ == "__main__":
    htmlStr = get_content().text
    print(htmlStr)
    # selector = etree.HTML(htmlStr)
    # lis = selector.xpath('//*[@id="Right_Content"]/div[3]/ul')
    # for li in lis:
    #     print(li)

