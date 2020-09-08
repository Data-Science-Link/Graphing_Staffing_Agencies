# Graphing_Staffing_Agencies

## Table of Contents
- [Introduction](#introduction)
- [Dataset](#dataset)
- [Analysis](#analysis)
	- [Geography](#geography)
	- [Job Type](#job-type)
	- [Salary](#salary)
- [Conclusion](#conclusion)

## Introduction
The purpose of this analysis is to perform market research on major staffing agencies. Some questions that are in the forefront of any staffing agency are:
- What types of jobs should we try to fill?
- In which geographic locations should we focus our search?
- Should we focus on a high volume of blue collar jobs or a small amount of white collar jobs?
- How long does it take to fill a position (Time to Fill)?
- How much does it cost to fill a position (Cost per Hire)?

During this analysis we will be taking the perspective of an up and coming staffing agency. We'll name the organization *Getting Bob a Job (GBAJ)*. GBAJ wants to strategically enter into the market. We will use the job boards from two of the largest staffing agencies to decide which types of jobs to fill and where to fill them. 

The latter two bullet points above (Time to Fill & Cost per Hire) are out of the scope of this analysis. Cost per hire cannot be calculated with the dataset described below. However, if GBAJ were to scrape the job boards of competitors on a daily basis it would be feasible to estimate the average time to fill of their competitors.


## Dataset
GBAJ is interested in strategically entering into the staffing agency market. What beter way to do this than to scrape the job boards of the two [top rated](https://www.thesmbguide.com/staffing-agencies) staffing agencies? A total of 17,000 job postings were web scraped from the following job boards:

Randstad - [Job Board](https://www.randstadusa.com/jobs/)

Adecco - [Job Board](https://www.adeccousa.com/jobs/job-search/)

The most salient variables in the dataset are:
- Job Name - Title of job
- Caregory - Which industry
- Job Type - Is it full time, temporary, etc.
- Salary - Hourly or Annual
- Location - City/State

  ![image](/docs/images/Data_Sample.png)

  *Sample of dataset*

## Analysis
For our analysis we will create visualizations in three categories:
- Geography
- Job Type
- Salary

By examining geography we can determine where major staffing agencies are conentrating their effors. And by examining job type and salary we can determine the competitor's primary candidate profile.

### Geography

  ![image](/docs/images/Adecco_Fleet_Percentage.png)

  *Adecco's Percent Jobs by State (i.e. where are most of the jobs?)*

  ![image](/docs/images/Randstad_Fleet_Percentage.png)

  *Randstad's Percent Jobs by State (i.e. where are most of the jobs?)*

  ![image](/docs/images/state_bar_top_10_Adecco.png)

  *Adecco's Top 10 States by Percentage of Job Posts*

  ![image](/docs/images/state_bar_top_10_Randstad.png)

  *Randstad's Top 10 States by Percentage of Job Posts*

  ![image](/docs/images/state_bar_bottom_10_Adecco.png)

  *Adecco's Bottom 10 States by Percentage of Job Posts*

  ![image](/docs/images/state_bar_bottom_10_Randstad.png)

  *Randstad's Bottom 10 States by Percentage of Job Posts*

### Job Type
  
  ![image](/docs/images/Adecco_Word_Cloud_category.png)

  *Adecco: Word Cloud of Job Categories*

  ![image](/docs/images/Randstad_Word_Cloud_category.png)

  *Randstad: Word Cloud of Job Categories*

  ![image](/docs/images/Adecco_Word_Cloud_job_name.png)

  *Adecco: Word Cloud of Job Names*

 ![image](/docs/images/Randstad_Word_Cloud_job_name.png)

  *Randstad: Word Cloud of Job Names*
### Salary

  ![image](/docs/images/salary.png)

  *Hourly Wage Distribution by Company*

## Conclusion
We began this corporate journey asking ourselves, what regions of the country are undertapped and which types of jobs are traditionally posted on staffing agency websites. 

With respect to geography, we see that California & Texas are both hotspots for jobs. Randstad has a hold on jobs in the southeast and Tennessee, while Adecco has significant market share around the great lakes. Assuming there are healthy economies in the under-targeted great plains, southwest, and northwest states, GBAJ has a good opportunity to enter into these markets.

With respect to the job postings and candidates, we see that low wage workers are targeted (see hourly wage histogram). As represented in the word clouds above, many of these job names and job categories are not in tech or engineering. The job postings are targeted at blue collar employees. Perhaps due to the high volume of work contracts. There is a large opportunity for GBAJ to target white collar employees if they can do so at scale.

Through web scraping, data cleaning, and simple exploratory data analysis we have come to some meaningful insights on the state of staffing in the U.S.  
