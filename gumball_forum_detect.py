#!/usr/bin/env python36

from gumball import reward_post, detect_content


if __name__ == '__main__':
    for _url, _name, _score in reward_post():
        _content = detect_content(_url)
        print(_url, _name, _score, 'contains' if _content.count('截图') else '')