# -*- coding:utf-8 -*-
import tornado.web
import config

class BookModule(tornado.web.UIModule):
    def render(self, book):
        return self.render_string('modules/book.html', book=book, urls=urls)

class PptArticleModule(tornado.web.UIModule):
    def render(self, pptArticle, urls):
        return self.render_string('modules/pptArticle.html', pptArticle=pptArticle, urls=urls)

class ListArticleModule(tornado.web.UIModule):
    def render(self, article, urls):
        return self.render_string('modules/listArticle.html', article=article, urls=urls)