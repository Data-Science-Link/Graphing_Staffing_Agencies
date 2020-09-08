from scrapy import Spider
from scrapy import Request
from randstad.items import RandstadItem
from datetime import datetime
import re
import math

class RandstadSpider(Spider):
    name = 'randstad_spider'
    allowed_domains = ['www.randstadusa.com']
    start_urls = ['https://www.randstadusa.com/jobs/']
    
    def parse(self, response): # Assemble a list of the briefing urls, titles, and dates

        # Extract number of jobs
        n_jobs = int(response.xpath('//span[@id="ctl07_ctl03_NrOfJobsLabel"]/text()').extract()[0].split()[-1])

        # Calculate number of pages (Jobs / 10 per page)
        n_pages = math.ceil(n_jobs/10)

        # Generate list of page urls
        lst_result_urls = [f'https://www.randstadusa.com/jobs/search/page-{i+1}/' for i in range(n_pages)]
        
        # Yield the requests to different search result urls, 
        # using parse_result_page function to parse the response.
        for url in lst_result_urls:
            yield Request(url=url, callback=self.parse_result_page)

    def parse_result_page(self, response):
        
        # We are looking for url of the detail page.
        lst_detail_urls = response.xpath('//div[@id="search-result-body"]//a/@href').extract()
        lst_detail_urls = ['https://www.randstadusa.com' + url for url in lst_detail_urls]
        
        # Yield the requests to the details pages, 
        # using parse_detail_page function to parse the response.
        for url in lst_detail_urls:
            yield Request(url=url, callback=self.parse_detail_page)


    def parse_detail_page(self, response):
        
        # Job name
        try:
            job_name = response.xpath('//p[@class="desc-job-title"]/text()').extract()[0]
        except:
            job_name = 'parse_error'
        
        # Location
        try:
            location = response.xpath('//span[@id="ctl07_ctl03_LocationLabel"]/text()').extract()[0]
        except:
            location = 'parse_error'

        # Experience
        try:
            experience = response.xpath('//span[@id="ctl07_ctl03_ExperienceLabel"]/text()').extract()[0]
        except:
            experience = 'parse_error'

        # Job type
        try:
            job_type = response.xpath('//span[@id="ctl07_ctl03_JobTypeIDLabel"]/text()').extract()[0]
        except:
            job_type = 'parse_error'
        
        # Salary
        try:
            salary = response.xpath('//span[@id="ctl07_ctl03_SalaryLabel"]/text()').extract()[0]
        except:
            salary = 'parse_error'

        # Category
        try:
            category = response.xpath('//span[@id="ctl07_ctl03_IndustryLabel"]/text()').extract()[0]
        except:
            category = 'parse_error'

        # Reference number
        try:
            ref_number = response.xpath('//span[@id="ctl07_ctl03_ReferenceLabel"]/text()').extract()[0]
        except:
            ref_number = 'parse_error'

        # Posting date
        try:
            posting_date = response.xpath('//span[@id="ctl07_ctl03_DatePostedLabel"]/text()').extract()[0]
        except:
            posting_date = 'parse_error'

        # First paragraph
        try:
            lst_txt = response.xpath('//div[@class="jobdescription-item"]//text()').extract()
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

        item = RandstadItem()
        item['job_name'] = job_name
        item['location'] = location
        item['job_type'] = job_type
        item['experience'] = experience
        item['salary'] = salary
        item['category'] = category
        item['ref_number'] = ref_number
        item['first_paragraph'] = first_paragraph
        item['description'] = description
        item['posting_date'] = posting_date
        item['scrape_datetime'] = dateTimeObj

        yield item
       