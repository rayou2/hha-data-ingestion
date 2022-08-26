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


tab1 = pd.read_excel('python/data1.xls',sheet_name='Sheet1') ## read excel file
tab2 = pd.read_excel('python/data1.xls',sheet_name='Sheet2') ## read excel file
print (tab1,'\n',tab2) ## prints the data

data = requests.get('https://data.cms.gov/data-api/v1/dataset/3817f5a4-bb28-416e-93b5-9cd794a76024/data')
## gets data from the API endpoint
data = data.json() ## turns data into json
print (data) ## prints the data