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
from typing import List, Union

import cv2
from RobotFrameworkBasic import robot_log_keyword, robot_no_log_keyword, do_until_check, do_when_error, RfError, wait_until_stable
from movoid_debug import debug
from movoid_function import reset_function_default_value, decorate_class_function_exclude
from movoid_package import importing
from selenium.webdriver import Keys
from selenium.webdriver.remote.webelement import WebElement

Basic = importing('..common', 'BasicCommon')


@decorate_class_function_exclude(robot_log_keyword)
class SeleniumAction(Basic):
    def __init__(self):
        super().__init__()
        self._check_element_attribute_change_value: Union[str, None] = None
        self._check_element_count_value: Union[int, None] = None

    def selenium_take_full_screenshot(self, screenshot_name='python-screenshot.png'):
        return self.selenium_take_screenshot(image_name=screenshot_name)

    def selenium_click_element(self, click_locator, operate='click'):
        self.selenium_click_element_with_offset(click_locator, 0, 0, operate)
        return True

    def selenium_get_element_color_list(self, screenshot_locator=None, image_name='catch-image-color.png', rename=True):
        tar_name, tar_path = self.selenium_take_screenshot(screenshot_locator, image_name, rename)
        print(f'try to read image:{tar_path}')
        return cv2.imread(tar_path)

    def selenium_click_element_with_offset(self, click_locator, x=0, y=0, operate='click'):
        tar_element = self.selenium_analyse_element(click_locator)
        self.action_chains.move_to_element_with_offset(tar_element, x, y)
        if operate == 'click':
            self.action_chains.click()
        elif operate in ('double_click', 'doubleclick'):
            self.action_chains.double_click()
        self.action_chains.perform()
        return True

    @robot_log_keyword(False)
    def selenium_check_element_attribute(self, check_locator, check_value, check_attribute='innerText', attribute_type='', regex=True, check_bool=True):
        """
        检查所有元素中，是否存在一个属性满足要求的元素
        :param check_locator: 元素定位
        :param check_value: 属性值
        :param check_attribute: 属性名
        :param attribute_type: 属性类型：attribute、dom、property
        :param regex: 是否做正则匹配
        :param check_bool: 要求满足条件还是不满足条件的
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

    def selenium_find_element_with_attribute(self, find_locator, find_value='', find_attribute='innerText', regex=True, check_bool=True):
        find_elements = self.selenium_find_elements_with_attribute(find_locator, find_value=find_value, find_attribute=find_attribute, regex=regex, check_bool=check_bool)
        if len(find_elements) == 0:
            raise RfError(f'fail to find <{find_locator}> with <{find_attribute}> is <{find_value}>(re={regex},bool={check_bool})')
        return find_elements[0]

    def selenium_get_locator_attribute(self, target_locator, target_attribute='innerText', attribute_type=''):
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

    def selenium_delete_elements(self, delete_locator):
        elements = self.selenium_analyse_elements(delete_locator)
        print(f'find {len(elements)} elements:{delete_locator}')
        for one_element in elements:
            self.selenium_execute_js_script('arguments[0].remove();', one_element)
        print(f'delete all {len(elements)} elements:{delete_locator}')

    def selenium_input_delete_all_and_input(self, input_locator, input_text, sleep_time=1.0, pass_when_same_input=True):
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

    @robot_log_keyword(False)
    def selenium_check_contain_element(self, check_locator, check_exist=True):
        find_elements = self.selenium_analyse_elements(check_locator)
        find_elements_bool = len(find_elements) > 0
        print(f'we find {find_elements_bool}→{check_exist} {check_locator}')
        return find_elements_bool == check_exist

    @robot_log_keyword(False)
    def selenium_check_contain_elements(self, check_locator, check_count=1):
        check_count = int(check_count)
        find_elements = self.selenium_analyse_elements(check_locator)
        find_elements_num = len(find_elements)
        print(f'we find {find_elements_num}→{check_count} {check_locator}')
        return find_elements_num == check_count

    @robot_log_keyword(False)
    def selenium_check_element_attribute_change_init(self, check_locator, check_attribute='innerText', attribute_type=''):
        tar_element = self.selenium_analyse_element(check_locator)
        self._check_element_attribute_change_value = self.selenium_get_locator_attribute(tar_element, check_attribute, attribute_type)
        print(f'we find {check_attribute} of {check_locator} is {self._check_element_attribute_change_value}')
        return False

    @robot_log_keyword(False)
    def selenium_check_element_attribute_change_loop(self, check_locator, check_attribute='innerText', attribute_type=''):
        tar_element = self.selenium_analyse_element(check_locator)
        temp_value = self.selenium_get_locator_attribute(tar_element, check_attribute, attribute_type)
        re_bool = self._check_element_attribute_change_value != temp_value
        print(f'we find {check_attribute} of {check_locator} is {temp_value}{"!=" if re_bool else "=="}{self._check_element_attribute_change_value}')
        return re_bool

    @robot_log_keyword(False)
    def selenium_check_element_count_change_init(self, check_locator):
        self._check_element_count_value = len(self.selenium_analyse_elements(check_locator))
        print(f'we find {check_locator} count of {self._check_element_count_value}')
        return False

    @robot_log_keyword(False)
    def selenium_check_element_count_change_loop(self, check_locator):
        now_count = len(self.selenium_analyse_elements(check_locator))
        re_bool = now_count != self._check_element_count_value
        print(f'we find {check_locator} count of {now_count} {"!=" if re_bool else "=="}{self._check_element_count_value}')
        return re_bool

    @robot_log_keyword(False)
    def selenium_check_stable_element_attribute_unchanged_init(self, check_locator, check_attribute='innerText'):
        tar_element = self.selenium_analyse_element(check_locator)
        self._check_element_attribute_change_value = tar_element.get_attribute(check_attribute)
        return False

    @robot_log_keyword(False)
    def selenium_check_stable_element_attribute_unchanged_loop(self, check_locator, check_attribute='innerText'):
        tar_element = self.selenium_analyse_element(check_locator)
        temp_value = tar_element.get_attribute(check_attribute)
        re_bool = self._check_element_attribute_change_value == temp_value
        if re_bool is False:
            self._check_element_attribute_change_value = temp_value
        print(f'we find {check_attribute} of {check_locator} is {temp_value}{"==" if re_bool else "!="}{self._check_element_attribute_change_value}')
        return re_bool

    def always_true(self):
        return True


@decorate_class_function_exclude(robot_log_keyword)
@decorate_class_function_exclude(debug, param=True, kwargs={'teardown_function': Basic.selenium_function_debug_continue_teardown})
class SeleniumActionUntil(SeleniumAction):

    @do_until_check(SeleniumAction.always_true, SeleniumAction.selenium_click_element_with_offset)
    def selenium_click_until_available(self):
        pass

    @debug(teardown_function=Basic.selenium_function_debug_continue_teardown)
    @do_until_check(SeleniumAction.always_true, SeleniumAction.selenium_check_contain_element)
    def selenium_wait_until_find_element(self):
        pass

    @reset_function_default_value(selenium_wait_until_find_element)
    def selenium_wait_until_not_find_element(self, check_exist=False):
        pass

    @debug(teardown_function=Basic.selenium_function_debug_continue_teardown)
    @do_until_check(SeleniumAction.selenium_click_element_with_offset, SeleniumAction.selenium_check_contain_elements)
    def selenium_click_until_find_elements(self):
        pass

    @debug(teardown_function=Basic.selenium_function_debug_continue_teardown)
    @do_until_check(SeleniumAction.selenium_click_element_with_offset, SeleniumAction.selenium_check_contain_element)
    def selenium_click_until_find_element(self):
        pass

    @reset_function_default_value(selenium_click_until_find_element)
    def selenium_click_until_not_find_element(self, check_exist=False):
        pass

    @debug(teardown_function=Basic.selenium_function_debug_continue_teardown)
    @do_until_check(SeleniumAction.selenium_click_element_with_offset, SeleniumAction.selenium_check_contain_elements)
    def selenium_click_until_find_elements(self):
        pass

    @debug(teardown_function=Basic.selenium_function_debug_continue_teardown)
    @do_until_check(SeleniumAction.always_true, SeleniumAction.selenium_find_element_with_attribute)
    def selenium_wait_until_find_element_attribute(self):
        pass

    @debug(teardown_function=Basic.selenium_function_debug_continue_teardown)
    @do_until_check(SeleniumAction.selenium_click_element_with_offset, SeleniumAction.selenium_find_element_with_attribute)
    def selenium_click_until_find_element_attribute(self):
        pass

    @debug(teardown_function=Basic.selenium_function_debug_continue_teardown)
    @do_until_check(SeleniumAction.always_true, SeleniumAction.selenium_check_element_attribute_change_loop, init_check_function=SeleniumAction.selenium_check_element_attribute_change_init)
    def selenium_wait_until_attribute_change(self):
        pass

    @debug(teardown_function=Basic.selenium_function_debug_continue_teardown)
    @do_until_check(SeleniumAction.selenium_click_element_with_offset, SeleniumAction.selenium_check_element_attribute_change_loop, init_check_function=SeleniumAction.selenium_check_element_attribute_change_init)
    def selenium_click_until_attribute_change(self):
        pass

    @debug(teardown_function=Basic.selenium_function_debug_continue_teardown)
    @do_until_check(SeleniumAction.always_true, SeleniumAction.selenium_check_element_count_change_loop, init_check_function=SeleniumAction.selenium_check_element_count_change_init)
    def selenium_wait_until_element_count_change(self):
        pass

    @debug(teardown_function=Basic.selenium_function_debug_continue_teardown)
    @do_until_check(SeleniumAction.selenium_click_element_with_offset, SeleniumAction.selenium_check_element_count_change_loop, init_check_function=SeleniumAction.selenium_check_element_count_change_init)
    def selenium_click_until_element_count_change(self):
        pass

    @debug(teardown_function=Basic.selenium_function_debug_continue_teardown)
    @wait_until_stable(SeleniumAction.selenium_check_contain_element)
    def selenium_wait_until_stable_find_element(self):
        pass

    @debug(teardown_function=Basic.selenium_function_debug_continue_teardown)
    @wait_until_stable(SeleniumAction.selenium_check_contain_elements)
    def selenium_wait_until_stable_find_elements(self):
        pass

    @reset_function_default_value(selenium_wait_until_stable_find_element)
    def selenium_wait_until_stable_not_find_element(self, check_exist=False):
        pass

    @debug(teardown_function=Basic.selenium_function_debug_continue_teardown)
    @wait_until_stable(SeleniumAction.selenium_find_element_with_attribute)
    def selenium_wait_until_stable_find_element_attribute(self):
        pass

    @debug(teardown_function=Basic.selenium_function_debug_continue_teardown)
    @wait_until_stable(SeleniumAction.selenium_check_stable_element_attribute_unchanged_loop, init_check_function=SeleniumAction.selenium_check_stable_element_attribute_unchanged_init)
    def selenium_wait_until_stable_attribute_unchanged(self):
        pass
