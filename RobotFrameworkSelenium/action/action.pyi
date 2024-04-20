##################################################
# This is auto generated by code.
##################################################

import os
import pathlib
import re
import time
import cv2
import typing
from ..common import BasicCommon

class SeleniumAction(BasicCommon):
	def __init__(self):
		super().__init__()
		self._check_element_attribute_change_value: typing.Union[str, None] =  None
		self._check_element_count_value: typing.Union[int, None] =  None
	def selenium_take_full_screenshot(self, screenshot_name = 'python-screenshot.png'):	...
	def selenium_click_element(self, click_locator, operate = 'click'):	...
	def selenium_get_element_color_list(self, screenshot_locator = None, image_name = 'catch-image-color.png', rename = True):	...
	def selenium_click_element_with_offset(self, click_locator, x = 0, y = 0, operate = 'click'):	...
	def selenium_check_element_attribute(self, check_locator, check_attribute = 'innerText', check_value = '', regex = True, check_bool = True):
		"""
		检查所有元素中，是否存在一个属性满足要求的元素
		:param check_locator: 元素定位
		:param check_attribute: 属性名
		:param check_value: 属性值
		:param regex: 是否做正则匹配
		:param check_bool: 要求满足条件还是不满足条件的
		:return: 判定结果
		"""
		...
	def selenium_find_elements_with_attribute(self, find_locator, find_value = '', find_attribute = 'innerText', regex = True, check_bool = True) -> typing.List[selenium.webdriver.remote.webelement.WebElement]:	...
	def selenium_find_element_with_attribute(self, find_locator, find_value = '', find_attribute = 'innerText', regex = True, check_bool = True):	...
	def selenium_get_locator_attribute(self, target_locator, target_attribute = 'innerText'):	...
	def selenium_new_screenshot_folder(self):	...
	def selenium_delete_elements(self, delete_locator):	...
	def selenium_input_delete_all_and_input(self, input_locator, input_text):	...
	def selenium_check_contain_element(self, check_locator, check_exist = True):	...
	def selenium_check_contain_elements(self, check_locator, check_count = 1):	...
	def selenium_check_element_attribute_change_init(self, check_locator, check_attribute = 'innerText'):	...
	def selenium_check_element_attribute_change_loop(self, check_locator, check_attribute = 'innerText'):	...
	def selenium_check_element_count_change_init(self, check_locator):	...
	def selenium_check_element_count_change_loop(self, check_locator):	...
	def always_true(self):	...
	def selenium_click_until_available(self, click_locator, x = 0, y = 0, operate = 'click', screenshot_name = 'python-screenshot.png', timeout = 30.0, init_check = True, init_sleep = 0.0, wait_before_check = 0.0, do_interval = 1.0, check_timeout = 1.0, check_interval = 0.2, error = True):
		"""
		"""
		...
	def selenium_wait_until_find_element(self, check_locator, check_exist = True, screenshot_name = 'python-screenshot.png', timeout = 30.0, init_check = True, init_sleep = 0.0, wait_before_check = 0.0, do_interval = 1.0, check_timeout = 1.0, check_interval = 0.2, error = True):
		"""
		"""
		...
	def selenium_wait_until_not_find_element(self, check_locator, check_exist = False, screenshot_name = 'python-screenshot.png', timeout = 30.0, init_check = True, init_sleep = 0.0, wait_before_check = 0.0, do_interval = 1.0, check_timeout = 1.0, check_interval = 0.2, error = True):
		"""
		"""
		...
	def selenium_click_until_find_elements(self, click_locator, check_locator, x = 0, y = 0, operate = 'click', check_count = 1, screenshot_name = 'python-screenshot.png', timeout = 30.0, init_check = True, init_sleep = 0.0, wait_before_check = 0.0, do_interval = 1.0, check_timeout = 1.0, check_interval = 0.2, error = True):
		"""
		"""
		...
	def selenium_click_until_find_element(self, click_locator, check_locator, x = 0, y = 0, operate = 'click', check_exist = True, screenshot_name = 'python-screenshot.png', timeout = 30.0, init_check = True, init_sleep = 0.0, wait_before_check = 0.0, do_interval = 1.0, check_timeout = 1.0, check_interval = 0.2, error = True):
		"""
		"""
		...
	def selenium_click_until_not_find_element(self, click_locator, check_locator, x = 0, y = 0, operate = 'click', check_exist = False, screenshot_name = 'python-screenshot.png', timeout = 30.0, init_check = True, init_sleep = 0.0, wait_before_check = 0.0, do_interval = 1.0, check_timeout = 1.0, check_interval = 0.2, error = True):
		"""
		"""
		...
	def selenium_wait_until_find_element_attribute(self, find_locator, find_value = '', find_attribute = 'innerText', regex = True, check_bool = True, screenshot_name = 'python-screenshot.png', timeout = 30.0, init_check = True, init_sleep = 0.0, wait_before_check = 0.0, do_interval = 1.0, check_timeout = 1.0, check_interval = 0.2, error = True):
		"""
		"""
		...
	def selenium_click_until_find_element_attribute(self, click_locator, find_locator, x = 0, y = 0, operate = 'click', find_value = '', find_attribute = 'innerText', regex = True, check_bool = True, screenshot_name = 'python-screenshot.png', timeout = 30.0, init_check = True, init_sleep = 0.0, wait_before_check = 0.0, do_interval = 1.0, check_timeout = 1.0, check_interval = 0.2, error = True):
		"""
		"""
		...
	def selenium_wait_until_attribute_change(self, check_locator, check_attribute = 'innerText', screenshot_name = 'python-screenshot.png', timeout = 30.0, init_check = True, init_sleep = 0.0, wait_before_check = 0.0, do_interval = 1.0, check_timeout = 1.0, check_interval = 0.2, error = True):
		"""
		"""
		...
	def selenium_click_until_attribute_change(self, click_locator, check_locator, x = 0, y = 0, operate = 'click', check_attribute = 'innerText', screenshot_name = 'python-screenshot.png', timeout = 30.0, init_check = True, init_sleep = 0.0, wait_before_check = 0.0, do_interval = 1.0, check_timeout = 1.0, check_interval = 0.2, error = True):
		"""
		"""
		...
	def selenium_wait_until_element_count_change(self, check_locator, screenshot_name = 'python-screenshot.png', timeout = 30.0, init_check = True, init_sleep = 0.0, wait_before_check = 0.0, do_interval = 1.0, check_timeout = 1.0, check_interval = 0.2, error = True):
		"""
		"""
		...
	def selenium_click_until_element_count_change(self, click_locator, check_locator, x = 0, y = 0, operate = 'click', screenshot_name = 'python-screenshot.png', timeout = 30.0, init_check = True, init_sleep = 0.0, wait_before_check = 0.0, do_interval = 1.0, check_timeout = 1.0, check_interval = 0.2, error = True):
		"""
		"""
		...
	...

