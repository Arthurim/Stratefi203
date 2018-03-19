# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 18:46:49 2017
@author: Arthur
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.externals import six
from datetime import datetime
import calendar
#%%
def to_table(data, title, col_width=2.5, row_height=0.5, font_size=14,
                     header_color='#48B4B8', row_colors=['#e7f4f5', 'w'], edge_color='w',
                     bbox=[0, 0, 1, 1], header_columns=0,
                     ax=None, **kwargs):
    if ax is None:
        size = (np.array(data.shape[::-1    ]) + np.array([0, 1])) * np.array([col_width, row_height])
        fig, ax = plt.subplots(figsize=size);
        ax.axis('off');
    #plt.title(title);
    day = 'As of '+ calendar.month_name[datetime.today().month][:3]+'. '+str(datetime.today().day)+ "th"
    col_header = ['', day ,'Weekly Change', 'YTD']
    col_labels = tuple(col_header)
    mpl_table = ax.table(cellText=data.values, bbox=bbox, colLabels=col_labels, cellLoc='center', **kwargs);
    mpl_table.auto_set_font_size(False);
    mpl_table.set_fontsize(font_size);
    myfont = {'fontname':'Arial'}
    for k, cell in six.iteritems(mpl_table._cells):
        cell.set_edgecolor(edge_color);
        if k[0] == 0 or k[1] < header_columns:
            cell.set_text_props(weight='bold', color='w', **myfont);
            cell.set_facecolor(header_color);
        else:
            cell.set_facecolor(row_colors[k[0]%len(row_colors) ])
            cell.set_text_props(**myfont);
    for i in range(18):
        mpl_table._cells[(i+1,0)]._text.set_weight('semibold');
        mpl_table._cells[(i+1,0)]._loc='left';
    for i in range(4):
        mpl_table._cells[(0,i)]._text.set_weight('semibold');   
        mpl_table._cells[(0,i)]._text.set_size(18);
    for i in range(1,19):
        for j in range(2,4):
            if(mpl_table._cells[(i,j)]._text.get_text()[0]=='-'):
                mpl_table._cells[(i,j)]._text.set_color('#FF0000')
            else:
                mpl_table._cells[(i,j)]._text.set_color('#16B84E')
    return fig;

def save_fig(fig,name,path):
        #day = '_As of '+ calendar.month_name[datetime.today().month][:3]+'.'+str(datetime.today().day)+ "th"
        fig.savefig(path+name,bbox_inches='tight',pad_inches=0.0)