#  coding=utf-8
import unittest,os,sys
import time
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# from testsuits.baidu_search import BaiduSearch
# from testsuits.test_get_page_title import GetPageTittle
from HTMLTestRunner import HTMLTestRunner
if __name__ == '__main__':
    # print(os.path.curdir)
    # testsuits=unittest.TestSuite(unittest.makeSuite(BaiduSearch))
    testsuits=unittest.TestLoader().discover("testsuits")
    # testsuits.addTests(map(BaiduSearch,["test_baidu_search","test_baidu_serach_python"]))
    # testsuits.addTest(GetPageTittle("test_get_baidu_tittle"))
    report_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"/reports/"
    print(report_path)
    now=time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
    HtmlFile = report_path + now + "HTMLtemplate.html"
    with open(HtmlFile, "w",encoding='utf-8') as fp:
        runner=HTMLTestRunner(stream=fp,description="用例运行情况",title="框架练习测试报告")
        runner.run(testsuits)

