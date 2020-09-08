from scrapy import Spider
from scrapy import Request
from adecco.items import AdeccoItem
from datetime import datetime
import re
import math

class AdeccoSpider(Spider):
    name = 'adecco_spider'
    allowed_domains = ['www.adeccousa.com']
    start_urls = ['https://www.adeccousa.com/jobs/job-search/']
    
    def parse(self, response): # Assemble a list of the briefing urls, titles, and dates
        
        # Pull the text that says how many jobs there are (e.g. "Want to find a job? We have 5583 of them")
        lst_txt = response.xpath('//h1[@id="txtjobCount"]//text()').extract()
        lst_clean_txt = [s.strip() for s in lst_txt if len(s.strip())>0]

        # Extract number of jobs from lst of strings
        n_jobs = int(''.join([i for i in lst_clean_txt[0] if i.isnumeric()]))

        # Calculate number of pages (Jobs / 10 per page)
        n_pages = math.ceil(n_jobs/10)

        # Generate list of page urls
        lst_result_urls = [f'https://www.adeccousa.com/jobs/job-search/?pageNum={i+1}' for i in range(n_pages)]
        
        # Yield the requests to different search result urls, 
        # using parse_result_page function to parse the response.
        for url in lst_result_urls:
            yield Request(url=url, callback=self.parse_result_page)

    def parse_result_page(self, response):
    
        # We are looking for url of the detail page.
        lst_detail_urls = response.xpath('//a[@class="btn btn-sm btn-success pull-right"]//@href').extract()
        
        # Yield the requests to the details pages, 
        # using parse_detail_page function to parse the response.
        for url in lst_detail_urls:
            yield Request(url=url, callback=self.parse_detail_page)


    def parse_detail_page(self, response):
        
        # Job name
        try:
            job_name = response.xpath('//header[@class="panel-header"]/h1/text()').extract()[0].strip()
        except:
            job_name = 'parse_error'
        
        # Location
        try:
            location = response.xpath('//span[@id="lblCity"]//text()').extract()
        except:
            location = 'parse_error'

        # Job type
        try:
            job_type = response.xpath('//span[@class="job-details-value" and @id="ltContractType"]/a/text()').extract()[0]
        except:
            job_type = 'parse_error'
        
        # Salary
        try:
            salary = response.xpath('//span[@id="ltSalaryWage"]/text()').extract()[0]
        except:
            salary = 'parse_error'

        # Category
        try:
            category = response.xpath('//span[@class="job-details-value" and @id="ltCategory"]/a/text()').extract()[0]
        except:
            category = 'parse_error'

        # Reference number
        try:
            ref_number = response.xpath('//p[@class="reference-number"]/span/text()').extract()[0].strip()
        except:
            ref_number = 'parse_error'

        # First paragraph
        try:
            lst_txt = response.xpath('//div[@class="job--task-specifics"]//text()').extract()
            lst_clean_txt = [s.strip() for s in lst_txt if len(s.strip())>0]
            first_paragraph = lst_clean_txt[0]
        except:
            first_paragraph = 'parse_error'
        
        # Description
        try:
            description = '\n\n'.join(lst_clean_txt)
        except:
            description = 'parse_error'

        # Date of scrape
        dateTimeObj = datetime.now()

        item = AdeccoItem()
        item['job_name'] = job_name
        item['location'] = location
        item['job_type'] = job_type
        item['salary'] = salary
        item['category'] = category
        item['ref_number'] = ref_number
        item['first_paragraph'] = first_paragraph
        item['description'] = description
        item['scrape_datetime'] = dateTimeObj

        yield item
       