# -*- coding:utf-8 -*-
import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
import os.path
import MySQLdb

import config
from MainHandler import MainHandler
from ArticleHandler import ArticleHandler
from ListHandler import ListHandler
from Module import BookModule, PptArticleModule, ListArticleModule

from tornado.options import define, options
define("port", default=8000, help="run on given port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers=[
            (r"/", MainHandler),
            (r"/list/(\w+)", ListHandler),
            (r"/article/(\w+)", ArticleHandler),
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__),"templates"),
            static_path=os.path.join(os.path.dirname(__file__),"static"),
            debug=True,
            ui_modules={'Book': BookModule, 'PptArticle':PptArticleModule, 'ListArticle':ListArticleModule},
        )
        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == '__main__':
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
