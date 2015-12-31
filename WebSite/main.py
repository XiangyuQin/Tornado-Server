# -*- coding:utf-8 -*-
import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
import os.path
import MySQLdb
import config

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
    def getArticles(self, themeArticles, articlesType):
        listArticles=[]
        for theme in themeArticles:
            if (theme['type']==articlesType):
                listArticles = theme['articles']
        return listArticles

    def getShowArticlesNum(self, currentNum, sum):
        endNum = currentNum + config.pageSize
        if (endNum>=sum):
            endNum=sum
        return endNum

    def getThemeName(self,themeId):
        themeName = config.themesType[themeId]
        if (themeName==None):
            themeName=""
        return themeName

    def str2Int(self, strElement):
        try:
            intElement=int(strElement)
        except:
            intElement=0
        return intElement

    def getImf(self, inputImf):
        inputDict={}
        inputArray = inputImf.split('_')
        if len(inputArray) > 1:
            inputDict['articlesType'] = inputArray[0]
            inputDict['startPage'] = inputArray[1]
        else:
            inputDict['articlesType'] = inputArray[0]
            inputDict['startPage'] = "1"
        return inputDict

    def getEndPage(self, page, sum):
        head=1
        max = (sum+config.pageSize-1)/config.pageSize
        start=head
        end=max
        if(max>config.pageSize):
            left=config.pageSize/2
            right=config.pageSize-left-1
            if(page<left+1):
                start=head
            elif(page>max-right):
                start=max-config.pageSize+1
            else:
                start=page-left
            end=start+config.pageSize-1
        pages=[start, end, max, page]
        return pages

    def addArticles_test(self, array, times):
        array_test=[]
        for i in range(0, times):
            for element in array:
                array_test.append(element)
        return array_test

    def getThemeArticles_test(self):
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
        return theme_articles

    def get(self, input):
        inputImf = input[::1]
        inputDict = self.getImf(inputImf)
        articlesType = inputDict['articlesType']
        startPage = inputDict['startPage']
        startPageInt = self.str2Int(startPage)
        themeArticles = self.getThemeArticles_test()
        listArticles = self.getArticles(themeArticles, int(articlesType))
        listArticles = self.addArticles_test(listArticles,config.times)
        startNum = (startPageInt-1)*config.pageSize
        endNum = self.getShowArticlesNum(startNum, len(listArticles))
        themeName = self.getThemeName(articlesType)
        pages = self.getEndPage(startPageInt, len(listArticles))
        self.render(
            "list.html",
            listArticles=listArticles,
            start=startNum,
            end=endNum,
            themeName=themeName,
            pages=pages,
            sum=len(listArticles),
            urls=config.urls,
            articlesType=articlesType,
        )
        #self.write(str(startPage)+" str(inputImf):"+str(inputImf)+" str(articlesType):"+str(articlesType)+" str(startPage):"+str(startPage)+' Num:'+str(startNum)+' '+str(endNum)+' pages:'+str(pages[0])+' '+str(pages[1])+' '+str(pages[2])+' pages len:'+str(len(pages))+' '+themeName+' '+str(len(listArticles))+' ')

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
