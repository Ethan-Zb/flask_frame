# -*- coding: UTF-8 -*-

"""
@Project ：flask_frame 
@File    ：web_socket_initialized.py
@IDE     ：PyCharm 
@Author  ：Ethan
@Date    ：2024/5/22 22:27 
"""

from flask_frame.scope.scope import Scope
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import parse_command_line
from tornado.web import RequestHandler

from flask_frame.logger import logger
from flask_frame.util.str_util import get_snake_case
from flask_frame.web_socket_app import get_web_socket_resource, get_web_resource, RegisterApplication, ChatRoom


class Alive(RequestHandler):
    def get(self, *args, **kwargs):
        logger.info('alive success')
        return self.write('yes')


class Stats(RequestHandler):
    def get(self, *args, **kwargs):
        return self.write(ChatRoom.chat_stats)


def init(
        web_socket_port,
        tornado_proc_num,
        settings: dict,
        ssl_options=None,
):
    prefix = Scope.get_url_prefix()
    web_socket_route_list = _load_route(type='web_socket')
    web_route_list = _load_route(type='web')

    handlers = [(r'{}/v{}/alive'.format(prefix, 1), Alive),
                (r'{}/v{}/stats'.format(prefix, 1), Stats)]

    for resource, routes, kwargs in web_socket_route_list:
        handlers.append((r'{}'.format(routes[0]), resource))

    for resource, routes, kwargs in web_route_list:
        handlers.append((r'{}'.format(routes[0]), resource))

    settings.update({
        'template_path': 'templates',
        'static_path': 'static'
    })

    logger.debug('web_socket_handlers is {}'.format(handlers))
    app = RegisterApplication(handlers, settings)
    start_web_socket(app, web_socket_port, tornado_proc_num, ssl_options)

    return app


def start_web_socket(app, web_socket_port, tornado_proc_num, ssl_options):
    parse_command_line()
    if ssl_options:
        http_server = HTTPServer(app, ssl_options=ssl_options)
    else:
        http_server = HTTPServer(app)

    http_server.bind(web_socket_port)
    http_server.start(tornado_proc_num)  # Fork 多个子进程
    IOLoop.current().start()


def _load_route(type):
    route_list = []
    if type == 'web_socket':
        for resource, version in get_web_socket_resource():
            endpoint = resource.__name__.lower() + version
            url_list = tuple(get_url_list(resource, version))
            if url_list:
                route_list.append((resource, url_list, {'endpoint': endpoint}))

    elif type == 'web':
        for resource, version in get_web_resource():
            endpoint = resource.__name__.lower() + version
            url_list = tuple(get_url_list(resource, version))
            if url_list:
                route_list.append((resource, url_list, {'endpoint': endpoint}))
    return route_list


def get_url_list(value, version):
    prefix = '{}/{}/'.format(Scope.get_url_prefix(), version)
    return [prefix + get_snake_case(value.__name__)]
