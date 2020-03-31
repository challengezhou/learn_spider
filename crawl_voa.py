#!/usr/bin/env python3

from lxml import etree
import req
import os


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
domain = 'https://www.51voa.com'


# prepare the document info which have translations and lyrics
def prepareInfo(url):
    r = req.get(url, headers=headers)
    html_str = r.text
    selector = etree.HTML(html_str)
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


# extract mp3 and lyric download url
def extract_download_link(selector):
    links = []
    mp3 = selector.xpath('//*[@id="mp3"]/@href')[0]
    lrc = selector.xpath('//*[@id="lrc"]/@href')[0]
    lrc = domain + lrc
    links.append(mp3)
    links.append(lrc)
    return links


def write_content(file_path, lines):
    with open(file_path, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line)
            f.write('\n\n')


def crawl(url, save_path):
    datas = prepareInfo(url)
    for info in datas:
        # english page href
        en_url = info['href']
        translation_url = en_url[:len(en_url)-5] + '_1.html'
        # jump to content page
        r = req.get(url=domain+en_url, headers=headers)
        en_content = r.text
        selector = etree.HTML(en_content)
        lines = extract_content(selector)
        # append refer url
        lines.append('en_url:{:s}\ntranslation_url:{:s}'.format(
            en_url, translation_url))
        download_links = extract_download_link(selector)
        for link in download_links:
            req.download(link, headers=headers, location=save_path)
        txt_file_path = os.path.join(
            save_path, download_links[0].rsplit('/', 1)[1][:-4] + '.txt')
        write_content(txt_file_path, lines)


if __name__ == "__main__":
    save_path = '/Users/zhoujian/Downloads/voa'
    for i in range(3, 10):
        url = 'https://www.51voa.com/Technology_Report_%d.html' % i
        crawl(url, save_path)
