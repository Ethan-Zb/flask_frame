# -*- coding: UTF-8 -*-

"""
@Project ：flask_frame 
@File    ：level.py
@IDE     ：PyCharm 
@Author  ：Ethan
@Date    ：2024/5/22 22:31 
"""


class Level:
    TRACE = 5  # you don't care
    DEBUG = 10  # don't care neither
    INFO = 20  # neither
    WARNING = 30  # just care little
    ERROR = 40  # when something wrong
    CRITICAL = 50  # when very much errors, you must know it.
    EMERGENCY = 60  # some dirty data will be added to db, or your money is flying away, you must stop it
    DOOM = 100000  # when it is doomsday. there is nothing you can do but asking your god for help if you believe one.
