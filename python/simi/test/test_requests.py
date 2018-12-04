#! encoding:utf8
import os
import sys
from collections import defaultdict
from multiprocessing import Process

import fire
import requests

reload(sys)
sys.path.append('..')
sys.path.append('../..')
from simi.logger.my_logger import MyLogger


class TestRequests(object):
    LOG_PREFIX = '%s_%s' % (__file__[:-3], os.getpid())
    my_logger = None

    def __init__(self, log_prefix=LOG_PREFIX):
        self.my_logger = MyLogger(log_prefix, stdout=False, stderr=False)

    def ping(self, url, count):
        status_dict = defaultdict(int)
        headers = {'user-agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
        for i in range(0, count):
            r = requests.get(url, headers=headers)
            self.my_logger.info('i=%s, url=%s, status_code=%s' % (i, url, r.status_code))
            status_dict[r.status_code] += 1
        self.my_logger.info(status_dict)

    # 'https://www.youtube.com/watch?v=fmR6evKDm4o'
    # 'http://v.youku.com/v_show/id_XMzc1NjA5Mjk5Ng==.html?spm=a2hww.11359951.m_26664.5~5!2~5~5~5~5!6~5~5~A'

    def start(self, url, count=1, process_count=1):

        process_list = []
        for i in range(0, process_count):
            process = Process(target=self.ping, args=(url, count))
            process_list.append(process)
            process.start()
        for process in process_list:
            process.join()

    print 'running...'


if __name__ == '__main__':
    fire.Fire(TestRequests)
