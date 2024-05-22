# -*- coding: UTF-8 -*-

"""
@Project ：flask_frame 
@File    ：__init__.py.py
@IDE     ：PyCharm 
@Author  ：Ethan
@Date    ：2024/5/21 22:14 
"""
import os


def get_possible_system_name():
    """

    :return:
    """
    path_split = os.getcwd().split(os.sep)
    if 'src' in path_split:
        path_split = path_split[:path_split.index('src')]
    if len(path_split) > 2:
        return path_split[-2]


def get_possible_subsystem_name():
    """

    :return:
    """
    path_split = os.getcwd().split(os.sep)
    if 'src' in path_split:
        path_split = path_split[:path_split.index('src')]
    if len(path_split) > 2:
        default_sub = path_split[-1]
        return default_sub
