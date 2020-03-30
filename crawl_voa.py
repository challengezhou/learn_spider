#!/usr/bin/env python3


from lxml import etree
import req
import os


# xpath //*[@id="Right_Content"]/div[3]/ul/li
# <li><a href="/Technology_Report_1.html" target="_blank">[ Technology Report ] </a>  <a href="/VOA_Special_English/top-video-calling-apps-for-learning-work-and-social-connections-84179.html" target="_blank">Top Video Calling Apps for Learning, Work, Social Connections  (2020/3/26)</a></li>

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
domain = 'https://www.51voa.com'


def get_content():
    url = 'https://www.51voa.com/Technology_Report_9.html'
    resp = req.get(url, headers=headers)
    return resp


# prepare the document info which have translation and lyric
def prepareLink():
    htmlStr = get_content().text
    selector = etree.HTML(htmlStr)
    lis = selector.xpath('//*[@id="Right_Content"]/div[3]/ul/li')
    datas = []
    for li in lis:
        yi = li.xpath('img[2]')
        if len(yi) > 0:
            categroy = li.xpath('a[1]/text()')[0]
            title = li.xpath('a[last()]/text()')[0]
            href = li.xpath('a[last()]/@href')[0]
            info = {}
            info['categroy'] = categroy
            info['href'] = href
            info['title'] = title
            datas.append(info)
    return datas


def extract_content(selector):
    lines = []
    title_path = selector.xpath(
        '//*[@id="Right_Content"]/div[@class="title"]')[0]
    title = title_path.xpath('string()')
    lines.append('##' + title)
    byline_path = selector.xpath(
        '//*[@id="Right_Content"]/div[@class="Content"]/span[1]')[0]
    byline = byline_path.xpath('string()')
    dateline_path = selector.xpath(
        '//*[@id="Right_Content"]/div[@class="Content"]/span[2]')[0]
    dateline = dateline_path.xpath('string()')
    lines.append(byline + '  ' + dateline)
    en_content_path = selector.xpath(
        '//*[@id="Right_Content"]/div[@class="Content"]/p')
    for p in en_content_path:
        line = p.xpath('string()')
        lines.append(line)
    return lines

if __name__ == "__main__":
    location = 'D:\\download\\voa'
    datas = prepareLink()
    for info in datas:
        main_title = info['title']
        # english page href
        en_url = info['href']
        translation_url = en_url[:len(en_url)-5] + '_1.html'
        r = req.get(url=domain+en_url, headers=headers)
        en_content = r.text
        selector = etree.HTML(en_content)
        lines = extract_content(selector)
        lines.append('en_url:{:s}\ntranslation_url:{:s}'.format(en_url, translation_url))
        mp3 = selector.xpath('//*[@id="mp3"]/@href')[0]
        lrc = selector.xpath('//*[@id="lrc"]/@href')[0]
        req.download(mp3, headers=headers, location=location)
        req.download(domain + lrc, headers=headers, location=location)
        txt_file = os.path.join(location, mp3.rsplit('/', 1)[1][:-4] + '.txt')
        with open(txt_file, 'w', encoding='utf-8') as f:
            for line in lines:
                f.write(line)
                f.write('\n\n')
