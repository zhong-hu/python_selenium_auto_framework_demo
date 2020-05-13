# coding=utf-8

from framework.base_page_action import BasePageAction

class BaiduNewsHomePage(BasePageAction):
    #体育新闻入口定位
    sport_news="xpath=//a[@href='/sports']"

    def click_sports(self):
        elements=self.find_elements(self.sport_news)
        self.hover_element(elements[1])
        self.click_element(elements[1])