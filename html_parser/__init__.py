import requests
from lxml import etree


def extract_content(url, xpath, headers=None):
    r = requests.get(url, headers=headers, timeout=10)
    selector = etree.HTML(r.text)
    content = selector.xpath(xpath)
    return content
