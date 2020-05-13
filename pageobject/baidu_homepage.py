# coding=utf-8

from framework.base_page_action import BasePageAction

class HomePage(BasePageAction):
    #搜索框定位
    input_box="id=kw"
    #"百度一下"按钮定位
    search_submit_btn="id=su"
    #百度新闻入口定位
    news_link="xpath=//*[@name='tj_trnews']"
    # news_link="xpath=//*[@id='s-top-left']/a[1]"


    def input_search_text(self,text):
        self.input_text(self.input_box,text)

    def click_submit_btn(self):
        self.click(self.search_submit_btn)

    def click_news(self):
        self.click(self.news_link)
