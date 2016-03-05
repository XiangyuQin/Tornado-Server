# -*- coding:utf-8 -*-
import sys
from RedisService import RedisService

def str2Int(strElement):
    try:
        intElement=int(strElement)
    except:
        intElement=0
    return intElement
    
def getMark():
    service = RedisService()
    redisMark = service.getArticlesMark()
    if redisMark==None or redisMark=="":
        redisMark = "A"
    return redisMark