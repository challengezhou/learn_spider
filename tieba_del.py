#!/usr/bin/env python36

"""
A util for delete all your tieba reply,because some main post is banned or deleted,you can't read it and just delete your reply

url:
my_reply  http://tieba.baidu.com/i/i/my_reply
post_redirect  like /p/2306337473?fid=73787&pid=32282756735&cid=32282876564#32282876564
xpath  //*[@id="content"]/div[3]/ul/div[*]/div[2]/span/a
delete_api  https://tieba.baidu.com/f/commit/post/delete

known resp:
success  {"no":0,"err_code":0,"error":null,"data":[]}
30/day limit  {"no":34,"err_code":220034,"error":null,"data":{"reason":30}}
"""

import requests
from urllib import parse
from lxml import etree
import time
from header_parser import parse_to_dict

# logged in Cookie,copy from chrome
header = parse_to_dict('baidu')

body = {
    "ie": "utf-8",
    "tbs": "c9152bc18f0d1f7a1543388967",  # unknown effect hardcode
    "fid": "73787",  # tieba id?  got from post_redirect_url
    "tid": "2351607199",  # main post id?  got from post_redirect_url
    "user_name": " 吹阴风点鬼火",
    "delete_my_post": " 1",
    "delete_my_thread": " 0",
    "is_vipdel": "0",
    "pid": "33263688200",  # your post id?  got from post_redirect_url
    "is_finf": "false"
}


def extract_post_path():
    r = requests.get('http://tieba.baidu.com/i/i/my_reply', headers=header)
    selector = etree.HTML(r.text)
    content = selector.xpath('//*[@id="content"]/div/ul/div[*]/div[2]//a[1][@class="b_reply"]/@href')
    return content


# /p/2306337473?fid=73787&pid=32282756735&cid=32282876564#32282876564
def parse_q(url):
    p = parse.urlparse(url)
    q = parse.parse_qs(p.query)
    return p.path[3:13], q.get('fid', 0), p.fragment


def del_t():
    r = requests.post('https://tieba.baidu.com/f/commit/post/delete', headers=header, data=body)
    return r.json()


def main():
    post_path = extract_post_path()
    _l = len(post_path)
    print('delete begin', end=' ', flush=True)
    for i, post_redirect_path in enumerate(post_path, start=1):
        a = parse_q(post_redirect_path)
        body['fid'] = a[1]
        body['tid'] = a[0]
        body['pid'] = a[2]
        r = del_t()
        if r['no'] != 0:
            print()
            print(r)
            break
        print(' . ', end=' ', flush=True)
        if i != _l:
            time.sleep(0.5)
        else:
            print('end')


if __name__ == '__main__':
    main()
