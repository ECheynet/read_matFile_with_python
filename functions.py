# -*- coding: utf-8 -*-
"""
Created on Tue May  3 07:31:39 2022

@author: Etienne Cheynet
"""
import datetime
import numpy as np
import pandas as pd
from scipy.interpolate import Akima1DInterpolator
from numpy import genfromtxt

def datenum_to_datetime(datenums):
   
    time = pd.to_datetime(datenums-719529, unit='D')
    return time    

    

def getP_15MW(U,turbineModel):    
    """
    getP_15MW(U,turbineModel) interpolate the power output of the wind turbine
    model over the range of wind speed used as input. 
    The interpolation scheme is Akima
    
    Input: 
        - U: array of wind speed
        - turbineModel: string giving the text file with the power curve. 
        The latter is taken from https://nrel.github.io/turbine-models/Offshore.html
        
    Output
        - P: Power output of the wind turbine for each U
        - cf: the total capacity factor 
        
    Author: E. Cheynet - UiB - Last modified: 03-05-2022
    """
    
    myData = genfromtxt(turbineModel, delimiter=',')
    
    U0 = myData[1:,0]
    P0 = myData[1:,1]*1e3

    P = Akima1DInterpolator(U0,P0)(U)
    P[U<3] = 0
    P[U>25] = 0
    P[np.isnan(P)] = 0
    P[P<0] = 0
    
    cf = np.sum(P)/(15e6*np.prod(U.shape))
    
    return P,cf