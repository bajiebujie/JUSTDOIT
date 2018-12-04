#! encoding:utf8
import json
import sys

import time

reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append('..')
sys.path.append('../..')

from scrapy import Selector
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from simi.logger.my_logger import MyLogger

driver = webdriver.PhantomJS()
# driver.implicitly_wait(30)
driver.get("https://play.google.com/store/apps/details?id=com.mxtech.videoplayer.ad&showAllReviews=true")
# WebDriverWait(driver, 10, 0.5, WebDriverException(msg='page not load complete')).until(
#     lambda driver: driver.execute_script('return document.readyState') == 'complete')
# WebDriverWait(driver, 10, 1, WebDriverException(msg='page not load complete')).until(
#     expected_conditions.presence_of_element_located((By.CLASS_NAME, "resClass")))
# time.sleep(3)
driver.execute_script('window.scrollTo(0,1000000)')
body = driver.page_source

s = Selector(text=body)
comment_divs = s.xpath("//div[@jsname='fk8dgd']/div/div/div[2]")
for comment_div in comment_divs:
    user = comment_div.xpath("./div[1]/div[1]/span/text()").extract_first()
    score = comment_div.xpath("./div[1]/div[1]/div/span[1]/div/div/@aria-label").extract_first()
    date = comment_div.xpath("./div[1]/div[1]/div/span[2]/text()").extract_first()
    comment = comment_div.xpath("./div[2]/span[2]/text()").extract_first()
    reply = comment_div.xpath("./div[3]/text()").extract_first()
    obj = {}
    obj['user'] = user
    obj['score'] = score
    obj['date'] = date
    obj['comment'] = comment
    obj['reply'] = reply
    data = json.dumps(obj)
    print(data)
    # print user
    # print score
    # print date
    # print comment
    # print reply

# print s.xpath("//div[@class='resClass']/div/span/article/a/@href").extract()

my_logger = MyLogger(__file__[:-3])
my_logger.debug('debug sth')
print 'stdout sth'

# screenshot
driver.get_screenshot_as_file('%s.png' % time.strftime("%y%m%d_%H%M%S"))
