import requests
import time
import os


def get(url, headers=None, body=None, timeout=10):
    try:
        r = requests.get(url, headers=headers, timeout=timeout)
        r.encoding = r.apparent_encoding
    except requests.RequestException as error:
        print('[ERROR] Call |%s| error msg:%s' % (url, error))
        raise error
    return r


def download(url, headers=None, location='.', filename=None):
    if not filename:
        filename = url.rsplit('/', 1)[1]
    try:
        r = requests.get(url, headers=headers, stream=True)
    except requests.RequestException as error:
        print('[ERROR] Call |%s| error msg:%s' % (url, error))
        raise error
    print('download [{:s}] begin [{:s}] =>   0.00%'.format(
        filename, time.strftime('%H:%M:%S')), end='', flush=True)
    length = int(r.headers['content-length'])
    now = 0
    begin = time.time()
    with open(os.path.join(location, filename), 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                now += len(chunk)
                f.write(chunk)
                now_percent = formatPercent(now/length)
                print('\b'*7 + now_percent, end='', flush=True)
        print('  finished!')


def formatPercent(num):
    if not num:
        num = 0
    percent = num * 100
    return '{:6.2f}%'.format(percent)


if __name__ == '__main__':
    mp3 = 'https://files.21voa.com/202003/new-pearl-jam-album-heavy-on-climate-activism.mp3'
    download(mp3)
