import time

from selenium import webdriver

print(__file__)
from RobotFrameworkSelenium import RobotSeleniumBasic, RobotFrameworkSelenium


class Rf1(RobotSeleniumBasic):
    pass


class Rf2(RobotFrameworkSelenium):
    pass


class Test_package:
    def test_01_package_available(self):
        rfs = RobotFrameworkSelenium()
        rsb = RobotSeleniumBasic()
        rf1 = Rf1()
        rf2 = Rf2()
        # rfs.selenium_init()
        # rfs.selenium_create_webdriver()
        # rfs.driver.get('http://www.baidu.com')
        # rfs.selenium_close_webdriver()
