import requests
from lxml import etree


def extract_content(url, xpath, headers=None):
    try:
        r = requests.get(url, headers=headers, timeout=10)
    except requests.exceptions.ConnectionError as error:
        print('[ERROR] Call |%s| error msg:%s' % (url, error))
        return None
    selector = etree.HTML(r.text)
    content = selector.xpath(xpath)
    return content
