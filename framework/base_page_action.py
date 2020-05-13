# coding=utf-8

import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import os.path
from framework.logger import Logger

# create a logger instance
logger = Logger(logger="BasePageAction").getlog()

class BasePageAction(object):
    """
        定义一个页面操作基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类
    """
    def __init__(self,driver):
        self.driver=driver


    def quit_browser(self):
        """
        quit browser and end testing
        :return: None
        """
        self.driver.quit()


    def forward(self):
        """
        浏览器前进操作
        :return: None
        """
        self.driver.forward()
        logger.info("Click forward on current page")


    def back(self):
        """
        浏览器后退操作
        :return: None
        """
        self.driver.back()
        logger.info("Click back on current page")


    def wait(self,seconds=10):
        """
        设置隐式等待
        :param seconds: 秒
        :return:
        """
        self.driver.implicity_wait(seconds)
        logger.info("Set implicitly wait %d seconds",seconds)


    def close(self):
        """
        点击关闭当前窗口
        :return:
        """
        try:
            self.driver.close()
            logger.info("Close and quit the browser")
        except NameError as e:
            logger.error("Failed to quit the browser : %s" % e)


    def get_windows_image(self):
        """
        在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹./reports/screenshots/下
        :return:
        """
        file_path=os.path.dirname(os.path.abspath('.'))+'/reports/screenshots/'
        rq=time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))
        image_name=file_path+rq+'.png'
        try:
            self.driver.get_screenshot_as_file(image_name)
            logger.info("Had take screenshot and save foler :/reports/screenshots/")
        except NameError as e:
            logger.error("Failed to take screenshot : %s" % e)


    def find_element(self,locator:str):
        element=None
        selector_by=locator.split("=",1)[0]
        selector_value=locator.split("=",1)[1]
        try:
            if selector_by in ("id","i"):
                element=self.driver.find_element_by_id(selector_value)
            elif selector_by in ("xpath","x"):
                element=self.driver.find_element_by_xpath(selector_value)
            elif selector_by in ("name","n"):
                element=self.driver.find_element_by_name(selector_value)
            elif selector_by in ("class_name","c"):
                element=self.driver.find_element_by_class_name(selector_value)
            elif selector_by in ("link_text", "l"):
                element = self.driver.find_element_by_link_text(selector_value)
            elif selector_by in ("partial_link_text", "p"):
                element = self.driver.find_element_by_partial_link_text(selector_value)
            elif selector_by in ("tag_name", "t"):
                element = self.driver.find_element_by_tag_name(selector_value)
            else:
                logger.error("\'%s\'is invalid! Please enter a valid type of targeting elements." % locator)
                raise NameError("Please enter a valid type of targeting elements.")
            logger.info("Had find element \'%s\' sucessful by %s with value: %s" % (element.text if element.text else locator, selector_by, selector_value))
            return element
        except NoSuchElementException as e:
            logger.error("NoSuchElementException: %s" % e)


    def find_elements(self,locator:str):
        elements=None
        selector_by=locator.split("=",1)[0]
        selector_value=locator.split("=",1)[1]
        try:
            if selector_by in ("id","i"):
                elements=self.driver.find_elements_by_id(selector_value)
            elif selector_by in ("xpath","x"):
                elements=self.driver.find_elements_by_xpath(selector_value)
            elif selector_by in ("name","n"):
                elements=self.driver.find_elements_by_name(selector_value)
            elif selector_by in ("class_name","c"):
                elements=self.driver.find_elements_by_class_name(selector_value)
            elif selector_by in ("link_text", "l"):
                elements = self.driver.find_elements_by_link_text(selector_value)
            elif selector_by in ("partial_link_text", "p"):
                elements = self.driver.find_elements_by_partial_link_text(selector_value)
            elif selector_by in ("tag_name", "t"):
                elements = self.driver.find_elements_by_tag_name(selector_value)
            else:
                logger.error("\'%s\'is invalid! Please enter a valid type of targeting elements." % locator)
                raise NameError("Please enter a valid type of targeting elements.")
            logger.info("Had find element \'%s\' sucessful by %s with value: %s" % (locator, selector_by, selector_value))
            return elements
        except NoSuchElementException as e:
            logger.error("NoSuchElementException: %s" % e)

    def input_text(self,locator: str, text):
        """
        输入框输入文本
        :param locator:元素定位表达式
        :param text:输入文本
        :return:
        """
        element=self.find_element(locator)
        element.clear()
        try:
            element.send_keys(text)
            logger.info("Had input \'%s\' in the inputBox" % text)
        except NameError as e:
            logger.error("Failed to input \'%s\' in the inputBox" % text)


    def clear(self,locator):
        """
        清除文本框
        :param locator: 元素定位表达式
        :return:
        """
        element=self.find_element(locator)
        try:
            element.clear()
            logger.info("Clear text sucess before the inputBox input")
        except NameError as e:
            logger.error("Failed to clear text of the inputBox with: %s" % e)


    def click(self,locator):
        """
        点击元素
        :param locator: 元素定位表达式
        :return:
        """
        element = self.find_element(locator)
        try:
            element.click()
            logger.info("The element \'%s\' is clicked" % locator)
        except NameError as e:
            logger.error("Failed to click the element whit: %s" % e)

    def click_element(self,element):
        try:
            element.click()
        except NameError as e:
            logger.error("Failed to click the element whit: %s" % e)

    def get_page_title(self):
        """
        获取页面标题
        :return: 页面标题
        """
        title=self.driver.title
        logger.info("Current page title is %s" % title)
        return title

    # 定位元素并且把鼠标悬停
    def hover_locator(self, locator):
        '''
        先根据locator定位元素，在将鼠标移动到定位的元素上
        :param locator:
        :return:
        '''
        element = self.find_element(locator)
        action=ActionChains(self.driver)
        action.move_to_element(element).perform()

    # 根据已知元素鼠标悬停
    def hover_element(self, element):
        '''
        将鼠标移动到已定位到的元素上面
        :param element: 定位到的元素
        :return:
        '''
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    def switch_to_new_handle(self):
        '''
        切换到最新的窗口
        :return:
        '''
        handles=self.driver.window_handles
        if len(handles)>1:
            self.driver.switch_to.window(handles[-1])
        else:
            self.driver.switch_to.window(handles[0])

    def switch_to_home_handle(self):
        '''
        切换到最早到窗口
        :return:
        '''
        handles=self.driver.window_handles
        self.driver.switch_to.window(handles[0])

    @staticmethod
    def sleep(seconds=1):
        time.sleep(seconds)
        logger.info("Sleep for %d seconds" % seconds)














