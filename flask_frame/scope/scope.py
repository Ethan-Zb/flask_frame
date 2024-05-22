# -*- coding: UTF-8 -*-

"""
@Project ：flask_frame 
@File    ：scope.py
@IDE     ：PyCharm 
@Author  ：Ethan
@Date    ：2024/5/22 22:36 
"""

from functools import lru_cache

from flask_frame.const import get_const_system_name, get_const_subsystem_name
from flask_frame.util import get_possible_system_name, get_possible_subsystem_name


class Scope:
    GLOBAL = 'global'
    SYSTEM = 'system'
    SUBSYSTEM = 'subsystem'
    __global_name = 'ethan'
    __system_name = None
    __subsystem_name = None

    @classmethod
    def set_scope(
            cls,
            system_name,
            subsystem_name=None,
    ):
        cls.__system_name = system_name
        cls.__subsystem_name = subsystem_name

    @classmethod
    @lru_cache()
    def get_system_name(cls):
        """

        :return:
        """
        return cls.__system_name or get_const_system_name() or get_possible_system_name()

    @classmethod
    @lru_cache()
    def get_subsystem_name(cls):
        """

        :return:
        """
        subsystem_name = cls.__subsystem_name or get_const_subsystem_name() or get_possible_subsystem_name()
        prefix = cls.get_system_name() + '_'
        if subsystem_name.startswith(prefix):
            subsystem_name = subsystem_name[len(prefix):]
        return subsystem_name

    @classmethod
    @lru_cache()
    def get_subsystem_full_name(cls):
        """

        :return:
        """
        return '{}_{}'.format(
            cls.get_system_name(), cls.get_subsystem_name()
        )

    @classmethod
    @lru_cache()
    def get_scope_name(cls, scope: str) -> str:
        """

        :param scope:
        :return:
        """
        prefix_mapper = {
            Scope.GLOBAL: cls.__global_name,
            Scope.SYSTEM: cls.get_system_name(),
            Scope.SUBSYSTEM: cls.get_subsystem_full_name()
        }
        return prefix_mapper.get(scope, cls.get_subsystem_name())

    @classmethod
    @lru_cache()
    def get_url_prefix(cls) -> str:
        """

        :return:
        """
        return '/{}/{}/api'.format(cls.get_system_name(), cls.get_subsystem_name())

    @classmethod
    @lru_cache()
    def get_admin_prefix(cls) -> str:
        """

        :return:
        """
        return '/{}/{}/admin'.format(cls.get_system_name(), cls.get_subsystem_name())
