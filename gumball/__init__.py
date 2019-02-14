from html_parser import extract_content

_u_wendao = 'http://bbs.leiting.com/forum-124-1.html'
_u_gumball = 'http://bbs.leiting.com/forum-288-1.html'
# 又要截图，又要id的~~
_u_dibao = 'http://bbs.leiting.com/forum-154-1.html'
_u_dongku = 'http://bbs.leiting.com/forum-166-1.html'

l_url = (_u_wendao,
         _u_gumball,
         # _u_dibao,
         _u_dongku)


def reward_post():
    xpath = '//*[@id="threadlisttableid"]/tbody[contains(@id,"normalthread")]//th/span[@class="xi1"]'
    for u in l_url:
        _content = extract_content(u, xpath)
        for i in _content:
            _url = i.xpath('./parent::*/a[2]/@href')[0]
            _name = i.xpath('./parent::*/a[2]/text()')[0]
            _score = i.xpath('./strong/text()'.strip())[0]
            yield _url, _name, _score


def detect_content(thread_url):
    c_xpath = '//td[contains(@id, "postmessage_")]'
    post_content = extract_content(thread_url, c_xpath)
    if 0 != len(post_content):
        _content = post_content[0].xpath('string(.)')
        return _content


def simple_content(content):
    _lines = []
    l_content = content.strip().split('\r\n')
    for _l in l_content:
        a_l = _l.replace('\n', ' ')
        _lines.append(a_l)
    return _lines


def generate_list():
    for _url, _name, _score in reward_post():
        if '寻宝任务' not in _name:
            _content = detect_content(_url)
            if _content:
                yield _url, _name, _score, 'contains' if '截图' in _content else 'no'
        else:
            yield _url, _name, _score, 'unknown'


if __name__ == '__main__':
    for url, name, score, contains in generate_list():
        print(url, name, score, contains)
