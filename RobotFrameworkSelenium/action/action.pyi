##################################################
# This is auto generated by code.
##################################################

import os
import pathlib
import re
import time
import cv2
import numpy as np
import RobotFrameworkSelenium.common
import typing
import numpy
import selenium.webdriver.remote.webelement

class SeleniumAction(RobotFrameworkSelenium.common.BasicCommon):
	def __init__(self):
		super().__init__()
		self._check_element_attribute_change_value: typing.Union[str, None] =  None
		self._check_element_count_value: typing.Union[int, None] =  None
	def selenium_take_full_screenshot(self, screenshot_name = 'python-screenshot.png', _return_when_error = None, _log_keyword_structure = True, _return_name = None):
		"""
		全窗口截屏，并保存文件
		:param screenshot_name: 截图名曾
		:return: (截图名称,截图路径) or cv全图片信息
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		"""
		...
	def selenium_click_element(self, click_locator, operate = 'click', _return_when_error = None, _log_keyword_structure = True, _return_name = None) -> bool:
		"""
		点击某个元素，可以双击
		:param click_locator:点击元素的位置，可以使用locator或者Element
		:param operate: 默认为点击，输入 doubleclick 可以双击
		:return:
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		"""
		...
	def selenium_get_element_color_list(self, screenshot_locator = None, _return_when_error = None, _log_keyword_structure = True, _return_name = None) -> numpy.ndarray:
		"""
		获得目标元素的颜色列表
		:param screenshot_locator: 目标元素或其locator。
		:return: 一个x*y*3的ndarray
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		"""
		...
	def selenium_click_element_with_offset(self, click_locator, x = 0, y = 0, operate = 'click', _return_when_error = None, _log_keyword_structure = True, _return_name = None) -> bool:
		"""
		选择某个元素相对中心偏移一定距离的位置进行点击
		:param click_locator: 目标元素或者locator
		:param x: 横坐标像素数
		:param y: 纵坐标像素数
		:param operate: 默认点击，doubleclick为双击
		:return: True
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		"""
		...
	def selenium_check_element_attribute(self, check_locator, check_value, check_attribute = 'innerText', attribute_type = '', regex: bool = True, check_bool: bool = True, _return_when_error = None, _log_keyword_structure = True, _return_name = None):
		"""
		检查目标元素的属性是否满足某个条件
		:param check_locator: 检查目标的元素或locator
		:param check_value: 属性值
		:param check_attribute: 属性名
		:param attribute_type: 属性的类型，默认三个类型均搜索，可以输入以下其中之一：attribute、property、dom
		:param regex: 属性值是否为一个正则公式，默认为正则，如果输入False，那么需要属性值完全匹配
		:param check_bool: 是否为满足条件，默认为找到满足条件的元素。如果输入False，那么需要找到目标元素存在一个不满足条件的
		:return: 判定结果
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		"""
		...
	def selenium_find_elements_with_attribute(self, find_locator, find_value = '', find_attribute = 'innerText', attribute_type = '', regex = True, check_bool = True, _return_when_error = None, _log_keyword_structure = True, _return_name = None) -> typing.List[selenium.webdriver.remote.webelement.WebElement]:
		"""
		在所有目标元素中，寻找所有属性值满足需求的元素，并返回
		:param find_locator: 搜索目标元素或locator
		:param find_value: 所需要匹配的属性值
		:param find_attribute: 所需要寻找的属性
		:param attribute_type: 属性的类型，默认三个类型均搜索，可以输入以下其中之一：attribute、property、dom
		:param regex: 属性值是否为一个正则公式，默认为正则，如果输入False，那么需要属性值完全匹配
		:param check_bool: 是否为满足条件，默认为找到满足条件的元素。如果输入False，那么需要找到目标元素存在一个不满足条件的
		:return:
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		"""
		...
	def selenium_find_element_with_attribute(self, find_locator, find_value = '', find_attribute = 'innerText', attribute_type = '', regex = True, check_bool = True, _return_when_error = None, _log_keyword_structure = True, _return_name = None) -> selenium.webdriver.remote.webelement.WebElement:
		"""
		在所有目标元素中，寻找第一个属性值满足需求的元素，并返回
		:param find_locator: 搜索目标元素或locator
		:param find_value: 所需要匹配的属性值
		:param find_attribute: 所需要寻找的属性
		:param attribute_type: 属性的类型，默认三个类型均搜索，可以输入以下其中之一：attribute、property、dom
		:param regex: 属性值是否为一个正则公式，默认为正则，如果输入False，那么需要属性值完全匹配
		:param check_bool: 是否为满足条件，默认为找到满足条件的元素。如果输入False，那么需要找到目标元素存在一个不满足条件的
		:return: 寻找到的满足要求的元素
		:raise RfError:如果没有满足要求的元素，那么会抛出
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		"""
		...
	def selenium_get_locator_attribute(self, target_locator, target_attribute = 'innerText', attribute_type = '', _return_when_error = None, _log_keyword_structure = True, _return_name = None) -> typing.Any:
		"""
		获取目标元素的属性的值
		:param target_locator: 目标元素或locator
		:param target_attribute: 属性名称
		:param attribute_type: 属性的类型，默认三个类型均搜索，可以输入以下其中之一：attribute、property、dom
		:return:
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		"""
		...
	def selenium_new_screenshot_folder(self, _return_when_error = None, _log_keyword_structure = True, _return_name = None):
		"""
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		"""
		...
	def selenium_delete_elements(self, delete_locator, _return_when_error = None, _log_keyword_structure = True, _return_name = None) -> None:
		"""
		在页面上把某个/些元素删除掉
		:param delete_locator: 待删除的元素或locator
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		"""
		...
	def selenium_check_contain_element(self, check_locator, check_exist: bool = True, _return_when_error = None, _log_keyword_structure = True, _return_name = None) -> bool:
		"""
		检查页面内是否存在某个元素
		:param check_locator: 目标元素或locator
		:param check_exist: 默认检查存在。改为False后，改为检查页面中是否不存在这个元素
		:return: 搜素结果
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		"""
		...
	def selenium_check_contain_elements(self, check_locator, check_count: int = 1, _return_when_error = None, _log_keyword_structure = True, _return_name = None) -> bool:
		"""
		检查页面内某些元素的总数是否为特定的值
		:param check_locator: 目标元素或locator
		:param check_count: 元素的数量
		:return: 搜索结果。只有正好数量相同才会返回True
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		"""
		...
	def selenium_check_element_attribute_change_init(self, check_locator, check_attribute = 'innerText', attribute_type = '', _return_when_error = None, _log_keyword_structure = True, _return_name = None) -> bool:
		"""
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		"""
		...
	def selenium_check_element_attribute_change_loop(self, check_locator, check_attribute = 'innerText', attribute_type = '', _return_when_error = None, _log_keyword_structure = True, _return_name = None) -> bool:
		"""
		:param check_locator: 待检查的元素或locator
		:param check_attribute: 检查的目标属性名
		:param attribute_type: 属性的类型，默认三个类型均搜索，可以输入以下其中之一：attribute、property、dom
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		"""
		...
	def selenium_check_element_count_change_init(self, check_locator, _return_when_error = None, _log_keyword_structure = True, _return_name = None) -> bool:
		"""
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		"""
		...
	def selenium_check_element_count_change_loop(self, check_locator, _return_when_error = None, _log_keyword_structure = True, _return_name = None) -> bool:
		"""
		:param check_locator: 待检查的元素或locator
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		"""
		...
	def selenium_check_stable_element_attribute_unchanged_init(self, check_locator, check_attribute = 'innerText', _return_when_error = None, _log_keyword_structure = True, _return_name = None) -> bool:
		"""
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		"""
		...
	def selenium_check_stable_element_attribute_unchanged_loop(self, check_locator, check_attribute = 'innerText', _return_when_error = None, _log_keyword_structure = True, _return_name = None) -> bool:
		"""
		:param check_locator: 待检查的元素或locator
		:param check_attribute: 检查的目标属性名
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		"""
		...
	def always_true(self, _return_when_error = None, _log_keyword_structure = True, _return_name = None) -> bool:
		"""
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		"""
		...
	...

class SeleniumActionUntil(SeleniumAction):
	def selenium_click_until_available(self, click_locator, x = 0, y = 0, operate = 'click', timeout = 30.0, init_check = True, init_sleep = 0.0, wait_before_check = 0.0, do_interval = 1.0, check_interval = 0.2, error = True, _return_when_error = None, _log_keyword_structure = True, _return_name = None, __debug_default = None, __debug_debug = None) -> bool:
		"""
		一直尝试点击某个元素，直至这个元素可以被点击并且成功被点击为止
		******************** 下方是辅助函数和参数，请忽略return参数 ********************
		
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		选择某个元素相对中心偏移一定距离的位置进行点击
		:param click_locator: 目标元素或者locator
		:param x: 横坐标像素数
		:param y: 纵坐标像素数
		:param operate: 默认点击，doubleclick为双击
		:return: True
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		"""
		...
	def selenium_wait_until_find_element(self, check_locator, check_exist: bool = True, timeout = 30.0, init_check = True, init_sleep = 0.0, wait_before_check = 0.0, do_interval = 1.0, check_interval = 0.2, error = True, _return_when_error = None, _log_keyword_structure = True, _return_name = None, __debug_default = None, __debug_debug = None) -> bool:
		"""
		一直等待，直到在页面上寻找到某个元素为止
		******************** 下方是辅助函数和参数，请忽略return参数 ********************
		
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		检查页面内是否存在某个元素
		:param check_locator: 目标元素或locator
		:param check_exist: 默认检查存在。改为False后，改为检查页面中是否不存在这个元素
		:return: 搜素结果
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		"""
		...
	def selenium_wait_until_not_find_element(self, check_locator, check_exist: bool = False, timeout = 30.0, init_check = True, init_sleep = 0.0, wait_before_check = 0.0, do_interval = 1.0, check_interval = 0.2, error = True, _return_when_error = None, _log_keyword_structure = True, _return_name = None, __debug_default = None, __debug_debug = None) -> bool:
		"""
		:param check_exist: 现在默认值为False
		
		一直等待，直到在页面上寻找到某个元素为止
		******************** 下方是辅助函数和参数，请忽略return参数 ********************
		
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		检查页面内是否存在某个元素
		:param check_locator: 目标元素或locator
		:param check_exist: 默认检查存在。改为False后，改为检查页面中是否不存在这个元素
		:return: 搜素结果
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		"""
		...
	def selenium_click_until_find_elements(self, click_locator, check_locator, x = 0, y = 0, operate = 'click', check_count: int = 1, timeout = 30.0, init_check = True, init_sleep = 0.0, wait_before_check = 0.0, do_interval = 1.0, check_interval = 0.2, error = True, _return_when_error = None, _log_keyword_structure = True, _return_name = None, __debug_default = None, __debug_debug = None) -> bool:
		"""
		点击第一个元素，直到寻找到一定数量的第二个元素才停止点击。
		******************** 下方是辅助函数和参数，请忽略return参数 ********************
		
		选择某个元素相对中心偏移一定距离的位置进行点击
		:param click_locator: 目标元素或者locator
		:param x: 横坐标像素数
		:param y: 纵坐标像素数
		:param operate: 默认点击，doubleclick为双击
		:return: True
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		检查页面内某些元素的总数是否为特定的值
		:param check_locator: 目标元素或locator
		:param check_count: 元素的数量
		:return: 搜索结果。只有正好数量相同才会返回True
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		"""
		...
	def selenium_click_until_find_element(self, click_locator, check_locator, x = 0, y = 0, operate = 'click', check_exist: bool = True, timeout = 30.0, init_check = True, init_sleep = 0.0, wait_before_check = 0.0, do_interval = 1.0, check_interval = 0.2, error = True, _return_when_error = None, _log_keyword_structure = True, _return_name = None, __debug_default = None, __debug_debug = None) -> bool:
		"""
		点击第一个元素，直到寻找到第二个元素才停止点击
		******************** 下方是辅助函数和参数，请忽略return参数 ********************
		
		选择某个元素相对中心偏移一定距离的位置进行点击
		:param click_locator: 目标元素或者locator
		:param x: 横坐标像素数
		:param y: 纵坐标像素数
		:param operate: 默认点击，doubleclick为双击
		:return: True
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		检查页面内是否存在某个元素
		:param check_locator: 目标元素或locator
		:param check_exist: 默认检查存在。改为False后，改为检查页面中是否不存在这个元素
		:return: 搜素结果
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		"""
		...
	def selenium_click_until_not_find_element(self, click_locator, check_locator, x = 0, y = 0, operate = 'click', check_exist: bool = False, timeout = 30.0, init_check = True, init_sleep = 0.0, wait_before_check = 0.0, do_interval = 1.0, check_interval = 0.2, error = True, _return_when_error = None, _log_keyword_structure = True, _return_name = None, __debug_default = None, __debug_debug = None) -> bool:
		"""
		:param check_exist: 现在默认值为False
		
		点击第一个元素，直到寻找到第二个元素才停止点击
		******************** 下方是辅助函数和参数，请忽略return参数 ********************
		
		选择某个元素相对中心偏移一定距离的位置进行点击
		:param click_locator: 目标元素或者locator
		:param x: 横坐标像素数
		:param y: 纵坐标像素数
		:param operate: 默认点击，doubleclick为双击
		:return: True
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		检查页面内是否存在某个元素
		:param check_locator: 目标元素或locator
		:param check_exist: 默认检查存在。改为False后，改为检查页面中是否不存在这个元素
		:return: 搜素结果
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		"""
		...
	def selenium_wait_until_find_element_attribute(self, find_locator, find_value = '', find_attribute = 'innerText', attribute_type = '', regex = True, check_bool = True, timeout = 30.0, init_check = True, init_sleep = 0.0, wait_before_check = 0.0, do_interval = 1.0, check_interval = 0.2, error = True, _return_when_error = None, _log_keyword_structure = True, _return_name = None, __debug_default = None, __debug_debug = None) -> selenium.webdriver.remote.webelement.WebElement:
		"""
		一直等待，直到第二组目标元素存在一个元素的属性值满足需求
		******************** 下方是辅助函数和参数，请忽略return参数 ********************
		
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		在所有目标元素中，寻找第一个属性值满足需求的元素，并返回
		:param find_locator: 搜索目标元素或locator
		:param find_value: 所需要匹配的属性值
		:param find_attribute: 所需要寻找的属性
		:param attribute_type: 属性的类型，默认三个类型均搜索，可以输入以下其中之一：attribute、property、dom
		:param regex: 属性值是否为一个正则公式，默认为正则，如果输入False，那么需要属性值完全匹配
		:param check_bool: 是否为满足条件，默认为找到满足条件的元素。如果输入False，那么需要找到目标元素存在一个不满足条件的
		:return: 寻找到的满足要求的元素
		:raise RfError:如果没有满足要求的元素，那么会抛出
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		"""
		...
	def selenium_click_until_find_element_attribute(self, click_locator, find_locator, x = 0, y = 0, operate = 'click', find_value = '', find_attribute = 'innerText', attribute_type = '', regex = True, check_bool = True, timeout = 30.0, init_check = True, init_sleep = 0.0, wait_before_check = 0.0, do_interval = 1.0, check_interval = 0.2, error = True, _return_when_error = None, _log_keyword_structure = True, _return_name = None, __debug_default = None, __debug_debug = None) -> selenium.webdriver.remote.webelement.WebElement:
		"""
		点击第一个元素，直到在第二组目标元素中存在一个元素的属性值满足需求，才停止点击
		******************** 下方是辅助函数和参数，请忽略return参数 ********************
		
		选择某个元素相对中心偏移一定距离的位置进行点击
		:param click_locator: 目标元素或者locator
		:param x: 横坐标像素数
		:param y: 纵坐标像素数
		:param operate: 默认点击，doubleclick为双击
		:return: True
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		在所有目标元素中，寻找第一个属性值满足需求的元素，并返回
		:param find_locator: 搜索目标元素或locator
		:param find_value: 所需要匹配的属性值
		:param find_attribute: 所需要寻找的属性
		:param attribute_type: 属性的类型，默认三个类型均搜索，可以输入以下其中之一：attribute、property、dom
		:param regex: 属性值是否为一个正则公式，默认为正则，如果输入False，那么需要属性值完全匹配
		:param check_bool: 是否为满足条件，默认为找到满足条件的元素。如果输入False，那么需要找到目标元素存在一个不满足条件的
		:return: 寻找到的满足要求的元素
		:raise RfError:如果没有满足要求的元素，那么会抛出
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		"""
		...
	def selenium_wait_until_attribute_change(self, check_locator, check_attribute = 'innerText', attribute_type = '', timeout = 30.0, init_check = True, init_sleep = 0.0, wait_before_check = 0.0, do_interval = 1.0, check_interval = 0.2, error = True, _return_when_error = None, _log_keyword_structure = True, _return_name = None, __debug_default = None, __debug_debug = None) -> bool:
		"""
		一直等待，直到目标元素的某个目标属性发生了变化
		******************** 下方是辅助函数和参数，请忽略return参数 ********************
		
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		:param check_locator: 待检查的元素或locator
		:param check_attribute: 检查的目标属性名
		:param attribute_type: 属性的类型，默认三个类型均搜索，可以输入以下其中之一：attribute、property、dom
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		"""
		...
	def selenium_click_until_attribute_change(self, click_locator, check_locator, x = 0, y = 0, operate = 'click', check_attribute = 'innerText', attribute_type = '', timeout = 30.0, init_check = True, init_sleep = 0.0, wait_before_check = 0.0, do_interval = 1.0, check_interval = 0.2, error = True, _return_when_error = None, _log_keyword_structure = True, _return_name = None, __debug_default = None, __debug_debug = None) -> bool:
		"""
		一直点击第一个元素，直到第二组目标元素的某个目标属性发生了变化
		******************** 下方是辅助函数和参数，请忽略return参数 ********************
		
		选择某个元素相对中心偏移一定距离的位置进行点击
		:param click_locator: 目标元素或者locator
		:param x: 横坐标像素数
		:param y: 纵坐标像素数
		:param operate: 默认点击，doubleclick为双击
		:return: True
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		:param check_locator: 待检查的元素或locator
		:param check_attribute: 检查的目标属性名
		:param attribute_type: 属性的类型，默认三个类型均搜索，可以输入以下其中之一：attribute、property、dom
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		"""
		...
	def selenium_wait_until_element_count_change(self, check_locator, timeout = 30.0, init_check = True, init_sleep = 0.0, wait_before_check = 0.0, do_interval = 1.0, check_interval = 0.2, error = True, _return_when_error = None, _log_keyword_structure = True, _return_name = None, __debug_default = None, __debug_debug = None) -> bool:
		"""
		一直等待，直到目标元素的数量发生了变化
		******************** 下方是辅助函数和参数，请忽略return参数 ********************
		
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		:param check_locator: 待检查的元素或locator
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		"""
		...
	def selenium_click_until_element_count_change(self, click_locator, check_locator, x = 0, y = 0, operate = 'click', timeout = 30.0, init_check = True, init_sleep = 0.0, wait_before_check = 0.0, do_interval = 1.0, check_interval = 0.2, error = True, _return_when_error = None, _log_keyword_structure = True, _return_name = None, __debug_default = None, __debug_debug = None) -> bool:
		"""
		一直点击第一个元素，直到第二组目标元素的数量发生了变化
		******************** 下方是辅助函数和参数，请忽略return参数 ********************
		
		选择某个元素相对中心偏移一定距离的位置进行点击
		:param click_locator: 目标元素或者locator
		:param x: 横坐标像素数
		:param y: 纵坐标像素数
		:param operate: 默认点击，doubleclick为双击
		:return: True
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		:param check_locator: 待检查的元素或locator
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		"""
		...
	def selenium_wait_until_stable_find_element(self, check_locator, check_exist: bool = True, timeout = 30.0, init_check = True, init_sleep = 0.0, stable_time = 3.0, check_interval = 0.2, error = True, _return_when_error = None, _log_keyword_structure = True, _return_name = None, __debug_default = None, __debug_debug = None) -> bool:
		"""
		一直等待，直到在界面上连续若干秒都能搜索到目标元素
		******************** 下方是辅助函数和参数，请忽略return参数 ********************
		
		检查页面内是否存在某个元素
		:param check_locator: 目标元素或locator
		:param check_exist: 默认检查存在。改为False后，改为检查页面中是否不存在这个元素
		:return: 搜素结果
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		"""
		...
	def selenium_wait_until_stable_find_elements(self, check_locator, check_count: int = 1, timeout = 30.0, init_check = True, init_sleep = 0.0, stable_time = 3.0, check_interval = 0.2, error = True, _return_when_error = None, _log_keyword_structure = True, _return_name = None, __debug_default = None, __debug_debug = None) -> bool:
		"""
		一直等待，直到在界面上连续若干秒都能搜索到一定数量的目标元素
		******************** 下方是辅助函数和参数，请忽略return参数 ********************
		
		检查页面内某些元素的总数是否为特定的值
		:param check_locator: 目标元素或locator
		:param check_count: 元素的数量
		:return: 搜索结果。只有正好数量相同才会返回True
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		"""
		...
	def selenium_wait_until_stable_not_find_element(self, check_locator, check_exist: bool = False, timeout = 30.0, init_check = True, init_sleep = 0.0, stable_time = 3.0, check_interval = 0.2, error = True, _return_when_error = None, _log_keyword_structure = True, _return_name = None, __debug_default = None, __debug_debug = None) -> bool:
		"""
		:param check_exist: 现在默认值为False
		
		一直等待，直到在界面上连续若干秒都能搜索到目标元素
		******************** 下方是辅助函数和参数，请忽略return参数 ********************
		
		检查页面内是否存在某个元素
		:param check_locator: 目标元素或locator
		:param check_exist: 默认检查存在。改为False后，改为检查页面中是否不存在这个元素
		:return: 搜素结果
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		"""
		...
	def selenium_wait_until_stable_find_element_attribute(self, find_locator, find_value = '', find_attribute = 'innerText', attribute_type = '', regex = True, check_bool = True, timeout = 30.0, init_check = True, init_sleep = 0.0, stable_time = 3.0, check_interval = 0.2, error = True, _return_when_error = None, _log_keyword_structure = True, _return_name = None, __debug_default = None, __debug_debug = None) -> selenium.webdriver.remote.webelement.WebElement:
		"""
		一直等待，直到在界面上连续若干秒都在目标元素内找到一个属性满足要求的元素
		******************** 下方是辅助函数和参数，请忽略return参数 ********************
		
		在所有目标元素中，寻找第一个属性值满足需求的元素，并返回
		:param find_locator: 搜索目标元素或locator
		:param find_value: 所需要匹配的属性值
		:param find_attribute: 所需要寻找的属性
		:param attribute_type: 属性的类型，默认三个类型均搜索，可以输入以下其中之一：attribute、property、dom
		:param regex: 属性值是否为一个正则公式，默认为正则，如果输入False，那么需要属性值完全匹配
		:param check_bool: 是否为满足条件，默认为找到满足条件的元素。如果输入False，那么需要找到目标元素存在一个不满足条件的
		:return: 寻找到的满足要求的元素
		:raise RfError:如果没有满足要求的元素，那么会抛出
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		"""
		...
	def selenium_wait_until_stable_attribute_unchanged(self, check_locator, check_attribute = 'innerText', timeout = 30.0, init_check = True, init_sleep = 0.0, stable_time = 3.0, check_interval = 0.2, error = True, _return_when_error = None, _log_keyword_structure = True, _return_name = None, __debug_default = None, __debug_debug = None) -> bool:
		"""
		一直等待，直到在界面上连续若干秒内目标元素的目标属性的属性值均未发生变化
		******************** 下方是辅助函数和参数，请忽略return参数 ********************
		
		:param check_locator: 待检查的元素或locator
		:param check_attribute: 检查的目标属性名
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		"""
		...
	def selenium_input_delete_all_and_input(self, input_locator, input_text, sleep_time = 1.0, pass_when_same_input = True, __debug_default = None, __debug_debug = None, _return_when_error = None, _log_keyword_structure = True, _return_name = None):
		"""
		对input输入框删除所有内容后重新输入内容。
		如果输入完毕后，发现文本没有变为理想结果，将会尝试重试，重试最多5此
		输入成功，或者达成最多重试次数后，会点击Tab进行失焦
		:param input_locator: input输入框或其locator
		:param input_text: 待输入的文本
		:param sleep_time: 输入完毕后等待时间
		:param pass_when_same_input: 默认如果已有信息和目标文本一致，那么将会跳过这些操作。如果传入False，那么将总是重新输入
		:param _return_when_error : 输入任意非None值后，当error发生时，不再raise error，而是返回这个值
		:param _log_keyword_structure : bool : 默认True，生成一组robotframework格式的可展开的日志。如果False时，就不会把这个函数做成折叠状，而是只打印一些内容
		:param _return_name : str : 你可以把代码中这个函数赋值的变量str写在这儿，来让日志更加贴近python代码内容
		"""
		...
	...

