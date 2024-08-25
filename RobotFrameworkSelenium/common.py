#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# File          : common
# Author        : Sun YiFan-Movoid
# Time          : 2024/2/16 18:47
# Description   : 
"""
import base64
import math
import os
from typing import List, Tuple, Union, Any

import cv2
import numpy as np
import robot.libraries.BuiltIn
import selenium.webdriver.chrome.webdriver
from RobotFrameworkBasic import RobotBasic, robot_log_keyword, RfError, robot_no_log_keyword
from Selenium2Library import Selenium2Library
from movoid_function import decorate_class_function_exclude
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement


@decorate_class_function_exclude(robot_log_keyword)
class BasicCommon(RobotBasic):
    def __init__(self):
        super().__init__()
        self.built: robot.libraries.BuiltIn.BuiltIn = getattr(self, 'built', None)
        self.selenium_lib: Selenium2Library = getattr(self, 'selenium_lib', None)
        self.driver: selenium.webdriver.chrome.webdriver.WebDriver = getattr(self, 'driver', None)
        self.action_chains: ActionChains = getattr(self, 'action_chains', None)
        self.screenshot_root: str = getattr(self, 'screenshot_root', None)
        self.outer_coordinate: Tuple[float] = getattr(self, 'outer_coordinate', None)
        self.inner_coordinate: Tuple[float] = getattr(self, 'inner_coordinate', None)
        self.window_x: float = getattr(self, 'window_x', None)
        self.window_y: float = getattr(self, 'window_y', None)

    def selenium_init(self, screenshot_log: bool = False):
        screenshot_log = self.robot_check_param(screenshot_log, bool, False)
        self.selenium_lib = self.built.get_library_instance('Selenium2Library')
        self.driver = self.selenium_lib.driver
        self.action_chains = ActionChains(self.driver)
        self.screenshot_root = None if screenshot_log else ('.' if self.selenium_lib.screenshot_root_directory is None else self.selenium_lib.screenshot_root_directory)
        if screenshot_log is True:
            self.selenium_lib.set_screenshot_directory("EMBED")

    def selenium_analyse_locator(self, locator: str) -> Tuple[str, str]:
        if locator.startswith('/'):
            return 'xpath', locator
        elif '=' in locator:
            by, path = locator.split('=', 1)
            by = by.lower().replace('_', ' ').strip(' ')
            if by in ["id", "xpath", "link text", "partial link text", "name", "tag name", "class name", "css selector"]:
                return by, path
            elif by in ('css',):
                return "css selector", locator
            elif by in ('link',):
                return "partial link text", locator
            elif by in ('tag',):
                return "tag name", locator
            elif by in ('class',):
                return "class name", locator
            else:
                return "css selector", locator
        else:
            return "css selector", locator

    def selenium_find_elements_by_locator(self, locator) -> List[WebElement]:
        by, path = self.selenium_analyse_locator(locator)
        return self.driver.find_elements(by, path)

    def selenium_find_element_by_locator(self, locator) -> WebElement:
        by, path = self.selenium_analyse_locator(locator)
        return self.driver.find_element(by, path)

    def selenium_execute_js_script(self, js_code: str, *args):
        return self.driver.execute_script(js_code, *args)

    def analyse_color_function(self, color_function):
        re_func = None
        if callable(color_function):
            return color_function
        elif isinstance(color_function, str):
            if ',' in color_function:
                re_func = self.exchange_list3_to_color_function(color_function.split(',', 2))
            else:
                raise RfError('you input [{}] to find a color function, but it is not in default_color_function'.format(color_function))
        elif isinstance(color_function, list):
            re_func = self.exchange_list3_to_color_function(color_function)
        return re_func

    def exchange_list3_to_color_function(self, formula_list):
        return lambda r, g, b: eval('r' + formula_list[0]) and eval('g' + formula_list[1]) and eval('b' + formula_list[2])

    def selenium_get_full_screenshot_path(self, screenshot_name):
        folder_name = self.get_suite_case_str().replace(' ', '_')
        full_folder_path = os.path.join(self.screenshot_root, folder_name)
        if not os.path.exists(full_folder_path):
            os.mkdir(full_folder_path)
            print(f'create image folder:{folder_name}')
        return os.path.join(full_folder_path, screenshot_name)

    def selenium_cut_screenshot(self, screenshot_locator, image_name='element-cut-image.png'):
        if self.screenshot_root is None:
            cut_image = self.selenium_log_screenshot(screenshot_locator)
        else:
            tar_name, tar_path = self.selenium_take_screenshot(None, image_name)
            full_image = self.selenium_analyse_image(tar_name)
            if screenshot_locator is None:
                cut_image = full_image
            else:
                tar_element = self.selenium_analyse_element(screenshot_locator)
                element_position = self.selenium_execute_js_script('return arguments[0].getBoundingClientRect();', tar_element)
                print(element_position)
                cut_rect = [math.floor(element_position['left']), math.floor(element_position['top']), math.floor(element_position['right']), math.floor(element_position['bottom'])]
                cut_image = full_image[cut_rect[1]:cut_rect[3], cut_rect[0]:cut_rect[2]]
                print(cut_image.shape)
                tar_path_split = os.path.splitext(tar_path)
                cv2.imwrite(tar_path_split[0] + '(cut)' + tar_path_split[1], cut_image)
        print(f'the shape of cut screenshot is {cut_image.shape}')
        return cut_image

    def selenium_take_screenshot(self, screenshot_locator=None, image_name='python-screenshot.png', rename=True):
        if self.screenshot_root is None:
            return self.selenium_log_screenshot(screenshot_locator), None
        else:
            tar_name = image_name
            ind = 1
            tar_path = self.selenium_get_full_screenshot_path(tar_name)
            while rename and os.path.isfile(tar_path):
                ind += 1
                name, post = os.path.splitext(image_name)
                tar_name = f'{name}-{ind}{post}'
                tar_path = self.selenium_get_full_screenshot_path(tar_name)
            if screenshot_locator is None:
                self.selenium_lib.capture_page_screenshot(tar_path)
                print(f'take a full window screenshot:{tar_name}')
            else:
                self.selenium_lib.capture_element_screenshot(screenshot_locator, tar_path)
                print(f'take a DOM({screenshot_locator}) screenshot:{tar_name}')
            return tar_name, tar_path

    def selenium_log_screenshot(self, screenshot_locator=None):
        if screenshot_locator is None:
            img = self.driver.get_screenshot_as_base64()
            cv_value = np.frombuffer(base64.b64decode(img), np.uint8)
        else:
            img_data = self.driver.get_screenshot_as_png()
            img_array = np.fromstring(img_data, np.uint8)
            full_image = cv2.imdecode(img_array, cv2.COLOR_RGB2BGR)
            tar_element = self.selenium_analyse_element(screenshot_locator)
            element_position = self.selenium_execute_js_script('return arguments[0].getBoundingClientRect();', tar_element)
            print("element_position:", element_position)
            cut_rect = [math.floor(element_position['left']), math.floor(element_position['top']), math.floor(element_position['right']), math.floor(element_position['bottom'])]
            cut_image = full_image[cut_rect[1]:cut_rect[3], cut_rect[0]:cut_rect[2]]
            cv_value = cut_image
            print("cut image shape:", cut_image.shape)
            image = cv2.imencode('.png', cut_image)[1]
            img = str(base64.b64encode(image))[2:-1]
        self.print(f'<img src="data:image/png;base64,{img}">', html=True)
        return cv_value

    def selenium_log_screenshot_path(self, screenshot_name):
        full_path = self.selenium_get_full_screenshot_path(screenshot_name)
        self.log_show_image(full_path)

    def selenium_analyse_image(self, image):
        if isinstance(image, str):
            image_full_path = image if os.path.isfile(image) else self.selenium_get_full_screenshot_path(image)
            print(f'try to read image:{image_full_path}')
            return cv2.imread(image_full_path)
        else:
            return image

    def selenium_analyse_element(self, locator: Union[WebElement, str]) -> WebElement:
        if isinstance(locator, str):
            return self.selenium_find_element_by_locator(locator)
        elif isinstance(locator, list):
            return locator[0]
        else:
            return locator

    def selenium_analyse_elements(self, locator: Union[List[WebElement], str]) -> List[WebElement]:
        if isinstance(locator, str):
            return self.selenium_find_elements_by_locator(locator)
        elif isinstance(locator, WebElement):
            return [locator]
        else:
            return locator

    @robot_no_log_keyword
    def selenium_function_debug_raise_teardown(self, function, args, kwargs, re_value, error, trace_back, has_return):
        if error:
            self.selenium_take_screenshot()
        if has_return:
            return re_value

    @robot_no_log_keyword
    def selenium_function_debug_continue_teardown(self, function, args, kwargs, re_value, error, trace_back, has_return):
        if error:
            self.error(self.get_suite_case_str(), function.__name__, args, kwargs, type(error).__name__, error)
            self.selenium_take_screenshot()
        if has_return:
            return re_value
