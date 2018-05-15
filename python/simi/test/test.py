#! encoding: utf8
import sys

import fire

reload(sys)
sys.path.append('..')
sys.path.append('../..')
from simi.util.misc import get_host_ip


class Test(object):
    def test_get_host_ip(self):
        print 'test_get_host_ip'
        print get_host_ip()


print 'test'
if __name__ == '__main__':
    print '__main__'
    fire.Fire(Test)
