# coding: utf-8

import socket


# 补全函数
def parsed_url(url):
    '''
    url 是字符串, 可能的值如下
    'g.cn'
    'g.cn/'
    'g.cn:3000'
    'g.cn:3000/search'
    'http://g.cn'
    'https://g.cn'
    'http://g.cn/'
    返回一个 tuple, 内容如下 (protocol, host, port, path)
    '''
    '''
    思路如下：
    1.protocol 协议字符串只有2种，http https ;有的按有的提取，没有的 按 http默认，然后拆分出来host以及其后所有字符串
    2.host 服务器字符串，分2种情况，没有'/' 使用find 查找返回 -1 ，有'/'的，按'/ 分离字符串'；分离出来g.cn:3000 以及 search
    3.path 服务器路径 = search
    4.port 判断，判断是否有’：‘  如果有，使用':'分离，后面的就是port，如果没有 就按protocol 走
    '''
    protocol = 'http'
    if url[:7] == 'http://':
        u = url.split('://')[1]
    elif url[:8] == 'https://':
        protocol = 'https'
        u = url.split('://')[1]
    else:
        u = url
    print(protocol, u)
    if u.find('/') == -1:
        host = u
        path = '/'
        print(host, path)
    else:
        host = u.split('/')[0]
        path = u.split('/')[1]
        print('----------1----------')
        print(host, path)
    port_dict = {
        'http': 80,
        'https': 433,
    }
    port = port_dict[protocol]
    print(port)
    if ':' in host:
        port = int(host.split(':')[1])
        host = host.split(':')[0]

    return protocol, host, port, path


# 5
# 把向服务器发送 HTTP 请求并且获得数据这个过程封装成函数
# 定义如下
def get(url):
    '''
    本函数使用上课代码 client.py 中的方式使用 socket 连接服务器
    获取服务器返回的数据并返回
    注意, 返回的数据类型为 bytes
    '''
    pass


# 测试程序
def test_parsed_url():
    http = 'http'
    https = 'https'
    host = 'g.cn'
    port = 80
    path = '/'
    test_items = [
        ('g.cn', (http, host, 80, path)),
        ('http://g.cn:5000', (http, host, 5000, path)),
        ('http://g.cn:5000/seclad', (http, host, 5000, 'seclad')),
    ]
    for t in test_items:
        url, expect = t
        u = parsed_url(url)
        print(u)
        e = 'parsed_url ERROR, ({}) ({}) ({})'.format(url, u, expect)
        assert u == expect, e


# 使用
def main():
    # url = 'http://movie.douban.com/top250'
    url = 'https://movie.douban.com'
    # r = get(url)
    # print(r)
    # print(parsed_url(url))
    test_parsed_url()


if __name__ == '__main__':
    main()
