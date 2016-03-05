# -*- coding:utf-8 -*-
import tornado.web
import config
import common
from MongoService import MongoService

class ListHandler(tornado.web.RequestHandler):
    def getArticles(self, type, startPage, limit):
        mongoService=MongoService()
        listArticles=[]
        start = (startPage-1)*config.pageSize
        mark = common.getMark()
        listArticles=mongoService.getListArticles(type, start, limit, mark)
        return listArticles

    def getThemeTitle(self,themeId):
        mongoService=MongoService()
        title = mongoService.getThemeTitle(themeId)
        return title

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

    def getListArticlesSum(self, type):
        mark = common.getMark()
        mongoService=MongoService()
        sum = mongoService.getListArticlesSum(type, mark)
        return sum

    def addArticles_test(self, array, times):
        array_test=[]
        for i in range(0, times):
            for element in array:
                array_test.append(element)
        return array_test

    def get(self, input):
        inputImf = input[::1]
        inputDict = self.getImf(inputImf)
        articlesType = inputDict['articlesType']
        startPage = inputDict['startPage']
        startPageInt = common.str2Int(startPage)
        listArticles = self.getArticles(articlesType, startPageInt, config.pageSize)
        themeTitle = self.getThemeTitle(articlesType)
        sum = self.getListArticlesSum(articlesType)
        #listArticles = self.addArticles_test(listArticles, config.times)
        pages = self.getEndPage(startPageInt, sum)
        self.render(
            "list.html",
            listArticles=listArticles,
            themeTitle=themeTitle,
            pages=pages,
            urls=config.urls,
            articlesType=articlesType,
        )
        '''
        self.write(str(sum)+articlesType)
        '''
