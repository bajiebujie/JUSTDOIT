#! encoding: utf8
import logging
import sys
from logging.handlers import TimedRotatingFileHandler

reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append('..')
from logger.my_logger import MyLogger
from stream_logger import StreamLogger


def test1():
    log_file_prefix = __file__[:-3]
    DEFAULT_FORMAT = '[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d %(process)d] %(message)s'
    DEFAULT_DATE_FORMAT = '%y%m%d %H:%M:%S'
    formatter = logging.Formatter(fmt=DEFAULT_FORMAT, datefmt=DEFAULT_DATE_FORMAT)

    fileHandler = TimedRotatingFileHandler(log_file_prefix + "_app.log", when='midnight', interval=1, backupCount=3)
    fileHandler.setFormatter(formatter)

    logger = logging.root
    logger = logging.getLogger(log_file_prefix)
    logger.addHandler(fileHandler)
    logger.setLevel(logging.DEBUG)
    logger.debug('test log is ok?')

    sys.stdout = StreamLogger(logger)
    sys.stderr = StreamLogger(logger)

    print 'just print sth!'


def test2():
    my_logger = MyLogger(__file__[:-3])
    my_logger.debug('my_logger debug')


if __name__ == '__main__':
    test1()
    # test2()
