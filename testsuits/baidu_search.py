# coding=utf-8
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobject.baidu_homepage import HomePage
from pageobject.baidu_news_home import BaiduNewsHomePage
from pageobject.baidu_sports_news_home import SprotsNewsHomePage

class BaiduSearch(unittest.TestCase):

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

    # @classmethod
    # def setUpClass(cls):
    #     """
    #     测试固件的setUp()的代码，主要是测试的前提准备工作，一个class中使用这种方式定义setUpClass()只会执行一次
    #     :return:
    #     """
    #     browse = BrowserEngine(cls)
    #     cls.driver = browse.open_browser(cls)
    #
    # @classmethod
    # def tearDownClass(cls):
    #     """
    #     测试结束后的操作，这里基本上都是关闭浏览器，一个class中使用这种方式定义tearDownClass()只会执行一次
    #     :return:
    #     """
    #     cls.driver.quit()

    def test_baidu_search(self):
        """
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。
        :return:
        """
        homepage=HomePage(self.driver)
        homepage.input_search_text("selenium")
        homepage.click_submit_btn()
        homepage.sleep(2)
        try:
            assert 'selenium' in homepage.get_page_title()
        except Exception  as e:
            print ('Test Fail.', format(e))

    def test_baidu_serach_python(self):
        homepage = HomePage(self.driver)
        homepage.input_search_text("python")
        homepage.click_submit_btn()
        homepage.sleep(2)
        homepage.get_windows_image()
        try:
            assert "python" in homepage.get_page_title()
        except Exception as e:
            print('Test Fail.', format(e))

    def test_view_nba_news(self):
        #初始化百度首页
        homepage=HomePage(self.driver)
        homepage.click_news()
        #初始化一个百度新闻主页对象
        newshome=BaiduNewsHomePage(self.driver)
        newshome.click_sports()
        sportnewhome=SprotsNewsHomePage(self.driver)
        sportnewhome.click_nba_link()
        time.sleep(2)
        sportnewhome.switch_to_new_handle()
        sportnewhome.get_windows_image()
        try:
            assert "NBA赛程表" in sportnewhome.get_page_title()
        except Exception as e:
            print('Test Fail.', format(e))
