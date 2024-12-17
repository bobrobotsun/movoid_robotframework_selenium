##################################################
# This is auto generated by code.
##################################################

import base64
import inspect
import math
import os
import cv2
import numpy as np
import robot
import selenium
import RobotFrameworkBasic
import robot.libraries.BuiltIn
import selenium.webdriver.chrome.webdriver
import typing
import selenium.webdriver.remote.webelement
import numpy
from Selenium2Library import Selenium2Library
from selenium.webdriver.common.action_chains import ActionChains

RUN: str
class BasicCommon(RobotFrameworkBasic.RobotBasic):
	def __init__(self):
		super().__init__()
		self.built: robot.libraries.BuiltIn.BuiltIn =  getattr(self, 'built', None)
		self.selenium_lib: Selenium2Library =  getattr(self, 'selenium_lib', None)
		self.driver: selenium.webdriver.chrome.webdriver.WebDriver =  getattr(self, 'driver', None)
		self.action_chains: ActionChains =  getattr(self, 'action_chains', None)
		self.screenshot_root: str =  getattr(self, 'screenshot_root', None)
		self.outer_coordinate: typing.Tuple[float] =  getattr(self, 'outer_coordinate', None)
		self.inner_coordinate: typing.Tuple[float] =  getattr(self, 'inner_coordinate', None)
		self.window_x: float =  getattr(self, 'window_x', None)
		self.window_y: float =  getattr(self, 'window_y', None)
	def selenium_init(self, screenshot_log: bool = False, _return_when_error = None, _log_keyword_structure = True, _return_name = None):
		"""
		:param screenshot_log: 是否将截屏默认放在log中
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		"""
		...
	def selenium_analyse_locator(self, locator: str, _return_when_error = None, _log_keyword_structure = True, _return_name = None) -> typing.Tuple[str, str]:
		"""
		将locator文本解析为by,path，方便find element
		:param locator: 合并的locator
		:return:
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		"""
		...
	def selenium_find_elements_by_locator(self, locator, _return_when_error = None, _log_keyword_structure = True, _return_name = None) -> typing.List[selenium.webdriver.remote.webelement.WebElement]:
		"""
		:param locator: by=path
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		"""
		...
	def selenium_find_element_by_locator(self, locator, _return_when_error = None, _log_keyword_structure = True, _return_name = None) -> selenium.webdriver.remote.webelement.WebElement:
		"""
		:param locator: by=path
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		"""
		...
	def selenium_execute_js_script(self, js_code: str, args, _return_when_error = None, _log_keyword_structure = True, _return_name = None) -> typing.Any:
		"""
		:param js_code: javascript脚本文本
		:param args: 其他相应的参数
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		"""
		...
	def analyse_color_function(self, color_function, _return_when_error = None, _log_keyword_structure = True, _return_name = None) -> typing.Callable[[int, int, int], bool]:
		"""
		:param color_function: 输入的符号+数值，例如 >60,>60,>60
		:return: 相应的判定函数
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		"""
		...
	def exchange_list3_to_color_function(self, formula_list, _return_when_error = None, _log_keyword_structure = True, _return_name = None) -> typing.Callable[[int, int, int], bool]:
		"""
		:param formula_list: 已经解析清晰的列表
		:return: 相应的判定函数
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		"""
		...
	def selenium_get_full_screenshot_path(self, screenshot_name, _return_when_error = None, _log_keyword_structure = True, _return_name = None) -> str:
		"""
		:param screenshot_name: 截图存储文件夹名
		:return: 截屏文件夹全路径
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		"""
		...
	def selenium_cut_screenshot(self, screenshot_locator = None, image_name = 'element-cut-image.png', _return_when_error = None, _log_keyword_structure = True, _return_name = None):
		"""
		:param screenshot_locator: 截图目标，不输入则全浏览器截屏
		:param image_name: 存储的文件名称
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		"""
		...
	def selenium_take_screenshot(self, screenshot_locator = None, image_name = 'python-screenshot.png', rename = True, _return_when_error = None, _log_keyword_structure = True, _return_name = None):
		"""
		:param screenshot_locator: 截图目标，不输入则全浏览器截屏
		:param image_name: 存储的文件名称
		:param rename: 如果重名了，是否通过增加序号的方式重命名
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		"""
		...
	def selenium_log_screenshot(self, screenshot_locator = None, _return_when_error = None, _log_keyword_structure = True, _return_name = None) -> numpy.ndarray:
		"""
		:param screenshot_locator: 截图目标，不输入则全浏览器截屏
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		"""
		...
	def selenium_log_screenshot_path(self, screenshot_name, _return_when_error = None, _log_keyword_structure = True, _return_name = None) -> None:
		"""
		:param screenshot_name: 截图存储文件夹名称
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		"""
		...
	def selenium_analyse_image(self, image, _return_when_error = None, _log_keyword_structure = True, _return_name = None):
		"""
		:param image: 目标图片的路径
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		"""
		...
	def selenium_analyse_element(self, locator: typing.Union[selenium.webdriver.remote.webelement.WebElement, str], _return_when_error = None, _log_keyword_structure = True, _return_name = None) -> selenium.webdriver.remote.webelement.WebElement:
		"""
		:param locator: locator或者element
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		"""
		...
	def selenium_analyse_elements(self, locator: typing.Union[typing.List[selenium.webdriver.remote.webelement.WebElement], str], _return_when_error = None, _log_keyword_structure = True, _return_name = None) -> typing.List[selenium.webdriver.remote.webelement.WebElement]:
		"""
		:param locator: locator或者elements
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		"""
		...
	def selenium_debug_teardown(self, function, args, kwargs, re_value, error, trace_back, has_return):	...
	...

