#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import define, options

from urls import handlers
from data import Trie

version = sys.version_info[0]
if version < 3:
    reload(sys)
    sys.setdefaultencoding('utf-8')

define('port', default=9600, help='run tornado app on the given port', type=int)

class App(tornado.web.Application):
    def __init__(self):
        settings = dict(
            static_path = os.path.join(os.path.dirname(__file__), "static"),
            template_path = os.path.join(os.path.dirname(__file__), "templates"),
        )
        super(App, self).__init__(handlers, **settings)

def main():
    Trie.parseTxt()
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(App())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()