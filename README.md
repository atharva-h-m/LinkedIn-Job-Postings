
#DA 204o Data Science in Practice Project

## Project Title
LinkedIn Job Postings - Salary Prediction and Job Recommendation

## Team Members
- Atharva Hemant Malandkar
- Barath Karthi R K
- Harikrishnan C
- Shunmuga Janani A

## Problem Statement
This project will analyze LinkedIn job postings to identify key factors influencing demand, compensation, and work arrangements across various industries. Our goal is to provide employers and job seekers with actionable insights by developing a salary prediction model that leverages job-specific attributes such as title, location, and required skills. The analysis will reveal trends in sought-after benefits, high-paying positions, and valuable skill sets, empowering users to make data-driven decisions for hiring and career advancement.

## Dataset Summary
This dataset contains a nearly comprehensive record of 124,000+ job postings listed in 2023 and 2024. Each individual posting contains dozens of valuable attributes for both postings and companies, including the title, job description, salary, location, application URL, and work-types (remote, contract, etc), in addition to separate files containing the benefits, skills, and industries associated with each posting. The majority of jobs are also linked to a company, which are all listed in another csv file containing attributes such as the company description, headquarters location, and number of employees, and follower count.

Data Set: https://www.kaggle.com/datasets/arshkon/linkedin-job-postings

## Dataset Files and Columns

job_postings.csv

job_id: The job ID as defined by LinkedIn (https://www.linkedin.com/jobs/view/ job_id )
company_id: Identifier for the company associated with the job posting (maps to companies.csv)
title: Job title.
description: Job description.
max_salary: Maximum salary
med_salary: Median salary
min_salary: Minimum salary
pay_period: Pay period for salary (Hourly, Monthly, Yearly)
formatted_work_type: Type of work (Fulltime, Parttime, Contract)
location: Job location
applies: Number of applications that have been submitted
original_listed_time: Original time the job was listed
remote_allowed: Whether job permits remote work
views: Number of times the job posting has been viewed
job_posting_url: URL to the job posting on a platform
application_url: URL where applications can be submitted
application_type: Type of application process (offsite, complex/simple onsite)
expiry: Expiration date or time for the job listing
closed_time: Time to close job listing
formatted_experience_level: Job experience level (entry, associate, executive, etc)
skills_desc: Description detailing required skills for job
listed_time: Time when the job was listed
posting_domain: Domain of the website with application
sponsored: Whether the job listing is sponsored or promoted.
work_type: Type of work associated with the job
currency: Currency in which the salary is provided.
compensation_type: Type of compensation for the job.

job_details/benefits.csv

job_id: The job ID
type: Type of benefit provided (401K, Medical Insurance, etc)
inferred: Whether the benefit was explicitly tagged or inferred through text by LinkedIn

company_details/companies.csv

company_id: The company ID as defined by LinkedIn
name: Company name
description: Company description
company_size: Company grouping based on number of employees (0 Smallest - 7 Largest)
country: Country of company headquarters.
state: State of company headquarters.
city: City of company headquarters.
zip_code: ZIP code of company's headquarters.
address: Address of company's headquarters
url: Link to company's LinkedIn page

company_details/employee_counts.csv

company_id: The company ID
employee_count: Number of employees at company
follower_count: Number of company followers on LinkedIn
time_recorded: Unix time of data collection

## Notebooks
The complete project is divided into different data science workflow steps as mentioned below.
The input , output , and description is provided for all the notebooks.
Please make sure the notebooks are run sequentially .

| **Notebook**                  | **Discription**     |
| ------------------- | ------------------ |
| [01_data_collection_and_cleaning](https://github.com/atharva-h-m/LinkedIn-Job-Postings/blob/main/notebooks/01-data_collection_and_cleaning.ipynb)   | Load the raw dataset and check overview , missing values etc..  |
| [02_data_wrangling](https://github.com/atharva-h-m/LinkedIn-Job-Postings/blob/main/notebooks/02-data_wrangling.ipynb)   | Perform descriptive statistics analysis , outlier handling and feature engineering.After this the cleaned dataset is stored.   |
| [03_eda](https://github.com/atharva-h-m/LinkedIn-Job-Postings/blob/main/notebooks/03-EDA.ipynb)   | Explore the dataset using various visualizations  |
| [04_model_development](https://github.com/atharva-h-m/LinkedIn-Job-Postings/blob/main/notebooks/04-model_development.ipynb)  | Compare various Model performances  |

## Models implemented:​
Regression models (e.g., Linear Regression, Ridge, Lasso, ElasticNet).​
Tree-based models (e.g., Random Forest, Decision Tree).​
Boosting model – XGBoost​
Neighbors model - KNN​
Deep learning methods (e.g., neural networks).

## Future Enhancement
Real-Time Data Integration:​
- Integrating real-time job postings from LinkedIn or other job boards (e.g., Indeed, Glassdoor) into the model would make the predictions more accurate and up-to-date.​

Transfer Learning:​
- Transfer learning from pre-trained models (e.g., BERT,GPTs for natural language processing) could be used to improve the handling of job descriptions, resulting in better predictions.
