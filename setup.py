# -*- coding: UTF-8 -*-

"""
@Project ：flask_temp 
@File    ：setup.py
@IDE     ：PyCharm 
@Author  ：Ethan
@Date    ：2024/5/21 21:58 
"""


import flask_frame

from setuptools import setup, find_packages

setup(
    name='flask_frame',
    version=flask_frame.__version__,
    description='flask frame',
    author='Ethan',
    author_email='',
    packages=find_packages('.', include=['flask_frame', 'flask_frame.*']),
    install_requires=[
        'celery == 4.4.7',
        'elasticsearch5 == 5.5.6',
        'fakeredis == 1.4.3',
        'Flask == 1.1.2',
        'Flask-RESTful == 0.3.8',
        'gevent == 20.9.0',
        'happybase == 1.2.0',
        'jsonschema == 3.2.0',
        'kombu == 4.6.10',
        'pymongo == 3.11.0',
        'python-etcd == 0.4.5',
        'PyYAML == 5.3.1',
        'redis == 3.5.3',
        'requests == 2.24.0',
        'SQLAlchemy == 1.2.12',
        'thriftpy == 0.3.9',
        'tornado == 6.0.4',
        'tzlocal == 2.1',
        'werkzeug >= 0.14.1',
        'future >= 0.18.2',
        'mongoengine == 0.20.0',
        'blinker == 1.4'
    ],
    include_package_data=True,
)

