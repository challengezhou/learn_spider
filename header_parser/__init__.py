import os


def parse_to_dict(name):
    _dict = {}
    with open(os.path.dirname(os.path.realpath(__file__)) + '/' + name +'_header_pairs.txt') as f:
        _str = f.read()
        if _str:
            _str_s = _str.strip()
            _ls = _str_s.split('\n')
            for i in _ls:
                if i.count(':') == 0:
                    continue
                _lls = i.split(':', 1)
                if len(_lls) == 2:
                    _dict[_lls[0]] = _lls[1].strip()
            return _dict


if __name__ == '__main__':
    print(parse_to_dict('baidu'))
