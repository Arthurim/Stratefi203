# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 14:21:16 2018

@author: Arthur
"""

import smtplib
import datetime
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
from time import sleep
from random import randint
import numpy as np
import locale

from IPython.display import Image
#%%
"""
Getting the information for the email: headlines, quote
"""
url = "https://docs.google.com/presentation/d/1SlDXHs-JzIcm2eXuzFEFxTe8zwrP5oVCiG7RgCj_Uws/edit#slide=id.g29879e9358_14_0"
page = urlopen(url)
sleep(randint(1,3))
soup = BeautifulSoup(page,"lxml")
pages = soup.find_all("div", {"id": "pages"})
svg = soup.find_all("svg", {"xmlns": "http://www.w3.org/2000/svg"})
myg = soup.find_all("g", {"id": "editor-g29879e9358_14_11"})
t= soup.find_all("g",{"class":"sketchy-text-content-text"})

#%%
"""
Drafting the email
"""
now = datetime.datetime.now()
mth = now.strftime("%b")
d = str(now.day)

options = {'0' : 'th',
           '1' : 'st',
           '2' : 'th',
           '3' : 'rd',
           '4' : 'th',
           '5' : 'th',
           '6' : 'th',
           '7' : 'th',
           '8' : 'th',
           '9' : 'th'}
c=options[str(d)[-1]]

subject = 'tt'#The Week At a Glance - '+ mth + '. ' + d + c 

sent_from = 'newsletter.m203@gmail.com'  
to = ['newsletter.m203@gmail.com']  

body = "Dear Glancers, \n\
        \nThe Week At a Glance is out. \
        \nIn this issue: \n\
- %s \n\
- %s \n\
- %s\n\
- %s\n\
- %s\n\
\n\
Did you know that %s ?\n\
\n\
Quote of the day: %s \n\
\n\
Have a great week.\n\
\n\
The Week At a Glance Team" % ("A","B","C","D","E","F","G")

message = 'Subject: {}\n\n{}'.format(subject, body)
#%%
"""
Sending the email
"""
gmail_user = 'newsletter.m203@gmail.com'  
gmail_password = 'Newsleter'

try:  
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, message)
    server.close()
    print('Email sent')
except:  
    print('Something went wrong...')