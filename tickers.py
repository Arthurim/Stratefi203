# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 13:45:05 2017

@author: Arthur
"""

TICKERS = {'INDU:IND':'Index', 'SPX:IND':'Index', 'UKX:IND':'Index', 'DAX:IND':'Index', 'CAC:IND':'Index', 'SHCOMP:IND':'Index', 'SX5E:IND':'Index', 'VIX:IND':'Index',
               'CO1:COM':'Commo', 'XAUUSD:CUR':'FX','EURUSD:CUR':'FX', 'EURGBP:CUR':'FX','libor/american-dollar/usd-libor-interest-rate-3-months.aspx':'Rate','euribor/euribor-interest-3-months.aspx':'Rate','USGG10YR:IND':'Yield','GDBR10:IND':'Yield','GFRN10:IND':'Yield'}

ticker_fx = {'XAUUSD=X':'FX','EURUSD=X':'FX', 'EURGBP=X':'FX'}
ticker_commo = {'CO1:COM':'Commo',}
ticker_index_bloom = {'INDU:IND':'Index', 'SPX:IND':'Index', 'UKX:IND':'Index', 'DAX:IND':'Index', 'CAC:IND':'Index', 'SHCOMP:IND':'Index', 'SX5E:IND':'Index', 'VIX:IND':'Index'}
ticker_index = {'^DJI':'Index', '^SPX':'Index', '^FTSE':'Index', '^GDAXI':'Index', '^FCHI':'Index', '^SSEC':'Index', '^STOXX50E':'Index', '^VIX':'Index'}
ticker_rate = {'libor/american-dollar/usd-libor-interest-rate-3-months.aspx':'Rate','euribor/euribor-interest-3-months.aspx':'Rate'}
ticker_yield = {'USGG10YR:IND':'Yield','GDBR10:IND':'Yield','GFRN10:IND':'Yield'}
#%%