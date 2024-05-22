# -*- coding: UTF-8 -*-

"""
@Project ：flask_frame 
@File    ：__init__.py.py
@IDE     ：PyCharm 
@Author  ：Ethan
@Date    ：2024/5/22 22:28 
"""
import logging
import traceback
from datetime import datetime

import requests
from flask_frame.scope.scope import Scope
from flask_frame.util.ascii_util import FormatCode
from flask_frame.util.conversion import convert_method_to_static
from flask_frame.util.level import Level

from flask_frame.util.str_util import highlight

TRACE = 5


def init_logger_level():
    """
    register logger level TRACE
    :return: None
    """
    logging.addLevelName(TRACE, 'TRACE')


class Log(logging.Logger):
    """
    Proxy logger class
    """

    @classmethod
    def initialize(cls, logger_object: logging.Logger):
        """
        convert methods of the `logger_object` to class methods
        :param logger_object: logger object
        :return:
        """
        convert_method_to_static(cls, logger_object)

        def trace(trace_id, msg, *args, **kwargs):
            if trace_id:
                msg = '[{}]{}'.format(trace_id, msg)
            if logger_object.isEnabledFor(TRACE):
                logger_object._log(TRACE, msg, args, **kwargs)  # pylint:disable=protected-access

        cls.trace = trace

    @staticmethod
    def debug(msg, *args, **kwargs):
        try:
            print('msg:{},args:{},kwargs:{}'.format(msg, args, kwargs))
        except Exception as e:
            pass

    @staticmethod
    def warning(msg, *args, **kwargs):
        try:
            print('msg:{},args:{},kwargs:{}'.format(msg, args, kwargs))
        except Exception as e:
            pass

    @staticmethod
    def info(msg, *args, **kwargs):
        try:
            print('msg:{},args:{},kwargs:{}'.format(msg, args, kwargs))
        except Exception as e:
            pass

    @staticmethod
    def error(msg, *args, **kwargs):
        try:
            print('msg:{},args:{},kwargs:{}'.format(msg, args, kwargs))
        except Exception as e:
            pass

    @staticmethod
    def exception(msg, *args, exc_info=True, **kwargs):
        try:
            print('msg:{},args:{},kwargs:{},traceback:{}'.format(msg, args, kwargs, traceback.format_exc()))
        except Exception as e:
            pass

    @staticmethod
    def critical(msg, *args, **kwargs):
        try:
            print('msg:{},args:{},kwargs:{}'.format(msg, args, kwargs))
        except Exception as e:
            pass

    @staticmethod
    def trace(trace_id, msg, *args, **kwargs):
        try:
            print('trace_id:{},msg:{},args:{},kwargs:{}'.format(trace_id, msg, args, kwargs))
        except Exception as e:
            pass

    @classmethod
    def highlight(cls, msg, color=FormatCode.Red, method=None, *args, **kwargs):
        method = method or cls.info
        method(highlight(msg, color), *args, **kwargs)

    @classmethod
    def alarm(cls, level=Level.CRITICAL, msg='known error', title='', data=None):
        from flask_frame.logger.logger_context import _get_logger_method
        method = _get_logger_method(level)
        method(msg)

        routing_data = {'service': '{}.{}'.format(
            Scope.get_system_name(), Scope.get_subsystem_name()
        )}
        if data:
            routing_data.update(data)

        message = {
            'title': title,
            'content': msg,
            'level': level,
            'time': str(datetime.now()),
            'routing_data': routing_data
        }
        from flask_frame.setting import get_setting
        from flask_frame import SYSTEM_CONFIG
        alarm_celery_task_broker = get_setting(SYSTEM_CONFIG.ALARM_CELERY_TASK_BROKER_SETTING_KEY, None)
        alarm_celery_task_name = get_setting(SYSTEM_CONFIG.ALARM_CELERY_TASK_NAME_SETTING_KEY, None)
        if alarm_celery_task_name:
            from flask_frame.celery_app.celery_app_initializer import send_task
            send_task(alarm_celery_task_name, args=(message,), broker_url=alarm_celery_task_broker)
        else:
            alarm_service_url = get_setting(SYSTEM_CONFIG.ALARM_SERVICE_URL_SETTING_KEY, None)
            if not alarm_service_url:

                try:
                    requests.post(alarm_service_url, json=message)
                    return
                except:
                    pass
            # deal with error
            cls.warning('not found alarm service. maybe you forgot set {}. msg is {}.'.format(
                [
                    SYSTEM_CONFIG.ALARM_CELERY_TASK_BROKER_SETTING_KEY,
                    SYSTEM_CONFIG.ALARM_CELERY_TASK_NAME_SETTING_KEY,
                    SYSTEM_CONFIG.ALARM_SERVICE_URL_SETTING_KEY
                ], msg
            ))

    @classmethod
    def emergency(cls, msg='known error', title='', data=None):
        cls.alarm(level=Level.EMERGENCY, msg=msg, title=title, data=data)


logger = Log  # pylint:disable=invalid-name
