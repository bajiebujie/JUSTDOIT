#! encoding:utf8
import datetime
import re
import sys
import time

import requests

reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append('..')
sys.path.append('../..')

from simi.logger.my_logger import MyLogger

from scrapy import Selector
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class SunriseSpider(object):
    def __init__(self):
        self._sunrise_dict = {}
        self._logger = MyLogger(__file__[:-3])
        self._logger.debug('init')

    def crawl_sunrise(self):
        driver = webdriver.PhantomJS()
        driver.get("https://richurimo.51240.com/beijing__richurimo/")
        WebDriverWait(driver, 10, 1, WebDriverException(msg='page not load complete')).until(
            expected_conditions.presence_of_element_located((By.ID, "richurimo_table")))
        body = driver.page_source
        s = Selector(text=body)
        trs = s.xpath("//table[@id='richurimo_table']/descendant-or-self::table/tbody/tr")
        for tr in trs[2:]:
            tds = tr.xpath("./td")
            date = tds[0].xpath('./text()').extract_first()
            sunrise = tds[1].xpath('./text()').extract_first()
            self._logger.debug('crawled date=%s, sunrise=%s' % (date, sunrise))
            m = re.search('([0-9]{4}.*?[0-9]{1,2}.*?[0-9]{1,2}.*?) .*', date)
            date = m.group(1)
            date = time.strftime('%Y%m%d', time.strptime(date, u'%Y年%m月%d日'))
            self._logger.debug(date)
            self._sunrise_dict[date] = sunrise
            # today = time.strftime('%Y%m%d')
            # print 'today=%s, sunrise=%s' % (today, sunrise_dict[today])

    def send_wx(self, watch):
        url = 'http://sc.ftqq.com/SCU7567T2d65fc431182df5c782b2dda07fff35a58f4112752201.send?text=sunrise&desp=%s' % watch
        self._logger.debug(url)
        requests.get(url)

    def start(self):
        self.crawl_sunrise()
        while True:
            try:
                now = datetime.datetime.now()
                today = now.strftime('%Y%m%d')
                watch = now.strftime('%H:%M')
                # watch = '04:45'
                self._logger.debug('today=%s, watch=%s' % (today, watch))
                if watch == '04:00':
                    self.crawl_sunrise()
                sunrise = self._sunrise_dict[today]
                self._logger.debug('sunrise=%s' % sunrise)
                if sunrise.startswith(watch):
                    self.send_wx(sunrise)
                time.sleep(60)
            except Exception as ex:
                self._logger.error(str(ex))


if __name__ == '__main__':
    SunriseSpider().start()
