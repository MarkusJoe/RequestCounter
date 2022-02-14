#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/2/12
# @File Name: __init__.py


import os
import hashlib
import sys
import requests
import threading


class MulThreadDownload(threading.Thread):
    """继承threading使用多线程"""
    def __init__(self, url, startpos, endpos, f, name):
        super(MulThreadDownload, self).__init__()
        self.session = requests.Session()
        self.session.trust_env = False
        self.url = url
        self.startpos = startpos
        self.endpos = endpos
        self.fd = f
        self.name = name

    def download(self):
        """
        多线程下载
        :return:
        """
        print(f'I: 线程: Thread-{self.name} 开始下载')
        headers = {"Range": "bytes=%s-%s" % (self.startpos, self.endpos)}
        res = self.session.get(self.url, headers=headers)
        self.fd.seek(self.startpos)
        self.fd.write(res.content)
        print(f'I: 线程: Thread-{self.name} 结束下载')

    def run(self):
        """
        此处启动
        :return:
        """
        self.download()


class Check:
    """检查md5是否相同和下载数据库"""
    def __init__(self):
        self.assets_url = 'https://themedatabases.vercel.app/assets'
        self.remote_md5 = 'https://themedatabases.vercel.app/md5'
        self.session = requests.Session()
        self.session.trust_env = False

    def check_md5(self):
        """
        检验本地文件md5是否和远程md5相同
        :return:
        """
        with open('./bin/assets/theme.db', 'rb') as fp:
            data = fp.read()
        local_md5 = hashlib.md5(data).hexdigest()
        remote_md5 = self.session.get(self.remote_md5).json()['data'][0]
        print(f'I: 本地数据库md5: {local_md5}\nI: 远程数据库md5: {remote_md5}')
        if local_md5 != remote_md5:
            print('E: 下载错误: 本地数据库md5和远程数据库md5检验不通过, 即将开始重新下载\nI: 本次下载将使用单线程下载')
            single_download(self.assets_url)
        else:
            print('I: md5检验已通过')

    def download(self):
        """
        开始下载
        :return:
        """
        filesize = int(self.session.head(self.assets_url).headers['Content-Length'])
        threaded_count = 3
        print(f'I: 数据库大小: {round(filesize / 1024 / 1024, 2)}Mb. 下载线程: {threaded_count}')
        threading.BoundedSemaphore(threaded_count)
        step = filesize // threaded_count
        mtd_list = []
        start = 0
        end = -1
        with open('./bin/assets/theme.db', 'w') as initial_file:
            initial_file.close()
        with open('./bin/assets/theme.db', 'rb+') as f:
            name = 1
            fileno = f.fileno()
            while end < filesize - 1:
                start = end + 1
                end = start + step - 1
                if end > filesize:
                    end = filesize
                dup = os.dup(fileno)
                fd = os.fdopen(dup, 'rb+', -1)
                t = MulThreadDownload(self.assets_url, start, end, fd, name)
                name += 1
                t.start()
                mtd_list.append(t)

            for i in mtd_list:
                i.join()

        self.check_md5()


def single_download(url):
    """
    单线程进行下载
    :param url:
    :return:
    """
    session = requests.Session()
    session.trust_env = False
    resp = session.get(url)
    print(f'I: 正在使用单线程下载中')
    with open('./bin/assets/theme.db', 'wb') as fp:
        fp.write(resp.content)
    print('I: 下载完成 正在检验文件md5')
    with open('./bin/assets/theme.db', 'rb') as fp:
        data = fp.read()
    local_md5 = hashlib.md5(data).hexdigest()
    remote_md5 = session.get('https://themedatabases.vercel.app/md5').json()['data'][0]
    print(f'I: 本地数据库md5: {local_md5}\nI: 远程数据库md5: {remote_md5}')
    if local_md5 != remote_md5:
        print('E: md5检验未通过请手动前往 https://themedatabases.vercel.app/assets 下载文件并放入./bin/assets文件夹内')
        sys.exit(-1)
    else:
        print('I: md5检验已通过')


if __name__ != '__main__':
    if not os.path.exists('./bin/assets/theme.db'):
        print('E: 没有检测到本地主题数据库即将开始下载')
        Check().download()
