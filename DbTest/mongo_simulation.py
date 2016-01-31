import pymongo
import config
import random
import datetime
import sys
from pymongo import MongoClient

class TestMongo(object):
    def __init__(self):
        conn = MongoClient("localhost", 27017)
        self.db = conn["webSite"]

    def getDataId(self, cursor):
        cursor_doc = cursor.find().sort([("id", pymongo.DESCENDING)]).limit(1)
        array=[]
        for doc in cursor_doc:
            del doc["_id"]
            array.append(doc)
        if (len(array)>0):
            id = array[0]["id"]
            return id
        else:
            return 0

    def insertArticle(self):
        url_image="/static/images/"
        cursor = self.db.articles
        type_id = self.getRandomList(config.type_id)
        lastest_id = self.getDataId(cursor)
        id = lastest_id+1
        title = self.getRandomList(config.title)
        image = self.getRandomList(config.image)
        date = self.getRandomDate()
        brief = self.getRandomList(config.brief)
        writer = self.getRandomList(config.writer)
        content = self.getRandomList(config.content)
        rankingScore = self.getRandomFloat(0, 1)
        article = {"id":id, "title":title, "image":url_image+image, "date":date, "brief":brief, "type_id":type_id, "writer":writer, "content":content,"rankingScore":rankingScore}
        cursor.insert(article)
        return 	article["id"]

    def getRandomFloat(self, start, end):
        return random.uniform(start,end)

    def getRandomDate(self):
        return datetime.datetime.now()

    def getRandomList(self, list):
        return random.choice(list)
        
def process(size):
    test = TestMongo()
    count=0
    while(count<size):
        test.insertArticle()
        count=count+1
    print size

if __name__=="__main__":
    if(len(sys.argv))>1:
        process(int(sys.argv[1]))
    else:
        print "default:10"
        process(10)
    print "done"