# coding=utf-8
from framework.base_page_action import BasePageAction

class SprotsNewsHomePage(BasePageAction):
    #NBA赛程定位
    nba_link="xpath=//*[@class='schedule clearfix']//li[1]/a"

    def click_nba_link(self):
        self.click(self.nba_link)
        self.sleep(3)
