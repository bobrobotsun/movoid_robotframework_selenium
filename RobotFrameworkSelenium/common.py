#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# File          : common
# Author        : Sun YiFan-Movoid
# Time          : 2024/2/16 18:47
# Description   : 
"""
import base64
import inspect
import math
import os
import typing
from typing import List, Tuple, Union, Any, Callable, Optional, Dict

import cv2
import numpy as np
import robot.libraries.BuiltIn
import selenium.webdriver.chrome.webdriver
from RobotFrameworkBasic import RobotBasic, robot_log_keyword, RfError, robot_no_log_keyword, RUN
from SeleniumLibrary import SeleniumLibrary
from lxml import html
from movoid_debug import debug, no_debug
from movoid_function import decorate_class_function_exclude
from selenium.common import NoSuchWindowException, InvalidSessionIdException
from selenium.webdriver.remote.webelement import WebElement
from selenium import webdriver


@decorate_class_function_exclude(debug)
@decorate_class_function_exclude(robot_log_keyword)
class BasicCommon(RobotBasic):
    def __init__(self):
        super().__init__()
        self.built: robot.libraries.BuiltIn.BuiltIn = getattr(self, 'built', None)
        self.selenium_lib: SeleniumLibrary = getattr(self, 'selenium_lib', None)
        self._driver_dict: typing.Dict[str, selenium.webdriver.chrome.webdriver.WebDriver] = getattr(self, '_driver_dict', {})
        self._driver_key: Optional[str] = getattr(self, '_driver_key', None)
        self.screenshot_root: str = getattr(self, 'screenshot_root', None)
        self.outer_coordinate: Tuple[float] = getattr(self, 'outer_coordinate', None)
        self.inner_coordinate: Tuple[float] = getattr(self, 'inner_coordinate', None)
        self.window_x: float = getattr(self, 'window_x', None)
        self.window_y: float = getattr(self, 'window_y', None)

    @property
    def driver(self) -> selenium.webdriver.chrome.webdriver.WebDriver:
        if self._driver_key is not None and self._driver_key in self._driver_dict:
            return self._driver_dict[self._driver_key]['driver']
        else:
            return None

    @property
    def action_chains(self) -> selenium.webdriver.ActionChains:
        if self._driver_key is not None and self._driver_key in self._driver_dict:
            return self._driver_dict[self._driver_key]['action_chains']
        else:
            return None

    @property
    def _driver_dict_value(self) -> dict:
        if self._driver_key is not None and self._driver_key in self._driver_dict:
            return self._driver_dict[self._driver_key]
        else:
            return {}

    if RUN == 'python':
        def selenium_init(self, screenshot_dir: str = '.'):
            """
            :param screenshot_dir: screenshot存储路径
            """
            self.screenshot_root = screenshot_dir if screenshot_dir else None
            self.selenium_lib = SeleniumLibrary()
            if not screenshot_dir:
                self.selenium_lib.set_screenshot_directory("EMBED")


    else:
        def selenium_init(self, screenshot_dir: str = '.'):
            self.selenium_lib = self.built.get_library_instance('Selenium2Library')
            self.screenshot_root = (screenshot_dir if self.selenium_lib.screenshot_root_directory is None else self.selenium_lib.screenshot_root_directory) if screenshot_dir else None
            if not screenshot_dir:
                self.selenium_lib.set_screenshot_directory("EMBED")

    def _create_driver_alias(self, alias=None) -> Tuple[bool, str]:
        """
        根据alias确实是否已经生成，如果不输入，那么将会自动生成一个没有过的值
        :param alias:
        :return: bool,str 是否已经生成了，目标alias名。
        """
        if alias is None:
            i = 0
            while True:
                temp = f'_{i}'
                if temp not in self._driver_dict and temp not in self.selenium_lib._drivers._aliases:
                    return False, temp
                i += 1
        else:
            temp = str(alias)
            return temp in self._driver_dict or temp in self.selenium_lib._drivers._aliases, temp

    def selenium_create_webdriver(self, driver_name: str = 'Chrome', alias=None, **kwargs):
        """
        :param driver_name: Chrome,Ie,Edge,Firefox,Safari,WebKitGTK,WPEWebKit
        :param alias: 标记名称，如果不填写的话，会默认按照_0、_1的逻辑无限循环增加下去
        :param kwargs: 其他driver参数
        """
        alias_exist, new_alias = self._create_driver_alias(alias=alias)
        if alias_exist:
            raise KeyError(f'can not create same alias:{new_alias}')
        else:
            driver_dict = {'driver': getattr(webdriver, driver_name)(**kwargs)}
            self._driver_dict[new_alias] = driver_dict
            self._driver_key = new_alias
            self.selenium_lib.register_driver(self.driver, new_alias)
            driver_dict['action_chains'] = selenium.webdriver.ActionChains(self.driver)
            driver_dict['window_list'] = []  # 这里是已经注册过的window handle的列表
            driver_dict['window_alias'] = {}  # 这里是用户确认的别名，alias:window_handle
            self.selenium_check_window_handles()
            return new_alias

    def _close_webdriver_by_key(self, key):
        """把目标driver整个quit掉"""
        key = str(key)
        if key in self._driver_dict:
            if self._driver_dict[key]['window_list']:
                if self._driver_key == key:
                    if len(self._driver_dict) <= 1:
                        self._driver_key = None
                    else:
                        driver_keys = list(self._driver_dict.keys())
                        driver_key_index = driver_keys.index(key)
                        if driver_key_index == 0:
                            self._driver_key = driver_keys[1]
                        else:
                            self._driver_key = driver_keys[driver_key_index - 1]
            self.selenium_lib._drivers._closed.add(self._driver_dict[key]['driver'])
            self._driver_dict[key]['driver'].quit()
            self._driver_dict.pop(key)
            if key in self.selenium_lib._drivers._aliases:
                del self.selenium_lib._drivers._aliases[key]

    def _close_window_by_key(self, key):
        key = str(key)
        if key in self._driver_dict:
            self._driver_dict[key]['driver'].close()
            self.selenium_check_window_handles(key)

    def selenium_switch_to_driver_by_alias(self, alias: str, error_when_not_find: bool = True):
        """
        将当前的driver切换到alias对应的driver
        :param alias:
        :param error_when_not_find:
        :return:
        """
        alias = str(alias)
        if alias in self._driver_dict:
            self._driver_key = alias
            self.selenium_lib._drivers.switch(self.driver)
            return True
        else:
            if error_when_not_find:
                raise KeyError(f'can not find alias:{alias}')
            else:
                return False

    def selenium_close_webdriver(self, alias=None, close_all_windows: bool = True):
        """
        删除
        :param alias:
        :param close_all_windows:会尝试关闭所有的窗口
        :return:
        """
        target_driver = self._driver_key if alias is None else str(alias)
        if target_driver in self._driver_dict:
            if close_all_windows:
                self._close_webdriver_by_key(target_driver)
            else:
                self._close_window_by_key(target_driver)

    def selenium_check_window_handles(self, alias=None, quit_driver: bool = True):
        """检查当前的windows handle是不是匹配。如果不匹配那么进行增删。仅处理当前的webdriver"""
        alias = self._driver_key if alias is None else str(alias)
        if alias in self._driver_dict:
            try:
                now_windows = self._driver_dict[alias]['driver'].window_handles
            except InvalidSessionIdException:
                self.selenium_close_webdriver(alias, close_all_windows=True)
            else:
                past_windows = [*self._driver_dict[alias]['window_list']]
                if now_windows != past_windows:
                    self._driver_dict[alias]['window_list'] = now_windows
                    should_delete = []
                    for name, window in self._driver_dict[alias]['window_alias']:
                        if window not in now_windows:
                            should_delete.append(name)
                    for name in should_delete:
                        self._driver_dict[alias]['window_alias'].pop(name)
                try:
                    handle = self._driver_dict[alias]['driver'].current_window_handle
                except NoSuchWindowException:
                    if len(self._driver_dict[alias]['window_list']) >= 1:
                        self._driver_dict[alias]['driver'].switch_to.window(self._driver_dict[alias]['window_list'][0])
                    else:
                        if quit_driver:
                            self.selenium_close_webdriver(alias, close_all_windows=True)

    def selenium_set_current_window_by_alias(self, window_alias):
        """
        给当前的window设置别名
        :param window_alias:
        :return:
        """
        self.selenium_check_window_handles()
        window_alias = str(window_alias)
        window = self.driver.current_window_handle
        self._driver_dict_value['window_alias'][window_alias] = window

    def selenium_set_index_window_by_alias(self, window_alias, window_index=-1):
        """
        给目标index的window设置别名，一般是设置最后一个
        :param window_alias:
        :param window_index:
        :return:
        """
        self.selenium_check_window_handles()
        window_alias = str(window_alias)
        window = self._driver_dict_value['window_list'][window_index]
        self._driver_dict_value['window_alias'][window_alias] = window

    def selenium_switch_to_window_by_index(self, window_index: int):
        window_index = int(window_index)
        self.driver.switch_to.window(self._driver_dict_value['window_list'][window_index])
        return True

    def selenium_switch_to_window_by_alias(self, window_alias: str, error_when_not_find: bool = True):
        """
        按照别名将window切换过去
        :param window_alias:
        :param error_when_not_find: 如果没有找到，那么是否报错
        :return:
        """
        self.selenium_check_window_handles()
        window_alias = str(window_alias)
        if window_alias in self._driver_dict_value['window_alias']:
            self.driver.switch_to.window(self._driver_dict_value['window_alias'][window_alias])
            return True
        else:
            if error_when_not_find:
                raise KeyError(f'there is no window alias:{window_alias}')
            else:
                return False

    def selenium_switch_to_window_by_handle(self, window_handle: str, error_when_not_find: bool = True):
        """
        根据handle来切换
        :param window_handle:
        :param error_when_not_find: 如果没有找到，那么是否报错
        :return:
        """
        self.selenium_check_window_handles()
        window_handle = str(window_handle)
        if window_handle in self._driver_dict_value['window_list']:
            self.driver.switch_to.window(window_handle)
            return True
        else:
            if error_when_not_find:
                raise KeyError(f'there is no window handle:{window_handle}')
            else:
                return False

    def selenium_get_window_handle_by_alias(self, window_alias: str):
        window_alias = str(window_alias)
        if window_alias in self._driver_dict_value['window_alias']:
            return self._driver_dict_value['window_alias'][window_alias]
        else:
            return None

    def selenium_get_window_handle_by_index(self, index: int):
        index = int(index)
        return self._driver_dict_value['window_list'][index]

    def selenium_get_target_window_title_by_handle(self, window_handle: str) -> str:
        window_handle = str(window_handle)
        current_handle = self.driver.current_window_handle
        if current_handle == window_handle:
            return self.driver.title
        else:
            self.selenium_switch_to_window_by_handle(window_handle)
            title = self.driver.title
            self.driver.switch_to.window(current_handle)
            return title

    def selenium_get_all_window_title(self) -> Dict[str, str]:
        current_handle = self.driver.current_window_handle
        self.selenium_check_window_handles()
        re_title = {}
        for handle in self._driver_dict_value['window_list']:
            self.driver.switch_to.window(handle)
            re_title[handle] = self.driver.title
        self.driver.switch_to.window(current_handle)
        return re_title

    def selenium_close_window(self):
        """把current window关了"""
        self.driver.close()
        self.selenium_check_window_handles()

    def selenium_analyse_locator(self, locator: Union[str, list, set, tuple]) -> Tuple[str, str]:
        """
        将locator文本解析为by,path，方便find element
        :param locator: 合并的locator
        :return:
        """
        if isinstance(locator, str):
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
        else:
            return locator[0], locator[1]

    def selenium_find_elements_by_locator(self, locator) -> List[WebElement]:
        """
        :param locator: by=path
        """
        by, path = self.selenium_analyse_locator(locator)
        return self.driver.find_elements(by, path)

    def selenium_find_element_by_locator(self, locator) -> WebElement:
        """
        :param locator: by=path
        """
        by, path = self.selenium_analyse_locator(locator)
        return self.driver.find_element(by, path)

    def selenium_html_find_element_by_locator(self, locator) -> html.HtmlElement:
        """
        :param locator: by=path
        """
        results = self.selenium_html_find_elements_by_locator(locator)
        if len(results) >= 1:
            return results[0]
        else:
            raise KeyError(f'cannot find any element by {locator}')

    def selenium_html_find_elements_by_locator(self, locator) -> List[html.HtmlElement]:
        """
        使用html的方法检查页面内是否存在某个元素
        :param locator: 目标元素或locator
        :return: 搜素结果
        """
        by, path = self.selenium_analyse_locator(locator)
        html_text = self.driver.page_source
        html_tree: html.HtmlElement = html.fromstring(html_text)
        if by == 'css selector':
            results = html_tree.cssselect(path)
        elif by == 'xpath':
            results = html_tree.xpath(path)
        elif by == 'id':
            results = html_tree.xpath(rf'//*[@id="{path}"]')
        elif by == 'class name':
            results = html_tree.find_class(path)
        else:
            raise ValueError(f'do not support {by},only [css selector/xpath/id/class name] accept')
        return results

    def selenium_execute_js_script(self, js_code: str, *args) -> Any:
        """
        :param js_code: javascript脚本文本
        :param args: 其他相应的参数
        """
        return self.driver.execute_script(js_code, *args)

    def analyse_color_function(self, color_function) -> Callable[[int, int, int], bool]:
        """
        :param color_function: 输入的符号+数值，例如 >60,>60,>60
        :return: 相应的判定函数
        """
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

    def exchange_list3_to_color_function(self, formula_list) -> Callable[[int, int, int], bool]:
        """
        :param formula_list: 已经解析清晰的列表
        :return: 相应的判定函数
        """
        return lambda r, g, b: eval('r' + formula_list[0]) and eval('g' + formula_list[1]) and eval('b' + formula_list[2])

    def selenium_get_full_screenshot_path(self, screenshot_name) -> str:
        """
        :param screenshot_name: 截图存储文件夹名
        :return: 截屏文件夹全路径
        """
        folder_name = self.get_suite_case_str().replace(' ', '_')
        full_folder_path = os.path.join(self.screenshot_root, folder_name)
        if not os.path.exists(full_folder_path):
            os.mkdir(full_folder_path)
            print(f'create image folder:{folder_name}')
        return os.path.join(full_folder_path, screenshot_name)

    def selenium_cut_screenshot(self, screenshot_locator=None, image_name='element-cut-image.png', _show_return_info=False):
        """
        :param screenshot_locator: 截图目标，不输入则全浏览器截屏
        :param image_name: 存储的文件名称
        :param _show_return_info: 是否显示返回值，默认不显示
        """
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

    def test123(self):
        self.selenium_log_screenshot(None, False)

    def selenium_take_screenshot(self, screenshot_locator=None, image_name='python-screenshot.png', rename=True, _show_return_info=False):
        """
        :param screenshot_locator: 截图目标，不输入则全浏览器截屏
        :param image_name: 存储的文件名称
        :param rename: 如果重名了，是否通过增加序号的方式重命名
        :param _show_return_info: 是否显示返回值，默认不显示
        """
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
                self.driver.save_screenshot(tar_path)
                print(f'take a full window screenshot:{tar_name}')
            else:
                self.selenium_find_element_by_locator(screenshot_locator).screenshot(tar_path)
                print(f'take a DOM({screenshot_locator}) screenshot:{tar_name}')
            return tar_name, tar_path

    def selenium_log_screenshot(self, screenshot_locator=None, _show_return_info=False) -> np.ndarray:
        """
        :param screenshot_locator: 截图目标，不输入则全浏览器截屏
        :param _show_return_info: 是否显示返回值，默认不显示
        """
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

    def selenium_log_screenshot_path(self, screenshot_name) -> None:
        """
        :param screenshot_name: 截图存储文件夹名称
        """
        full_path = self.selenium_get_full_screenshot_path(screenshot_name)
        self.log_show_image(full_path)

    def selenium_analyse_image(self, image):
        """
        :param image: 目标图片的路径
        """
        if isinstance(image, str):
            image_full_path = image if os.path.isfile(image) else self.selenium_get_full_screenshot_path(image)
            print(f'try to read image:{image_full_path}')
            return cv2.imread(image_full_path)
        else:
            return image

    def selenium_analyse_element(self, locator: Union[WebElement, str]) -> WebElement:
        """
        :param locator: locator或者element
        """
        if isinstance(locator, str):
            return self.selenium_find_element_by_locator(locator)
        elif isinstance(locator, list):
            return locator[0]
        else:
            return locator

    def selenium_analyse_elements(self, locator: Union[List[WebElement], str]) -> List[WebElement]:
        """
        :param locator: locator或者elements
        """
        if isinstance(locator, str):
            return self.selenium_find_elements_by_locator(locator)
        elif isinstance(locator, WebElement):
            return [locator]
        else:
            return locator

    @no_debug
    @robot_no_log_keyword
    def selenium_debug_teardown(self, function, args, kwargs, re_value, error, trace_back, has_return):
        """
        通用的debug teardown函数
        :param function: 函数
        :param args: args参数
        :param kwargs: kwargs参数
        :param re_value: 对应的返回值
        :param error: 弹出的报错，没报错就None
        :param trace_back: 弹出的报错的traceback，没报错就None
        :param has_return: 是否有返回值
        :return:
        """
        if error:
            if self._no_error_when_exception <= 0:
                self.error(self.get_suite_case_str(), function.__name__, args, kwargs, type(error).__name__, error)
            self.selenium_take_screenshot()
        if has_return:
            return re_value
