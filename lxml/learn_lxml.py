from lxml import etree

with open('./test.html') as f:
    str = f.read()
    selector = etree.HTML(str)


def print_text(x):
    for t in x:
        print(t.text)


if __name__ == '__main__':
    # if use etree.HTML default add /html/body
    x1 = content = selector.xpath('/html/body/bookstore')
    for x in x1:
        print(x.tag)
    print(len(x1))
    x2 = content = selector.xpath('/html/body/bookstore/book[0]/title')
    print_text(x2)
    print(len(x2))
