# -*- coding:utf-8 -*-
import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
import os.path
import MySQLdb

from tornado.options import define, options
define("port", default=8000, help="run on given port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers=[
            (r"/", MainHandler),
            (r"/list/(\w+)", ListHandler),
            (r"/recommended", RecommendedHandler),
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__),"templates"),
            static_path=os.path.join(os.path.dirname(__file__),"static"),
            debug=True,
            ui_modules={'Book': BookModule,'PptArticle':PptArticleModule},
        )
        tornado.web.Application.__init__(self, handlers, **settings)

class ListHandler(tornado.web.RequestHandler):
    def getArticles(self, theme_articles):
        listArticle={}
        for theme in theme_articles:
            if (theme['type']==input[::-1]):
                listArticle = theme['articles']
        return listArticle

    def get(self, input):
        theme_articles=[
            {
                "type":0,
                "articles":[
                    {
                        "title":"一个“好人”如何去挽回失去的爱情",
                        "image":"/static/images/website4.jpg",
                        "brief":"第一，不要纠结于过去，承认你们的关系已经破裂。盗哥讲过，不要把过去的承诺拿到现在来用，一切的承诺仅仅限于女孩对你当时的感觉和情绪。感觉和情绪一去不复返， 现在有的只有厌烦，之前的所有兴趣都成为过去。承认关系已经破裂，你现在需要做的不是纠缠，而是想如何正确的去修复……",
                        "type_id":"0"
                    },
                ]
            },
            {
                "type":1,
                "articles":[
                    {
                        "title":"一个“好人”如何去挽回失去的爱情2",
                        "image":"/static/images/website5.jpg",
                        "brief":"第一，不要纠结于过去，承认你们的关系已经破裂。盗哥讲过，不要把过去的承诺拿到现在来用，一切的承诺仅仅限于女孩对你当时的感觉和情绪。感觉和情绪一去不复返， 现在有的只有厌烦，之前的所有兴趣都成为过去。承认关系已经破裂，你现在需要做的不是纠缠，而是想如何正确的去修复……",
                        "type_id":"1"
                    },
                ]
            },
        ]
        listArticle=getArticles(theme_articles)
        self.render(
            "list.html",
        )

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
            "index.html",
            page_title = "About Love",
            urls={
                "list_url":"http://115.159.116.153:8000/list",
                "article_url":"http://115.159.116.153:8000/article"
            },
            themes=[
                    {
                        "title":"精品文章",
                        "theme_id":"0"
                    },
                    {
                        "title":"精品文章2",
                        "theme_id":"1"
                    },
            ],
            listArticles=[
                    {
                        "title":"一个“好人”如何去挽回失去的爱情",
                        "image":"/static/images/website4.jpg",
                        "brief":"第一，不要纠结于过去，承认你们的关系已经破裂。盗哥讲过，不要把过去的承诺拿到现在来用，一切的承诺仅仅限于女孩对你当时的感觉和情绪。感觉和情绪一去不复返， 现在有的只有厌烦，之前的所有兴趣都成为过去。承认关系已经破裂，你现在需要做的不是纠缠，而是想如何正确的去修复……",
                        "type_id":"0"
                    },
                    {
                        "title":"一个“好人”如何去挽回失去的爱情2",
                        "image":"/static/images/website5.jpg",
                        "brief":" 第二，不要纠结于过去，承认你们的关系已经破裂。盗哥讲过，不要把过去的承诺拿到现在来用，一切的承诺仅仅限于女孩对你当时的感觉和情绪。感觉和情绪一去不复返， 现在有的只有厌烦，之前的所有兴趣都成为过去。承认关系已经破裂，你现在需要做的不是纠缠，而是想如何正确的去修复……",
                        "type_id":"1"
                    },
            ],
            pptArticles=[
                    {
                        "title":"Programming Collective Intelligence",
                        "image":"/static/images/website1.jpg",
                        "theme":"主题1"
                    },
                    {
                         "title":"Programming Collective Intelligence2",
                         "image":"/static/images/website2.jpg",
                         "theme":"主题2"
                    },
                    {
                         "title":"Programming Collective Intelligence3",
                         "image":"/static/images/website3.jpg",
                         "theme":"主题3"
                    },
            ]
        )

class BookModule(tornado.web.UIModule):
    def render(self, book):
        return self.render_string('modules/book.html', book=book)

class PptArticleModule(tornado.web.UIModule):
    def render(self, pptArticle):
        return self.render_string('modules/pptArticle.html', pptArticle=pptArticle)

class RecommendedHandler(tornado.web.RequestHandler):
    def get(self):
        try:
            conn=MySQLdb.connect(host='localhost',user='root',passwd='qinxiangyu',db='spider',port=3306)
            cur=conn.cursor()
            count=cur.execute('select title, COUNT(url), url, createtime from puahome_bbs WHERE createtime>date_add(NOW(),interval -3 day)  GROUP BY url ORDER BY createtime DESC')
            results=cur.fetchall()
            test_len=len(results)
            test_type=type(results)
            cur.close()
            conn.close()
        except MySQLdb.Error,e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        for result in results:
            result_len=len(result)
            result_type=type(result)		
        self.render(
        "recommended.html",
        page_title="Burt's Books | Recommended Reading",
        header_text="Recommended Reading",
        test_len=test_len,
        test_type=test_type,
		result_type=result_type,
        result_len=result_len,
        books=[
        {
            "title":"Programming Collective Intelligence",
            "subtitle": "Building Smart Web 2.0 Applications",
            "image":"/static/images/collective_intelligence.gif",
            "author": "Toby Segaran",
            "date_added":1310248056,
            "date_released": "August 2007",
            "isbn":"978-0-596-52932-1",
            "description":"<p>This fascinating book demonstrates how" \
            "you " \
            "can build web applications to mine the enormous amount" \
            "of data created by people " \
            "you've found it.</p>"
        }
        ]
        )


if __name__ == '__main__':
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
