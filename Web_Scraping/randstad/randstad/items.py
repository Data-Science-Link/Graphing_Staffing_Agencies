# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RandstadItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    job_name = scrapy.Field()
    location = scrapy.Field()
    job_type = scrapy.Field()
    salary = scrapy.Field()
    category = scrapy.Field()
    experience = scrapy.Field()
    ref_number = scrapy.Field()
    first_paragraph = scrapy.Field()
    description = scrapy.Field()
    posting_date = scrapy.Field()
    scrape_datetime = scrapy.Field()
