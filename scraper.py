# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 20:48:08 2017

@author: Arthur
"""

"""
This code is meant to udpdate the table of prices/indices etc
"""

from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
from time import sleep
from tickers import TICKERS
from graph import to_table, save_fig
import numpy as np
import locale
#%%
# function meant to scrap the prices
def scraper(ticker, asset_class):
    if asset_class in ("Yield","Commo","Index","FX"):
        print(ticker)
        url = "https://www.bloomberg.com/quote/%s"%(ticker)
        myclass="price"
        page = urlopen(url)
        sleep(5)
        soup = BeautifulSoup(page,"lxml")
        prices = soup.find(class_="price")
        price = prices.get_text()
        if asset_class == 'Yield':
            price=str(float(price)/100)
    elif asset_class == 'Rate':
        url = "http://www.global-rates.com/interest-rates/"+ ticker
        myclass = "tabledata1"
        page = urlopen(url)
        sleep(5)
        soup = BeautifulSoup(page,"lxml")
        data = soup.find(class_=myclass)
        price = data.find(align='center').get_text()
        price = str(float(price.replace('\xa0%',''))/100)
    else:
        print("Asset class not recognized")
    return price

# Clean data
def clean_data(price_list):
    price_list=[s.replace('N/A','NaN') for s in price_list]
    price_list=[s.replace(',','') for s in price_list]
    price_list=list(map(float,price_list))
    return price_list

# ComputingTable is the csv meant to store the computations
# Laod csv, update prices, and save
def compute_data(price_list,path):
    ComputingTable = pd.read_csv(path+"ComputingTable.csv", encoding='latin1', index_col=0)
    ComputingTable['Today'] = price_list              
    ComputingTable['Weekly Change'] = (ComputingTable['Today']-ComputingTable['Last Week'])/ComputingTable['Last Week']
    ComputingTable['YTD'] = (ComputingTable['Today']-ComputingTable['As of Jan 2nd'])/ComputingTable['As of Jan 2nd']
    ComputingTable['Last Week'] = ComputingTable['Today']
    ComputingTable.to_csv(path+"ComputingTable.csv")
    return ComputingTable
#%%
# Table is the table of data meant to be copy psated on the newsletter
def format_table(ComputingTable,path):
    Table = pd.DataFrame()
    Table['Securities']=ComputingTable.index
    Table['Today']=ComputingTable['Today'].values
    Table['Weekly Change']=ComputingTable['Weekly Change'].values
    Table['YTD'] = ComputingTable['YTD'].values
    for i in range(12,len(Table)-1):
        Table['Today'][i]=pd.Series(Table['Today'][i]*100).apply('{0:.2f}%'.format)[0]
    for col in ['YTD','Weekly Change']:
        Table[col] = pd.Series(["{0:.2f}%".format(val * 100) for val in Table[col]], index = Table.index)
    #decimals = pd.Series([0,2,2, 2], index=['Securities', 'Today', 'Weekly Change', 'YTD'])
    #Table=Table.round(decimals)     
    for i in range(7):
        Table['Today'][i]=round(Table['Today'][i],0)
    for i in range(7):
        Table['Today'][i]='{:,}'.format(Table['Today'][i]).replace(',',' ')
    Table['Today'][17]=round(Table['Today'][17],0)
    Table['Today'][17]='{:,}'.format(Table['Today'][17]).replace(',',' ')
    TableStr=Table.astype(str)
    TableStr=TableStr.applymap(lambda x: str(x.replace('.',',')))
    TableStr['Today']=TableStr['Today'].map(lambda x: str(x.replace(',0','')))
    TableStr.to_csv(path+"ValuesTable.csv")
    save_fig(to_table(TableStr,'Table'),'Table.png',path)
    return TableStr

