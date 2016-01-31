# -*- coding:utf-8 -*-
import tornado.web
import config
from MongoService import MongoService

class MainHandler(tornado.web.RequestHandler):
    def mergeArticleAndThemes(self, themes_array, pptArticles_array):
        array=[]
        for pptArticle in pptArticles_array:
            for theme in themes_array:
                if(theme["theme_id"]==pptArticle["type_id"]):
                    pptArticle["theme"]=theme["title"]
                    break
        return pptArticles_array

    def getArticlesSum(self, type):
        mongoService=MongoService()
        sum = mongoService.getListArticlesSum(type)
        return sum

    def getArticles(self, themes_array, limits):
        mongoService=MongoService()
        array=[]
        for theme in themes_array:
            listArticles=mongoService.getMainArticles(theme["theme_id"], limits)
            array.extend(listArticles)
        return array

    def getThemes(self, themes):
        mongoService=MongoService()
        return mongoService.getThemes(themes)

    def get(self):
        themes_array=self.getThemes(config.mainThemes)
        pptThemes_array=self.getThemes(config.pptThemes)
        listArticles_array=self.getArticles(themes_array, config.MainArticlesNumber)
        pptArticles_array=self.getArticles(pptThemes_array, config.PptArticlesNumber)
        pptArticles_array=self.mergeArticleAndThemes(pptThemes_array, pptArticles_array)
        self.render(
            "index.html",
            page_title = config.WebTitle,
            urls=config.urls,
            themes=themes_array,
            listArticles=listArticles_array,
            pptArticles=pptArticles_array
        )
        '''
        self.write(str(pptArticles_array))
        '''
