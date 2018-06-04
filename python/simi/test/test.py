#! encoding: utf8
import commands
import os
import subprocess
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
        print p.returncode, p.stdout.read(), p.stderr.read()


if __name__ == '__main__':
    fire.Fire(Test)
