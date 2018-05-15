#! encoding:utf8
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append('..')

from scrapy import Selector
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from logger.my_logger import MyLogger

driver = webdriver.PhantomJS()
# driver.implicitly_wait(30)
driver.get("http://www.hotstar.com/channels/life-ok")
# WebDriverWait(driver, 10, 0.5, WebDriverException(msg='page not load complete')).until(
#     lambda driver: driver.execute_script('return document.readyState') == 'complete')
WebDriverWait(driver, 10, 1, WebDriverException(msg='page not load complete')).until(
    expected_conditions.presence_of_element_located((By.CLASS_NAME, "resClass")))
# time.sleep(3)
driver.execute_script('window.scrollTo(0,1000000)')
body = driver.page_source

s = Selector(text=body)
print s.xpath("//div[@class='resClass']/div/span/article/a/@href").extract()

my_logger = MyLogger(__file__[:-3])
my_logger.debug('debug sth')
print 'stdout sth'