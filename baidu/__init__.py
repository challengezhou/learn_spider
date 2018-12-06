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

from html_parser import extract_content
from header_parser import parse_to_dict
import requests
from urllib import parse

_del_post_body = {
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
# logged in Cookie,copy from chrome
headers = parse_to_dict('baidu')


def extract_post_path():
    u = 'http://tieba.baidu.com/i/i/my_reply'
    xpath = '//*[@id="content"]/div/ul/div[*]/div[2]//a[1][@class="b_reply"]/@href'
    _content = extract_content(u, xpath, headers)
    return _content


# /p/2306337473?fid=73787&pid=32282756735&cid=32282876564#32282876564
def parse_query(url):
    p = parse.urlparse(url)
    q = parse.parse_qs(p.query)
    return p.path[3:13], q.get('fid', 0), p.fragment


def del_post(post_redirect_path):
    a = parse_query(post_redirect_path)
    _del_post_body['fid'] = a[1]
    _del_post_body['tid'] = a[0]
    _del_post_body['pid'] = a[2]
    r = requests.post('https://tieba.baidu.com/f/commit/post/delete', headers=headers, data=_del_post_body)
    return r.json()
