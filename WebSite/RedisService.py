# -*- coding: UTF-8 -*-
import redis
import common
import datetime

class RedisService(object):
    def __init__(self):
        self.r = redis.Redis(host='localhost', port=6379, db=0)
            
    def getArticlesMark(self):
        try:
            mark = self.r.get("rankMark")
            return mark
        except Exception as e:
            return ""
            

if __name__ == '__main__':
    service = RedisService()
    