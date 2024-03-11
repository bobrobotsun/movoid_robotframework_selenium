#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# File          : common
# Author        : Sun YiFan-Movoid
# Time          : 2024/2/16 18:47
# Description   : 
"""
import math
import os
from typing import List, Tuple, Union

import cv2
import robot.libraries.BuiltIn
import selenium.webdriver.chrome.webdriver
from Selenium2Library import Selenium2Library
from RobotFrameworkBasic import RobotBasic, robot_log_keyword, RfError
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement


class BasicCommon(RobotBasic):
    def __init__(self):
        super().__init__()
        self.built: robot.libraries.BuiltIn.BuiltIn = getattr(self, 'built', None)
        self.selenium_lib: Selenium2Library = getattr(self, 'built', None)
        self.driver: selenium.webdriver.chrome.webdriver.WebDriver = getattr(self, 'driver', None)
        self.action_chains: ActionChains = getattr(self, 'action_chains', None)
        self.screenshot_root: str = getattr(self, 'screenshot_root', None)
        self.outer_coordinate: Tuple[float] = getattr(self, 'outer_coordinate', None)
        self.inner_coordinate: Tuple[float] = getattr(self, 'inner_coordinate', None)
        self.window_x: float = getattr(self, 'window_x', None)
        self.window_y: float = getattr(self, 'window_y', None)

    @robot_log_keyword
    def selenium_init(self):
        self.selenium_lib = self.built.get_library_instance('Selenium2Library')
        self.driver = self.selenium_lib.driver
        self.action_chains = ActionChains(self.driver)
        self.screenshot_root = self.selenium_lib.screenshot_root_directory

    @robot_log_keyword
    def selenium_find_elements_by_locator(self, locator) -> List[WebElement]:
        by, path = locator.split('=', 1)
        return self.driver.find_elements(by, path)

    @robot_log_keyword
    def selenium_find_element_by_locator(self, locator) -> WebElement:
        by, path = locator.split('=', 1)
        return self.driver.find_element(by, path)

    @robot_log_keyword
    def selenium_execute_js_script(self, js_code: str, *args):
        return self.driver.execute_script(js_code, *args)

    @robot_log_keyword
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

    @robot_log_keyword
    def exchange_list3_to_color_function(self, formula_list):
        return lambda r, g, b: eval('r' + formula_list[0]) and eval('g' + formula_list[1]) and eval('b' + formula_list[2])

    @robot_log_keyword
    def selenium_get_full_screenshot_path(self, screenshot_name):
        suite = self.get_robot_variable('SUITE NAME').replace(' ', '_')
        case_ori = self.get_robot_variable('TEST NAME')
        folder_name = suite if case_ori is None else f"{suite}-{case_ori.replace(' ', '_')}"
        full_folder_path = os.path.join(self.screenshot_root, folder_name)
        if not os.path.exists(full_folder_path):
            os.mkdir(full_folder_path)
            self.print(f'create image folder:{folder_name}')
        return os.path.join(full_folder_path, screenshot_name)

    @robot_log_keyword
    def selenium_cut_screenshot(self, screenshot_locator, image_name='element-cut-image.png'):
        tar_name, tar_path = self.selenium_take_screenshot(None, image_name)
        full_image = self.selenium_analyse_image(tar_name)
        if screenshot_locator is None:
            return full_image
        else:
            tar_element = self.selenium_analyse_element(screenshot_locator)
            element_position = self.selenium_execute_js_script('return arguments[0].getBoundingClientRect();', tar_element)
            self.print(element_position)
            cut_rect = [math.floor(element_position['left']), math.floor(element_position['top']), math.floor(element_position['right']), math.floor(element_position['bottom'])]
            cut_image = full_image[cut_rect[1]:cut_rect[3], cut_rect[0]:cut_rect[2]]
            self.print(cut_image.shape)
            tar_path_split = os.path.splitext(tar_path)
            cv2.imwrite(tar_path_split[0] + '(cut)' + tar_path_split[1], cut_image)
            return cut_image

    @robot_log_keyword
    def selenium_take_screenshot(self, screenshot_locator=None, image_name='python-screenshot.png', rename=True):
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
            self.print(f'take a full window screenshot:{tar_name}')
        else:
            self.selenium_lib.capture_element_screenshot(screenshot_locator, tar_path)
            self.print(f'take a DOM({screenshot_locator}) screenshot:{tar_name}')
        return tar_name, tar_path

    @robot_log_keyword
    def selenium_analyse_image(self, image):
        if isinstance(image, str):
            image_full_path = image if os.path.isfile(image) else self.selenium_get_full_screenshot_path(image)
            self.print(f'try to read image:{image_full_path}')
            return cv2.imread(image_full_path)
        else:
            return image

    @robot_log_keyword
    def selenium_analyse_element(self, locator: Union[WebElement, str]) -> WebElement:
        if isinstance(locator, str):
            return self.selenium_find_element_by_locator(locator)
        elif isinstance(locator, list):
            return locator[0]
        else:
            return locator

    @robot_log_keyword
    def selenium_analyse_elements(self, locator: Union[List[WebElement], str]) -> List[WebElement]:
        if isinstance(locator, str):
            return self.selenium_find_elements_by_locator(locator)
        elif isinstance(locator, WebElement):
            return [locator]
        else:
            return locator