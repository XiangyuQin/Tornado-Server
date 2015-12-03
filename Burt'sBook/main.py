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
        try:
            conn=MySQLdb.connect(host='localhost',user='root',passwd='qinxiangyu',db='spider',port=3306)
            cur=conn.cursor()
            count=cur.execute('select * from puahome_bbs limit 1')
            results=cur.fetchall()
            print type(results)
            cur.close()
            conn.close()
        except MySQLdb.Error,e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1]
        handlers=[
            (r"/", MainHandler),
            (r"/recommended", RecommendedHandler),
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__),"templates"),
            static_path=os.path.join(os.path.dirname(__file__),"static"),
            debug=True,
            ui_modules={'Book': BookModule},
        )
        tornado.web.Application.__init__(self, handlers, **settings)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
            "main.html",
            page_title = "Burt's Books | Home",
            header_text = "Welcome to Burt's Books!",
        )

class BookModule(tornado.web.UIModule):
    def render(self, book):
        return self.render_string('modules/book.html', book=book)

class RecommendedHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
        "recommended.html",
        page_title="Burt's Books | Recommended Reading",
        header_text="Recommended Reading",
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
