# -*- coding: UTF-8 -*-

"""
@Project ：flask_frame 
@File    ：__init__.py.py
@IDE     ：PyCharm 
@Author  ：Ethan
@Date    ：2024/5/22 22:40 
"""
from flask_frame import SYSTEM_CONFIG


def get_const_system_name():
    """

    :return:
    """
    try:
        const_model = __import__(SYSTEM_CONFIG.CONST_MODULE_NAME)
        return const_model.CONST.SYSTEM_NAME
    except:
        return None


def get_const_subsystem_name():
    """

    :return:
    """
    try:
        const_model = __import__(SYSTEM_CONFIG.CONST_MODULE_NAME)
        return const_model.CONST.SUBSYSTEM_NAME  # type:str
    except:
        return None
