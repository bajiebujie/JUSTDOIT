#! encoding: utf8
import bisect
import commands
import os
import subprocess
import sys

reload(sys)
sys.path.append('..')
sys.path.append('../..')

import fire
import numpy as np
import pandas as pd
import itertools

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

    def test_cmd(self):
        cmd = 'ls'
        ret = os.system(cmd)
        print ret
        output = os.popen(cmd)
        print output
        print output.read()
        status, output = commands.getstatusoutput(cmd)
        print status, output
        output = subprocess.check_output(cmd, shell=True)
        print output
        print '----- final -----'
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        p.wait()
        print p.pid
        print p.returncode, p.stdout.read(), p.stderr.read()

    def test_iter(self):
        data = np.random.randn(10)
        dates = pd.date_range('6/5/2018', periods=10)
        time_series = pd.Series(data, index=dates)

        for i, x in enumerate(data):
            print i, x

        # low opt in python2
        for date, x in zip(dates, data):
            print date, x

        for date, x in itertools.izip(dates, data):
            print date, x

        print
        # data_list = list(data)
        # data_list.append(100)
        # data_list.append(10000)
        print type(data)
        print data
        data = np.append(data, [111], axis=0)
        print data
        for date, x in itertools.izip_longest(dates, data):
            print date, x

    def test_bsearch(self):
        data = [1,3,5,7,9]
        pos = bisect.bisect_left(data, 0)
        print pos
        pos = bisect.bisect_left(data, 10)
        print pos
        pos = bisect.bisect_left(data, 3)
        print pos
        pos = bisect.bisect_left(data, 6)
        print pos



if __name__ == '__main__':
    fire.Fire(Test)
