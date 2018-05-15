#! encoding: utf8
import logging
import sys
from logging.handlers import TimedRotatingFileHandler

from stream_logger import StreamLogger


class MyLogger(object):
    _logger = None

    def __init__(self, log_file_prefix=__file__[:-3], stdout=False, stderr=False):
        DEFAULT_FORMAT = '[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d %(process)d] %(message)s'
        DEFAULT_DATE_FORMAT = '%y%m%d %H:%M:%S'
        formatter = logging.Formatter(fmt=DEFAULT_FORMAT, datefmt=DEFAULT_DATE_FORMAT)
        fileHandler = TimedRotatingFileHandler(log_file_prefix + "_app.log", when='midnight', interval=1, backupCount=3)
        fileHandler.setFormatter(formatter)
        self._logger = logging.getLogger(log_file_prefix)
        self._logger.addHandler(fileHandler)
        self._logger.setLevel(logging.DEBUG)
        if stdout:
            sys.stdout = StreamLogger(self._logger)
        if stderr:
            sys.stderr = StreamLogger(self._logger)

    def debug(self, msg, *args, **kwargs):
        self._logger.debug(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        self._logger.info(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        self._logger.warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self._logger.error(msg, *args, **kwargs)


def test():
    my_logger = MyLogger(__file__[:-3], stdout=True, stderr=True)
    my_logger.debug('debug sth')
    my_logger.info('info sth')
    my_logger.warning('warning sth')
    my_logger.error('error sth')
    print 'print sth'
    sys.stderr.write('stderr sth')


if __name__ == '__main__':
    test()
