# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 19:05:25 2022

@author: Dhananjay Bhujbal
"""
import pandas as pd
import matplotlib.pyplot as plt

def pcr(df):
    '''Get PCR value for given Option Chain'''
    
    pcr = sum(df['Put OI'])/sum(df['Call OI'])
    return pcr

def max_IV(df):
    '''Get maximum value of IV for given option chain'''
    
    max_value = max(df['IV'])
    return max_value

def max_IV_Index(df):
    '''Get index of maximum IV location'''
    
    index = df['IV'].idxmax()
    return index

def min_IV(df):
    ''' Get mimimum value of IV for given option chain'''
    
    min_value = min(df['IV'])
    return min_value

def min_IV_Index(df):
    '''Get index of maximum IV location'''
    
    index = df['IV'].idxmin()
    return index

def straddle(df):
    ''' Get straddle prices for each strike price in given option chain'''
    
    straddle = df['Call LTP'] + df['Put LTP']
    result = pd.DataFrame(straddle, columns = ['Straddle value'])
    return result

def max_straddle(df):
    ''' Get details about maximum straddle value'''
    
    straddle = df['Call LTP'] + df['Put LTP']
    index = straddle.idxmax()
    result = df.iloc[index]
    return result

def max_oi(df):
    ''' Get maximimum Call and Put OI values'''
    
    call_oi = max(df['Call OI'])
    put_oi = max(df['Put OI'])
    
    call_oi_index = df['Call OI'].idxmax()
    put_oi_index = df['Put OI'].idxmax()
    
    result = pd.DataFrame([(call_oi, call_oi_index), (put_oi, put_oi_index)], index= ['Call', 'Put'], columns=['Value', 'Index'])
    return result

class call_moneyness(object):
    def __init__(self, df):
        self.df = df
    
    def itm(self):
        return self.df[self.df['Call Delta'] > 0.50]
    
    def otm(self):
        return self.df[self.df['Call Delta'] < 0.50]
    
    def atm(self):
        return self.df[self.df['Call Delta'] == 0.50]
    
class put_moneyness(object):
    def __init__(self, df):
        self.df = df
        
    def itm(self):
        return self.df[self.df['Put Delta'] < -0.50]
    
    def otm(self):
        return self.df[self.df['Put Delta'] > -0.50]
    
    def atm(self):
        return self.df[self.df['Put Delta'] == -0.50]
    
def plot_iv(df):
    plot = plt.plot(df['IV'])
    plt.show()
