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
def to_table(data, title, col_width=5.0, row_height=0.625, font_size=14,
                     header_color='#40466e', row_colors=['#f1f1f2', 'w'], edge_color='w',
                     bbox=[0, 0, 1, 1], header_columns=0,
                     ax=None, **kwargs):
    if ax is None:
        size = (np.array(data.shape[::-1    ]) + np.array([0, 1])) * np.array([col_width, row_height])
        fig, ax = plt.subplots(figsize=size);
        ax.axis('off');
    #plt.title(title);
    col_header = ['', 'As of '+ calendar.month_name[datetime.today().month][:3]+'. '+str(datetime.today().day)+ "th" ,'Weekly Change', 'YTD']
    col_labels = tuple(col_header)
    mpl_table = ax.table(cellText=data.values, bbox=bbox, colLabels=col_labels, cellLoc='center', **kwargs);
    mpl_table.auto_set_font_size(False);
    mpl_table.set_fontsize(font_size);
    for k, cell in six.iteritems(mpl_table._cells):
        cell.set_edgecolor(edge_color);
        if k[0] == 0 or k[1] < header_columns:
            cell.set_text_props(weight='bold', color='w');
            cell.set_facecolor(header_color);
        else:
            cell.set_facecolor(row_colors[k[0]%len(row_colors) ])
    return fig;

def save_fig(fig,name,path):
    fig.savefig(path+name)
#%%













