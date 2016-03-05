# -*- coding:utf-8 -*-
import tornado.web
import config
import common
from MongoService import MongoService

class ArticleHandler(tornado.web.RequestHandler):
    def get(self, input):
        articleId=input[::1]
        article=self.getArticle(articleId)
        self.render(
            "article.html",
            article=article,
        )
    def getArticle(self, articleId):
        mark = common.getMark()
        mongoService = MongoService()
        article = mongoService.getArticles(articleId, mark)
        return article