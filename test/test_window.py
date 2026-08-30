
from RobotFrameworkSelenium import RobotSeleniumBasic, RobotFrameworkSelenium



class Test_window:
    def test_01_multi_window(self):
        rfs = RobotFrameworkSelenium()
        rfs.selenium_init()
        rfs.selenium_create_webdriver()
        rfs.driver.get('http://www.baidu.com')
        rfs.driver.switch_to.new_window('tab')
        rfs.selenium_close_webdriver()
