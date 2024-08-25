#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# File          : __init__.py
# Author        : Sun YiFan-Movoid
# Time          : 2024/1/30 21:16
# Description   : 
"""
from .action import SeleniumActionUntil


class RobotSeleniumBasic(SeleniumActionUntil):
    pass


class RobotFrameworkSelenium(RobotSeleniumBasic):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
