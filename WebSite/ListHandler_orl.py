# -*- coding:utf-8 -*-
import tornado.web
import config
import common

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
                        "type_id":"0",
                        "id":"100"
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
                        "type_id":"1",
                        "id":"101"
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
        startPageInt = common.str2Int(startPage)
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
