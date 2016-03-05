# -*- coding:utf-8 -*-

import pymongo
from pymongo import MongoClient

class MongoService(object):
    def __init__(self):
        conn = MongoClient("localhost", 27017)
        self.db = conn["webSite"]

    def getThemes(self, ids):
        cursor = self.db.themes
        cursor_doc = cursor.find({"theme_id":{'$in':ids}})
        array=[]
        for doc in cursor_doc:
            del doc["_id"]
            array.append(doc)
        return array

    def getThemeTitle(self, id):
        cursor = self.db.themes
        doc = cursor.find_one({"theme_id":id})
        if doc:
            return doc["title"]
        else:
            return ""

    def getMainArticles(self, type, limit, mark):
        cursor = self.getCursor(mark)
        cursor_doc = cursor.find({"type_id":type}).sort([("rankingScore", pymongo.DESCENDING),("date",pymongo.DESCENDING)]).limit(limit)
        array=[]
        for doc in cursor_doc:
            del doc["_id"]
            array.append(doc)
        return array

    def getListArticles(self, type, skip, limit, mark):
        cursor = self.getCursor(mark)
        cursor_doc = cursor.find({"type_id":type}).sort([("rankingScore", pymongo.DESCENDING),("date",pymongo.DESCENDING)]).skip(skip).limit(limit)
        array=[]
        for doc in cursor_doc:
            del doc["_id"]
            array.append(doc)
        return array

    def getListArticlesSum(self, type, mark):
        cursor = self.getCursor(mark)
        doc = cursor.find({"type_id":type}).count()
        return doc

    def getArticles(self, id, mark):
        cursor = self.getCursor(mark)
        cursor_doc = cursor.find_one({"id":int(id)})
        if cursor_doc:
            del cursor_doc["_id"]
            return cursor_doc
        else:
            cursor_doc={}
            return cursor_doc
    
    def getCursor(self, mark):
        if mark=="A":
            cursor = self.db.articlesA
        else:
            cursor = self.db.articlesB
        return cursor