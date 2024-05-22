# -*- coding: UTF-8 -*-

"""
@Project ：flask_frame 
@File    ：str_util.py
@IDE     ：PyCharm 
@Author  ：Ethan
@Date    ：2024/5/22 22:29 
"""

from flask_frame.util.ascii_util import FormatCode


def highlight(target, color=FormatCode.Red, reset=FormatCode.Color_Off):
    """

    :param target:
    :param color:
    :param reset:
    :return:
    """
    return color + target + reset
