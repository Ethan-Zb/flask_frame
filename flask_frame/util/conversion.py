# -*- coding: UTF-8 -*-

"""
@Project ：flask_frame 
@File    ：conversion.py
@IDE     ：PyCharm 
@Author  ：Ethan
@Date    ：2024/5/22 22:33 
"""


def convert_method_to_static(cls, obj):
    """

    :param cls:
    :param obj:
    :return:
    """
    for attr in dir(obj):
        if attr.startswith('_'):
            continue

        setattr(cls, attr, getattr(obj, attr))
