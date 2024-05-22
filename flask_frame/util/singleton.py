# -*- coding: UTF-8 -*-

"""
@Project ：flask_frame 
@File    ：singleton.py
@IDE     ：PyCharm 
@Author  ：Ethan
@Date    ：2024/5/21 22:15 
"""


class Singleton(type):
    """meta class of singleton"""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
