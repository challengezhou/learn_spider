#!/usr/bin/env python36

import time
from baidu import extract_post_path, del_post

if __name__ == '__main__':
    print('delete begin', end=' ', flush=True)
    count = 0
    while count <= 30:
        post_path = extract_post_path()
        _l = len(post_path)
        for i, post_redirect_path in enumerate(post_path, start=1):
            r = del_post(post_redirect_path)
            if r['no'] != 0:
                count = 31
                print()
                print(r)
                break
            print(' . ', end=' ', flush=True)
            count += 1
            if i != _l:
                time.sleep(0.5)
    print('end')
    print('%s replies deleted' % count)
