#! encoding: utf8
import sys

reload(sys)
sys.path.append('..')
sys.path.append('../..')

import fire

from simi.logger.my_logger import MyLogger
from simi.util.load_monitor import LoadMonitor
from simi.util.misc import get_host_ip


class Test(object):
    def test_get_host_ip(self):
        print 'test_get_host_ip'
        print get_host_ip()

    def test_load_monitor(self):
        print 'test_load_monitor'
        load_monitor = LoadMonitor()
        load_monitor.start()

    def test_my_logger(self):
        my_logger = MyLogger(__file__[:-3])
        my_logger.debug('my_logger debug')

    def test_all(self):
        self.test_get_host_ip()
        self.test_load_monitor()
        self.test_my_logger()


if __name__ == '__main__':
    fire.Fire(Test)
