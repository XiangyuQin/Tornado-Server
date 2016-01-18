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

    def getMainArticles(self, type, limit):
        cursor = self.db.articles
        cursor_doc = cursor.find({"type_id":type}).sort([("rankingScore", pymongo.DESCENDING),("date",pymongo.DESCENDING)]).limit(limit)
        array=[]
        for doc in cursor_doc:
            del doc["_id"]
            array.append(doc)
        return array

    def getListArticles(self, type, skip, limit):
        cursor = self.db.articles
        cursor_doc = cursor.find({"type_id":type}).sort([("rankingScore", pymongo.DESCENDING),("date",pymongo.DESCENDING)]).skip(skip).limit(limit)
        array=[]
        for doc in cursor_doc:
            del doc["_id"]
            array.append(doc)
        return array

    def getArticles(self, id):
        cursor = self.db.articles
        cursor_doc = cursor.find_one({"id":id})
        if cursor_doc:
            del cursor_doc["_id"]
            return cursor_doc
        else:
            cursor_doc={}
            return cursor_doc