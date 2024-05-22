# -*- coding: UTF-8 -*-

"""
@Project ：flask_frame 
@File    ：project_generator.py
@IDE     ：PyCharm 
@Author  ：Ethan
@Date    ：2024/5/21 22:21 
"""

import getpass
import os

import pkg_resources
from flask_frame.const.common_const import CommonConst
from flask_frame.util.date_util import get_date
from flask_frame.util.file_util import ensure_dir, ensure_file

from flask_frame import SYSTEM_CONFIG
from flask_frame.util import get_possible_system_name, get_possible_subsystem_name

greeting = 'Welcome to use flask_frame project generator!'
promotes = {
    'a': '(a)all',
    'm': '(m)mysql',
    'e': '(e)elasticsearch',
    'r': '(r)redis',
    'c': '(c)celery',
    'f': '(f)flask',
    'h': '(h)hbase',
    'q': '(q)queue',
    's': '(s)statistic',
    'o': '(o)mongo'
}
config = dict(date=get_date())


def promote(chosen, remains):
    return '''Please choose features you want. use `+` or `-` to add or remove features. `#` for confirm.
for example: `+rf-e#` means `add redis,flask; remove elasticsearch; confirm`. 
current chosen: [{}], 
remains: [{}]
(default: all)>>>'''.format(','.join(chosen), ','.join(remains))


def copy_all(path):
    for file_name in _list_dir(path):
        copy(path, file_name, rename=None)


def copy(path, file_name='__init__.py', rename=None, target_path=None):
    rename = rename or file_name
    target_path = target_path or path
    file_path = '{}/{}'.format(target_path, rename)
    ensure_file(file_path)
    with open(file_path, 'w') as file:
        content = pkg_resources.resource_string('flask_frame', 'dev_tool/sample_project/{}/{}'.format(path, file_name))
        file.write(content.decode().format(file_name=rename.rstrip('.py'), **config))


def get_configs(name, attr_dict: dict):
    intent = '      '
    return '{}:\n{}{}'.format(name, intent, '\n{}'.format(intent).join([
        '{}: {}'.format(key.lower(), value)
        for key, value in attr_dict.items()
    ]))


def build_by_chosen(chosen):
    initializer_list = []
    settings = []
    subsystem_name = config['subsystem_name']
    system_name = config['system_name']
    if chosen:
        if not (len(chosen) == 1 and chosen[0] == promotes['f']):
            settings.append('global:')
    if promotes['m'] in chosen or promotes['h'] in chosen:
        copy_all('src/model')
    if promotes['m'] in chosen:
        copy_all('src/model/mysql_model')
        initializer_list.append('builder.init_mysql()')
        settings.append(get_configs('mysql', {
            'mysql_url': 'mysql+pymysql://user:password@127.0.0.1:3306/db_name?charset=utf8',
            'mysql_pool_size': 64,
            'mysql_max_overflow': 64,
            'mysql_pool_recycle': 3600
        }))
    if promotes['o'] in chosen:
        copy_all('src/model/mongo_model')
        initializer_list.append('builder.init_mongo()')
        settings.append(get_configs('mongo', {
            SYSTEM_CONFIG.MONGO_HOST_SETTING_KEY.lower(): '127.0.0.1',
            SYSTEM_CONFIG.MONGO_PORT_SETTING_KEY.lower(): 27017,
            SYSTEM_CONFIG.MONGO_USERNAME_SETTING_KEY.lower(): '',
            SYSTEM_CONFIG.MONGO_PASSWORD_SETTING_KEY.lower(): '',

        }))
    if promotes['h'] in chosen:
        copy_all('src/model/hbase_model')
        initializer_list.append('builder.init_hbase()')
        settings.append(get_configs('hbase', {
            'hbase_host': '127.0.0.1',
            'hbase_port': 9090,
            'hbase_pool_size': 64,
            'hbase_timeout': 60000
        }))

    if promotes['s'] in chosen or promotes['q'] in chosen:
        copy('src/manager', '__init__.py')
        if promotes['s'] in chosen:
            copy('src/manager', 'statistic_manager.py')
        if promotes['q'] in chosen:
            copy('src/manager', 'queue_manager.py')

    if promotes['r'] in chosen or promotes['s'] in chosen:
        initializer_list.append('builder.init_redis()')
        settings.append(get_configs('redis', {
            SYSTEM_CONFIG.REDIS_HOST_SETTING_KEY: '127.0.0.1',
            SYSTEM_CONFIG.REDIS_PORT_SETTING_KEY: 6379,
            SYSTEM_CONFIG.REDIS_PASSWORD_SETTING_KEY: '',
            SYSTEM_CONFIG.REDIS_DB_SETTING_KEY: 0,
            SYSTEM_CONFIG.REDIS_DEFAULT_EXPIRE_SETTING_KEY: 3 * CommonConst.MONTH_SECONDS
        }))
    if promotes['c'] in chosen:
        ensure_dir('doc/celery')
        copy('src/task/celery_task')
        copy('src/task/celery_task/system_name', target_path='src/task/celery_task/' + system_name)
        copy('src/task/celery_task/system_name/subsystem_name',
             target_path='src/task/celery_task/{}/{}'.format(system_name, subsystem_name))
        copy('src/task/celery_task/system_name/subsystem_name', 'demo.py',
             target_path='src/task/celery_task/{}/{}'.format(system_name, subsystem_name))
        # copy('src/task/celery_task', 'demo.py', '{}.py'.format(subsystem_name))
        # copy('src/task/celery_beat_task')
        # copy('src/task/celery_beat_task', 'demo.py', '{}.py'.format(subsystem_name))
        # copy_all('src/task/celery_external_task')
        # copy_all('src/task/celery_external_task/external_system_name')
        initializer_list.append('builder.init_celery()')
        settings.append(get_configs('celery', {
            'broker_url': ' amqp://guest:guest@127.0.0.1:5672//',
            'backend_url': 'redis://127.0.0.1:6379/0'
        }))
    if promotes['f'] in chosen:
        ensure_dir('doc/restful/')
        copy_all('src/api/v1')
        copy_all('src/api/')
        initializer_list.append('builder.init_flask()')

    return '\n    '.join(initializer_list), '\n    '.join(settings)


def _list_dir(path):
    for file_name in pkg_resources.resource_listdir('flask_frame', 'dev_tool/sample_project/{}'.format(path)):
        if pkg_resources.resource_isdir('flask_frame', 'dev_tool/sample_project/{}/{}'.format(path, file_name)):
            continue
        yield file_name


def generate():
    chosen = set()
    remains = set(promotes.values())
    print(greeting)
    command = input(promote(chosen, remains))
    if not command:
        command = 'a#'

    end = False
    while not end:
        current_style = '+'
        for char in command:
            if char in ['+', '-']:
                current_style = char
            if char in promotes:
                item = promotes[char]
                if current_style == '+':
                    chosen.add(item)
                    remains.discard(item)
                if current_style == '-':
                    chosen.discard(item)
                    remains.add(item)
            if char == 'a':
                if current_style == '+':
                    chosen = set(promotes.values())
                    remains = set()
                if current_style == '-':
                    chosen = set()
                    remains = set(promotes.values())
            if char == '#':
                end = True
                break
        else:
            command = input(promote(chosen, remains))

    path_split = os.getcwd().split(os.sep)
    default_sys, default_sub = 'flask_frame', 'demo'
    if len(path_split) > 2:
        default_sys, default_sub = get_possible_system_name(), get_possible_subsystem_name()
    try:
        default_author = getpass.getuser()
    except:
        default_author = 'jing'

    system_name = input('please input system name.(default:{}): >>>'.format(default_sys)) or default_sys
    subsystem_name = input('please input subsystem name(default:{}): >>>'.format(default_sub)) or default_sub
    author = input('please input author name(default:{}): >>>'.format(default_author)) or default_author

    config.update(dict(subsystem_name=subsystem_name, system_name=system_name, author=author))

    ensure_dir('src')
    ensure_dir('test')
    ensure_dir('doc')
    ensure_dir('doc')
    ensure_dir('script')

    copy_all('src/service')
    copy_all('src/orm')
    copy_all('src/task')
    copy_all('src/task/cyclic_task')
    copy_all('src/task/instance_task')

    init_lines, setting_lines = build_by_chosen(chosen)

    for file_name in _list_dir('src'):
        with open('src/{}'.format(file_name), 'w') as file:
            content = pkg_resources.resource_string(
                'flask_frame', 'dev_tool/sample_project/src/{}'.format(file_name)).decode()
            formatter = {}
            formatter.update(config)
            if '{sys}' in content:
                formatter['sys'] = system_name
            if '{sub}' in content:
                formatter['sub'] = subsystem_name
            if '{init_lines}' in content:
                formatter['init_lines'] = init_lines
            if '{setting_lines}' in content:
                formatter['setting_lines'] = setting_lines
            if formatter:
                content = content.format(**formatter)
            file.write(content)
