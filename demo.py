
import os
import redis
import zipfile
import requests
from datetime import datetime ,timedelta
import csv
import click
import cherrypy
import time

previous_day = datetime.now() - timedelta(1)
prev_date=previous_day.date().strftime("%d%m%y")
zipfile_date=prev_date+"_CSV.ZIP"
zipfile_name='EQ'+zipfile_date
csvfile_name='EQ'+prev_date+".CSV"

link="https://www.bseindia.com/download/BhavCopy/Equity/EQ"
download_url=link+zipfile_date
#file_path="C:\\Users\\rohitd\\Downloads\\"+zipfile_name
file_to_save=open(zipfile_name,"wb")
print(f'{download_url}')
#print(f'{file_path}')
			
					
with requests.get(download_url, verify=False, stream=True) as response:
													for chunk in response.iter_content(chunk_size=1024):
																	file_to_save.write(chunk)
																	print("Completed downloading file")
												 

file_to_save.close()



with zipfile.ZipFile(zipfile_name,'r') as zip: 
					# printing all the contents of the zip file    
					# extracting all the files 
					print('Extracting all the files now...') 
					#zip.extractall(r'C:\Users\rohitd\Downloads')
					zip.extractall()
					print('Done!')

												
r =redis.StrictRedis('localhost', 6379, charset="utf-8", decode_responses=True)

with open(csvfile_name) as csvfile:
					content=csv.reader(csvfile)
					i=1
					for row in content:
								if (row[0] != 'SC_CODE'):
											r.hmset(i,{r"code":row[0],r"name":row[1],r"open":row[4],r"high":row[5],r"low":row[6],r"close":row[7]} )
											i=i+1
