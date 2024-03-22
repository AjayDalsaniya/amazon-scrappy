import scrapy

class AmazonItem(scrapy.Item):
    category = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    review = scrapy.Field()
    next_page = scrapy.Field()