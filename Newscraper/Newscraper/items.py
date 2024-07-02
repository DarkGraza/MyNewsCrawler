from scrapy.item import Item, Field

class ArticleItem(Item):
    Article_Url = Field()
    Title = Field()
    Author = Field()
    Author_Url = Field()
    Content = Field()
    Published_Date = Field()

class Urls(Item):
    Initial_Urls =Field()
