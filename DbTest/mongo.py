import pymongo
from pymongo import MongoClient

class TestMongo(object):
    def __init__(self):
        conn = MongoClient("localhost", 27017)
        self.db = conn["webSite"]

    def testFind(self):
        coll = self.db.words
        arrayWord=[]
        word_doc = coll.find()
        for doc in word_doc:
            arrayWord.append(doc)
        print len(arrayWord)

    def getThemes(self):
        cursor = self.db.themes
        abc=["1","2"]
        cursor_doc = cursor.find({"theme_id":{'$in':abc}})
        array=[]
        for doc in cursor_doc:
            del doc["_id"]
            array.append(doc)
        return array

    def getListArticles(self, type, skip, limit):
        cursor = self.db.articles
        cursor_doc = cursor.find({"type_id":type}).sort([("rankingScore", pymongo.DESCENDING),("date",pymongo.DESCENDING)]).limit(limit)
        array=[]
        count=0
        for doc in cursor_doc:
            count=count+1
            print "hah"
            del doc["_id"]
            array.append(doc)
        return count

if __name__=="__main__":
    test = TestMongo()
    '''
    abc = test.getListArticles("0", 0 , 3)
    '''
    abc = test.getThemes()
    print len(abc)