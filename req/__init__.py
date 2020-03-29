import requests


def req(url, headers=None, body=None, method='GET', timeout=10):
    try:
        if method.upper() == 'GET':
            r = requests.get(url, headers=headers, timeout=timeout)
        else:
            r = requests.post(url, json=body, headers=headers, timeout=timeout)
        r.encoding = r.apparent_encoding
    except requests.RequestException as error:
        print('[ERROR] Call |%s| error msg:%s' % (url, error))
        raise error
    return r


def download(url, headers=None, filename='temp.mp3'):
    r = req(url, headers)
    with open(filename, 'wb') as f:
        f.write(r.content)
    print(r.headers)


if __name__ == '__main__':
    mp3 = 'https://files.21voa.com/202003/new-pearl-jam-album-heavy-on-climate-activism.mp3'
    download(mp3)