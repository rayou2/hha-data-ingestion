import pandas as pd ## import pandas for general file types 
import json ## imoprt json for json files
import bs4 ## import bs4 for html files
import requests ## import requests for web requests
import sqlalchemy ## import sqlalchemy for sql queries
from PIL import Image  ## import pillow for image files
import pydub ## import pydub for audio files
from pydub.playback import play
import playsound ## import playsound for audio files
import geopandas as gpd ## import geopandas for geospatial files
from google.cloud import bigquery ## import bigquery for bigquery files
import matplotlib
import xlrd ## import xlrd for excel files, tab names 
import PyPDF2 ## import PyPDF2 for pdf files

## Section 1 
## open excel file
tab1 = pd.read_excel("data/data1.xls",sheet_name='Sheet1') ## read excel file
tab2 = pd.read_excel('data/data1.xls',sheet_name='Sheet2') ## read excel file
print (tab1,'\n',tab2) ## prints the data


## Section 2
## using request module for json api
data = requests.get('https://data.cms.gov/data-api/v1/dataset/3817f5a4-bb28-416e-93b5-9cd794a76024/data')
## gets data from the API endpoint
data = data.json() ## turns data into json
print (data) ## prints the data

## Section 3
# pip install --upgrade google-cloud-bigquery

client = bigquery.Client.from_service_account_json('data/ramon-507-2509a55a26d6.json') ## connects to GCP
query_job = client.query("SELECT * FROM `bigquery-public-data.breathe.arxiv` LIMIT 100") 
## we used client query which wraps a sql query that selects all the column on breathe data and limited to the first 100 rows.
results = query_job.result() ## results is a function that displays the results of the above query
bigquery1 = pd.DataFrame(results.to_dataframe()) ## put results into dataframe
print(bigquery1)

query_job2 = client.query("SELECT * FROM `bigquery-public-data.austin_crime.crime` LIMIT 100")
## we used client query which wraps a sql query that selects all the column on crime data and limited to the first 100 rows.
results2 = query_job2.result()
bigquery2 = pd.DataFrame(results2.to_dataframe())
print(bigquery2)