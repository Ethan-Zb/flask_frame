# -*- coding: UTF-8 -*-

"""
@Project ：flask_frame
@File    ：__init__.py.py
@IDE     ：PyCharm 
@Author  ：Ethan
@Date    ：2024/5/21 22:01 
"""

import threading
from multiprocessing import Manager

from flask_frame.abstract_system_config import AbstractSystemConfig

__author__ = 'ethan'
__version__ = '0.0.1'

# from flask_frame.util.ascii_util import colored_print
print("""
------------------------------------------------------------
version: {}
""".format(__version__))

try:
    module = __import__('system_config').SYSTEM_CONFIG
    if isinstance(module, AbstractSystemConfig):
        SYSTEM_CONFIG = module
    else:
        raise AttributeError

except (ImportError, AttributeError):
    SYSTEM_CONFIG = AbstractSystemConfig()

shared_memory = Manager()
thread_local = threading.local()
