# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 20:04:28 2017

@author: Arthur
"""

from scraper import scraper, clean_data, compute_data,format_table
import pandas as pd
from tickers import TICKERS


def main():
    path = "C:\\Users\Arthur\Documents\Studies\Paris Dauphine University\Master203\\Newsletter\\"
    price_list = []
    for ticker, sec in TICKERS.items():
        price_list.append(scraper(ticker,sec))
    price_list = clean_data(price_list)
    ComputingTable = compute_data(price_list,path)
    TableStr = format_table(ComputingTable, path)
    return TableStr

if __name__ == "__main__":
    TableStr = main()