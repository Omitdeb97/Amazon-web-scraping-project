#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Imporing libraries.
from bs4 import BeautifulSoup
import time
import datetime
import requests

import smtplib


# In[4]:


# Connect to Amazon website
url = 'https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data%2Banalyst%2Btshirt&qid=1626655184&sr=8-3&customId=B0752XJYNL&th=1%27'

header1 = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}

page = requests.get(url)

soup1 = BeautifulSoup(page.content, 'html.parser')

soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')

title = soup2.find(id='productTitle').get_text()

raiting  = soup2.find(id = "acrCustomerReviewLink").get_text()

detailes  = soup2.find(id = "detailBulletsWrapper_feature_div").get_text()



print(title)

print(raiting)

print(detailes)





# In[5]:


title = title.strip()
raiting  = raiting .strip()
detailes = detailes.strip()

print(title)
print(raiting)


# In[6]:


price = soup2.find(class_ = "a-price-whole").get_text()
print(price)


# In[7]:


# Importing datetime
import datetime

date = datetime.date.today()
print(date)


# In[8]:


import csv

header = ['title', 'raiting','date']

data = [title, raiting, date]
type(data)

# Creating csv file
with open('Amazonwebdata.csv','w', newline='', encoding='UTF8') as f:
    write = csv.writer(f)
    write.writerow(header)
    write.writerow(data)


# In[ ]:





# In[9]:


# Appending data to csv file
with open('Amazonwebdata.csv','a+', newline='', encoding='UTF8') as f:
    write = csv.writer(f)
    write.writerow(data)


# In[ ]:





# In[10]:


import pandas as pd
df = pd.read_csv(r'C:\Users\amitd\Amazonwebdata.csv')
df


# In[ ]:





# In[11]:


# Checking data

def check_data():
    url = 'https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data%2Banalyst%2Btshirt&qid=1626655184&sr=8-3&customId=B0752XJYNL&th=1%27'

    header1 = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}

    page = requests.get(url)

    soup1 = BeautifulSoup(page.content, 'html.parser')

    soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')

    title = soup2.find(id='productTitle').get_text()

    raiting  = soup2.find(id = "acrCustomerReviewLink").get_text()
    
    title = title.strip()
    
    raiting  = raiting .strip()
    
    import datetime

    date = datetime.date.today()
    
    import csv

    header = ['title', 'raiting','date']

    data = [title, raiting, date]

    with open('Amazonwebdata.csv','a+', newline='', encoding='UTF8') as f:
        write = csv.writer(f)
        write.writerow(data)


# In[14]:


# Running the check_data function
while (True):
    check_data()
    time.sleep(5)


# In[15]:


import pandas as pd
df = pd.read_csv(r'C:\Users\amitd\Amazonwebdata.csv')
df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




