#! encoding: utf8
import logging


class StreamLogger(object):
    def __init__(self, logger, log_level=logging.WARNING):
        self.logger = logger
        self.log_level = log_level

    def write(self, buf):
        for line in buf.rstrip().splitlines():
            self.logger.log(self.log_level, line.rstrip())

    def flush(self):
        for h in self.logger.handlers:
            h.flush()
