# -*- coding:utf-8 -*-
import tornado.web
import config

class ArticleHandler(tornado.web.RequestHandler):
    def get(self, input):
        articleId=input[::1]
        article=self.getArticle(articleId)
        self.render(
            "article.html",
            article=article,
        )
    def getArticle(self, articleId):
        article={
            "title":"一个“好人”如何去挽回失去的爱情2",
            "image":"/static/images/website5.jpg",
            "date":"2015-7-07",
            "brief":"第一，不要纠结于过去，承认你们的关系已经破裂。盗哥讲过，不要把过去的承诺拿到现在来用，一切的承诺仅仅限于女孩对你当时的感觉和情绪。感觉和情绪一去不复返， 现在有的只有厌烦，之前的所有兴趣都成为过去。承认关系已经破裂，你现在需要做的不是纠缠，而是想如何正确的去修复……",
            "type_id":"1",
            "writer":"aboutLove",
            "content":"不要纠结于过去，承认你们的关系已经破裂。盗哥讲过，不要把过去的承诺拿到现在来用，一切的承诺仅仅限于女孩对你当时的感觉和情绪。"
        }
        return article