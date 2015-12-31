# -*- coding:utf-8 -*-
import tornado.web
import config

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
            "index.html",
            page_title = "About Love",
            urls=config.urls,
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
                        "type_id":"0",
                        "id":"102"
                    },
                    {
                        "title":"一个“好人”如何去挽回失去的爱情2",
                        "image":"/static/images/website5.jpg",
                        "brief":" 第二，不要纠结于过去，承认你们的关系已经破裂。盗哥讲过，不要把过去的承诺拿到现在来用，一切的承诺仅仅限于女孩对你当时的感觉和情绪。感觉和情绪一去不复返， 现在有的只有厌烦，之前的所有兴趣都成为过去。承认关系已经破裂，你现在需要做的不是纠缠，而是想如何正确的去修复……",
                        "type_id":"1",
                        "id":"103"
                    },
            ],
            pptArticles=[
                    {
                        "title":"Programming Collective Intelligence",
                        "image":"/static/images/website1.jpg",
                        "theme":"主题1",
                        "id":"103"
                    },
                    {
                         "title":"Programming Collective Intelligence2",
                         "image":"/static/images/website2.jpg",
                         "theme":"主题2",
                         "id":"102"
                    },
                    {
                         "title":"Programming Collective Intelligence3",
                         "image":"/static/images/website3.jpg",
                         "theme":"主题3",
                         "id":"101"
                    },
            ]
        )