# coding=utf-8
import unittest
from framework.browser_engine import BrowserEngine
from pageobject.baidu_homepage import HomePage

class GetPageTittle(unittest.TestCase):

    '''
    使用 def setUp(self): 方法定义固件执行用例时，有多个用例，每一个用例就要执行一次setUp()
    使用 如下方式则不同，有多个用例也只会执行一次setUpClass
    @classmethod
    def setUpClass(cls):
    '''
    def setUp(self):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作，一个class中使用这种方式定义setUp()会执行次数与泪中用例个数一致
        :return:
        """
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)

    def tearDown(self):
        """
        测试结束后的操作，这里基本上都是关闭浏览器，一个class中使用这种方式定义tearDown()会执行次数与泪中用例个数一致
        :return:
        """
        self.driver.quit()

    def test_get_baidu_tittle(self):
        homepage=HomePage(self.driver)
        tittle=homepage.get_page_title()
        assert tittle.startswith('百度一下')
