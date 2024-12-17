#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# File          : basic
# Author        : Sun YiFan-Movoid
# Time          : 2024/2/16 20:12
# Description   : 
"""

import os
import pathlib
import re
import time
from typing import List, Union, Any

import cv2
import numpy as np
from RobotFrameworkBasic import robot_log_keyword, do_until_check, RfError, wait_until_stable
from movoid_debug import debug
from movoid_function import reset_function_default_value, decorate_class_function_exclude
from selenium.webdriver import Keys
from selenium.webdriver.remote.webelement import WebElement

from ..common import BasicCommon as Basic


@decorate_class_function_exclude(robot_log_keyword)
class SeleniumAction(Basic):
    def __init__(self):
        super().__init__()
        self._check_element_attribute_change_value: Union[str, None] = None
        self._check_element_count_value: Union[int, None] = None

    def selenium_take_full_screenshot(self, screenshot_name='python-screenshot.png'):
        """
        全窗口截屏，并保存文件
        :param screenshot_name: 截图名曾
        :return: (截图名称,截图路径) or cv全图片信息
        """
        return self.selenium_take_screenshot(image_name=screenshot_name)

    def selenium_click_element(self, click_locator, operate='click') -> bool:
        """
        点击某个元素，可以双击
        :param click_locator:点击元素的位置，可以使用locator或者Element
        :param operate: 默认为点击，输入 doubleclick 可以双击
        :return:
        """
        self.selenium_click_element_with_offset(click_locator, 0, 0, operate)
        return True

    def selenium_get_element_color_list(self, screenshot_locator=None) -> np.ndarray:
        """
        获得目标元素的颜色列表
        :param screenshot_locator: 目标元素或其locator。
        :return: 一个x*y*3的ndarray
        """
        img_array = self.selenium_log_screenshot(screenshot_locator)
        full_image = cv2.imdecode(img_array, cv2.COLOR_RGB2BGR)
        return full_image

    def selenium_click_element_with_offset(self, click_locator, x=0, y=0, operate='click') -> bool:
        """
        选择某个元素相对中心偏移一定距离的位置进行点击
        :param click_locator: 目标元素或者locator
        :param x: 横坐标像素数
        :param y: 纵坐标像素数
        :param operate: 默认点击，doubleclick为双击
        :return: True
        """
        tar_element = self.selenium_analyse_element(click_locator)
        self.action_chains.move_to_element_with_offset(tar_element, x, y)
        if operate == 'click':
            self.action_chains.click()
        elif operate in ('double_click', 'doubleclick'):
            self.action_chains.double_click()
        self.action_chains.perform()
        return True

    @robot_log_keyword(False)
    def selenium_check_element_attribute(self, check_locator, check_value, check_attribute='innerText', attribute_type='', regex: bool = True, check_bool: bool = True):
        """
        检查目标元素的属性是否满足某个条件
        :param check_locator: 检查目标的元素或locator
        :param check_value: 属性值
        :param check_attribute: 属性名
        :param attribute_type: 属性的类型，默认三个类型均搜索，可以输入以下其中之一：attribute、property、dom
        :param regex: 属性值是否为一个正则公式，默认为正则，如果输入False，那么需要属性值完全匹配
        :param check_bool: 是否为满足条件，默认为找到满足条件的元素。如果输入False，那么需要找到目标元素存在一个不满足条件的
        :return: 判定结果
        """
        tar_elements = self.selenium_analyse_elements(check_locator)
        tar_exist = False
        for i_element, one_element in enumerate(tar_elements):
            tar_value = self.selenium_get_locator_attribute(one_element, check_attribute, attribute_type)
            print(f'{check_attribute} of <{check_locator}>({i_element}) is:{tar_value}')
            if regex:
                check_result = bool(re.search(check_value, tar_value))
                print(f'{check_result}: <{check_value}> in <{tar_value}>')
            else:
                check_result = check_value == tar_value
                print(f'{check_result}: <{check_value}> == <{tar_value}>')
            tar_exist = tar_exist or check_result == check_bool
            print(f'{i_element}/{len(tar_elements)} is {check_result} -> {check_result == check_bool}')
        print(f'check result is:{tar_exist}')
        return tar_exist

    def selenium_find_elements_with_attribute(self, find_locator, find_value='', find_attribute='innerText', attribute_type='', regex=True, check_bool=True) -> List[WebElement]:
        """
        在所有目标元素中，寻找所有属性值满足需求的元素，并返回
        :param find_locator: 搜索目标元素或locator
        :param find_value: 所需要匹配的属性值
        :param find_attribute: 所需要寻找的属性
        :param attribute_type: 属性的类型，默认三个类型均搜索，可以输入以下其中之一：attribute、property、dom
        :param regex: 属性值是否为一个正则公式，默认为正则，如果输入False，那么需要属性值完全匹配
        :param check_bool: 是否为满足条件，默认为找到满足条件的元素。如果输入False，那么需要找到目标元素存在一个不满足条件的
        :return:
        """
        tar_elements = self.selenium_analyse_elements(find_locator)
        find_elements = []
        if find_attribute is None:
            find_elements = tar_elements
            print(f'find {len(find_elements)} elements only locator <{find_locator}>')
        else:
            print(f'find {len(tar_elements)} elements <{find_locator}> first')
            for i_element, one_element in enumerate(tar_elements):
                try:
                    tar_value = self.selenium_get_locator_attribute(one_element, find_attribute, attribute_type)
                except:
                    print(f'{find_attribute} of <{find_locator}>({i_element}) can not be read, pass it')
                    continue
                print(f'{find_attribute} of <{find_locator}>({i_element}) is:{tar_value}')
                if regex:
                    check_result = bool(re.search(str(find_value), tar_value))
                    print(f'{check_result}: <{find_value}> in <{tar_value}>')
                else:
                    check_result = find_value == tar_value
                    print(f'{check_result}: <{find_value}> == <{tar_value}>')
                if check_result == check_bool:
                    find_elements.append(one_element)
            print(f'find {len(find_elements)} elements <{find_locator}> <{find_attribute}> is <{find_value}>(regex={regex},check={check_bool})')
        return find_elements

    def selenium_find_element_with_attribute(self, find_locator, find_value='', find_attribute='innerText', attribute_type='', regex=True, check_bool=True) -> WebElement:
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
        """
        find_elements = self.selenium_find_elements_with_attribute(find_locator, find_value=find_value, find_attribute=find_attribute, attribute_type=attribute_type, regex=regex, check_bool=check_bool)
        if len(find_elements) == 0:
            raise RfError(f'fail to find <{find_locator}> with <{find_attribute}> is <{find_value}>(re={regex},bool={check_bool})')
        return find_elements[0]

    def selenium_get_locator_attribute(self, target_locator, target_attribute='innerText', attribute_type='') -> Any:
        """
        获取目标元素的属性的值
        :param target_locator: 目标元素或locator
        :param target_attribute: 属性名称
        :param attribute_type: 属性的类型，默认三个类型均搜索，可以输入以下其中之一：attribute、property、dom
        :return:
        """
        tar_element = self.selenium_analyse_element(target_locator)
        if attribute_type == 'attribute':
            re_value = tar_element.get_attribute(target_attribute)
        elif attribute_type == 'property':
            re_value = tar_element.get_property(target_attribute)
        elif attribute_type == 'dom':
            re_value = tar_element.get_dom_attribute(target_attribute)
        else:
            re_value = tar_element.get_attribute(target_attribute)
            re_value = tar_element.get_dom_attribute(target_attribute) if re_value is None else re_value
            re_value = tar_element.get_property(target_attribute) if re_value is None else re_value
        return re_value

    def selenium_new_screenshot_folder(self):
        screen_path = self.get_robot_variable("Screenshot_path")
        if screen_path:
            screen_pathlib = pathlib.Path(screen_path)
            if not screen_pathlib.exists():
                os.mkdir(screen_path)
                print('create dir : {}'.format(screen_path))

    def selenium_delete_elements(self, delete_locator) -> None:
        """
        在页面上把某个/些元素删除掉
        :param delete_locator: 待删除的元素或locator
        """
        elements = self.selenium_analyse_elements(delete_locator)
        print(f'find {len(elements)} elements:{delete_locator}')
        for one_element in elements:
            self.selenium_execute_js_script('arguments[0].remove();', one_element)
        print(f'delete all {len(elements)} elements:{delete_locator}')

    @robot_log_keyword(False)
    def selenium_check_contain_element(self, check_locator, check_exist: bool = True) -> bool:
        """
        检查页面内是否存在某个元素
        :param check_locator: 目标元素或locator
        :param check_exist: 默认检查存在。改为False后，改为检查页面中是否不存在这个元素
        :return: 搜素结果
        """
        find_elements = self.selenium_analyse_elements(check_locator)
        find_elements_bool = len(find_elements) > 0
        print(f'we find {find_elements_bool}→{check_exist} {check_locator}')
        return find_elements_bool == check_exist

    @robot_log_keyword(False)
    def selenium_check_contain_elements(self, check_locator, check_count: int = 1) -> bool:
        """
        检查页面内某些元素的总数是否为特定的值
        :param check_locator: 目标元素或locator
        :param check_count: 元素的数量
        :return: 搜索结果。只有正好数量相同才会返回True
        """
        check_count = int(check_count)
        find_elements = self.selenium_analyse_elements(check_locator)
        find_elements_num = len(find_elements)
        print(f'we find {find_elements_num}→{check_count} {check_locator}')
        return find_elements_num == check_count

    @robot_log_keyword(False)
    def selenium_check_element_attribute_change_init(self, check_locator, check_attribute='innerText', attribute_type='') -> bool:
        tar_element = self.selenium_analyse_element(check_locator)
        self._check_element_attribute_change_value = self.selenium_get_locator_attribute(tar_element, check_attribute, attribute_type)
        print(f'we find {check_attribute} of {check_locator} is {self._check_element_attribute_change_value}')
        return False

    @robot_log_keyword(False)
    def selenium_check_element_attribute_change_loop(self, check_locator, check_attribute='innerText', attribute_type='') -> bool:
        """
        :param check_locator: 待检查的元素或locator
        :param check_attribute: 检查的目标属性名
        :param attribute_type: 属性的类型，默认三个类型均搜索，可以输入以下其中之一：attribute、property、dom
        """
        tar_element = self.selenium_analyse_element(check_locator)
        temp_value = self.selenium_get_locator_attribute(tar_element, check_attribute, attribute_type)
        re_bool = self._check_element_attribute_change_value != temp_value
        print(f'we find {check_attribute} of {check_locator} is {temp_value}{"!=" if re_bool else "=="}{self._check_element_attribute_change_value}')
        return re_bool

    @robot_log_keyword(False)
    def selenium_check_element_count_change_init(self, check_locator) -> bool:
        self._check_element_count_value = len(self.selenium_analyse_elements(check_locator))
        print(f'we find {check_locator} count of {self._check_element_count_value}')
        return False

    @robot_log_keyword(False)
    def selenium_check_element_count_change_loop(self, check_locator) -> bool:
        """
        :param check_locator: 待检查的元素或locator
        """
        now_count = len(self.selenium_analyse_elements(check_locator))
        re_bool = now_count != self._check_element_count_value
        print(f'we find {check_locator} count of {now_count} {"!=" if re_bool else "=="}{self._check_element_count_value}')
        return re_bool

    @robot_log_keyword(False)
    def selenium_check_stable_element_attribute_unchanged_init(self, check_locator, check_attribute='innerText') -> bool:
        tar_element = self.selenium_analyse_element(check_locator)
        self._check_element_attribute_change_value = tar_element.get_attribute(check_attribute)
        return False

    @robot_log_keyword(False)
    def selenium_check_stable_element_attribute_unchanged_loop(self, check_locator, check_attribute='innerText') -> bool:
        """
        :param check_locator: 待检查的元素或locator
        :param check_attribute: 检查的目标属性名
        """
        tar_element = self.selenium_analyse_element(check_locator)
        temp_value = tar_element.get_attribute(check_attribute)
        re_bool = self._check_element_attribute_change_value == temp_value
        if re_bool is False:
            self._check_element_attribute_change_value = temp_value
        print(f'we find {check_attribute} of {check_locator} is {temp_value}{"==" if re_bool else "!="}{self._check_element_attribute_change_value}')
        return re_bool

    def always_true(self) -> bool:
        return True


@decorate_class_function_exclude(robot_log_keyword)
@decorate_class_function_exclude(debug, param=True, kwargs={'teardown_function': SeleniumAction.selenium_debug_teardown})
class SeleniumActionUntil(SeleniumAction):

    @do_until_check(SeleniumAction.always_true, SeleniumAction.selenium_click_element_with_offset)
    def selenium_click_until_available(self):
        """
        一直尝试点击某个元素，直至这个元素可以被点击并且成功被点击为止
        ******************** 下方是辅助函数和参数，请忽略return参数 ********************
        """
        pass

    @do_until_check(SeleniumAction.always_true, SeleniumAction.selenium_check_contain_element)
    def selenium_wait_until_find_element(self):
        """
        一直等待，直到在页面上寻找到某个元素为止
        ******************** 下方是辅助函数和参数，请忽略return参数 ********************
        """
        pass

    @reset_function_default_value(selenium_wait_until_find_element)
    def selenium_wait_until_not_find_element(self, check_exist=False):
        """
        :param check_exist: 现在默认值为False
        """
        pass

    @do_until_check(SeleniumAction.selenium_click_element_with_offset, SeleniumAction.selenium_check_contain_elements)
    def selenium_click_until_find_elements(self):
        """
        点击第一个元素，直到寻找到一定数量的第二个元素才停止点击。
        ******************** 下方是辅助函数和参数，请忽略return参数 ********************
        """
        pass

    @do_until_check(SeleniumAction.selenium_click_element_with_offset, SeleniumAction.selenium_check_contain_element)
    def selenium_click_until_find_element(self):
        """
        点击第一个元素，直到寻找到第二个元素才停止点击
        ******************** 下方是辅助函数和参数，请忽略return参数 ********************
        """
        pass

    @reset_function_default_value(selenium_click_until_find_element)
    def selenium_click_until_not_find_element(self, check_exist=False):
        """
        :param check_exist: 现在默认值为False
        """
        pass

    @do_until_check(SeleniumAction.always_true, SeleniumAction.selenium_find_element_with_attribute)
    def selenium_wait_until_find_element_attribute(self):
        """
        一直等待，直到第二组目标元素存在一个元素的属性值满足需求
        ******************** 下方是辅助函数和参数，请忽略return参数 ********************
        """
        pass

    @do_until_check(SeleniumAction.selenium_click_element_with_offset, SeleniumAction.selenium_find_element_with_attribute)
    def selenium_click_until_find_element_attribute(self):
        """
        点击第一个元素，直到在第二组目标元素中存在一个元素的属性值满足需求，才停止点击
        ******************** 下方是辅助函数和参数，请忽略return参数 ********************
        """
        pass

    @do_until_check(SeleniumAction.always_true, SeleniumAction.selenium_check_element_attribute_change_loop, init_check_function=SeleniumAction.selenium_check_element_attribute_change_init)
    def selenium_wait_until_attribute_change(self):
        """
        一直等待，直到目标元素的某个目标属性发生了变化
        ******************** 下方是辅助函数和参数，请忽略return参数 ********************
        """
        pass

    @do_until_check(SeleniumAction.selenium_click_element_with_offset, SeleniumAction.selenium_check_element_attribute_change_loop, init_check_function=SeleniumAction.selenium_check_element_attribute_change_init)
    def selenium_click_until_attribute_change(self):
        """
        一直点击第一个元素，直到第二组目标元素的某个目标属性发生了变化
        ******************** 下方是辅助函数和参数，请忽略return参数 ********************
        """
        pass

    @do_until_check(SeleniumAction.always_true, SeleniumAction.selenium_check_element_count_change_loop, init_check_function=SeleniumAction.selenium_check_element_count_change_init)
    def selenium_wait_until_element_count_change(self):
        """
        一直等待，直到目标元素的数量发生了变化
        ******************** 下方是辅助函数和参数，请忽略return参数 ********************
        """
        pass

    @do_until_check(SeleniumAction.selenium_click_element_with_offset, SeleniumAction.selenium_check_element_count_change_loop, init_check_function=SeleniumAction.selenium_check_element_count_change_init)
    def selenium_click_until_element_count_change(self):
        """
        一直点击第一个元素，直到第二组目标元素的数量发生了变化
        ******************** 下方是辅助函数和参数，请忽略return参数 ********************
        """
        pass

    @wait_until_stable(SeleniumAction.selenium_check_contain_element)
    def selenium_wait_until_stable_find_element(self):
        """
        一直等待，直到在界面上连续若干秒都能搜索到目标元素
        ******************** 下方是辅助函数和参数，请忽略return参数 ********************
        """
        pass

    @wait_until_stable(SeleniumAction.selenium_check_contain_elements)
    def selenium_wait_until_stable_find_elements(self):
        """
        一直等待，直到在界面上连续若干秒都能搜索到一定数量的目标元素
        ******************** 下方是辅助函数和参数，请忽略return参数 ********************
        """
        pass

    @reset_function_default_value(selenium_wait_until_stable_find_element)
    def selenium_wait_until_stable_not_find_element(self, check_exist=False):
        """
        :param check_exist: 现在默认值为False
        """
        pass

    @wait_until_stable(SeleniumAction.selenium_find_element_with_attribute)
    def selenium_wait_until_stable_find_element_attribute(self):
        """
        一直等待，直到在界面上连续若干秒都在目标元素内找到一个属性满足要求的元素
        ******************** 下方是辅助函数和参数，请忽略return参数 ********************
        """
        pass

    @wait_until_stable(SeleniumAction.selenium_check_stable_element_attribute_unchanged_loop, init_check_function=SeleniumAction.selenium_check_stable_element_attribute_unchanged_init)
    def selenium_wait_until_stable_attribute_unchanged(self):
        """
        一直等待，直到在界面上连续若干秒内目标元素的目标属性的属性值均未发生变化
        ******************** 下方是辅助函数和参数，请忽略return参数 ********************
        """
        pass

    def selenium_input_delete_all_and_input(self, input_locator, input_text, sleep_time=1.0, pass_when_same_input=True):
        """
        对input输入框删除所有内容后重新输入内容。
        如果输入完毕后，发现文本没有变为理想结果，将会尝试重试，重试最多5此
        输入成功，或者达成最多重试次数后，会点击Tab进行失焦
        :param input_locator: input输入框或其locator
        :param input_text: 待输入的文本
        :param sleep_time: 输入完毕后等待时间
        :param pass_when_same_input: 默认如果已有信息和目标文本一致，那么将会跳过这些操作。如果传入False，那么将总是重新输入
        """
        self.selenium_wait_until_find_element(input_locator)
        input_element = self.selenium_analyse_element(input_locator)
        print(f'try to input ({str(input_text)}) by ({input_text})')
        input_text = str(input_text)
        print(f'find element:{input_element.get_attribute("outerHTML")},')
        now_str = input_element.get_attribute('value')
        print(f'element has text({len(now_str)}):{now_str}')
        if now_str == str(input_text) and pass_when_same_input:
            print(f'it has already been {now_str}, pass input')
            input_element.send_keys(Keys.TAB)
        else:
            for input_retry in range(5):
                for backspace_count in range(len(now_str) + 2):
                    input_element.send_keys(Keys.BACKSPACE)
                now_str = self.selenium_get_locator_attribute(input_locator, "value")
                print(f'we try to delete all input text, and now it is >{now_str}<')
                for i in input_text:
                    input_element.send_keys(i)
                    time.sleep(0.01)
                now_str = self.selenium_get_locator_attribute(input_locator, 'value')
                print(f'we want >{input_text}< and got >{now_str}<')
                if str(now_str) == str(input_text):
                    break
                else:
                    print(f'input failed {input_retry} time, we try to input again')
                    time.sleep(0.1)
            input_element.send_keys(Keys.TAB)
            print(f'tab and leave input')
            time.sleep(sleep_time)
