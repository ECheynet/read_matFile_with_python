# -*- coding: utf-8 -*-
"""
Created on Tue May  3 07:33:17 2022

@author: Etienne Cheynet
"""

import numpy as np
import matplotlib.pyplot as plt
from functions import getP_15MW, datenum_to_datetime
import scipy.io


# %% Load the data at 150 m
data= scipy.io.loadmat('SNII_1992_2020_150m.mat')

Dir = np.squeeze(np.array(data['Dir']))
U = np.squeeze(np.array(data['U']))
t = np.squeeze(np.array(data['t']))

time = datenum_to_datetime(t)

time = time[~np.isnan(U)]
DirU = Dir[~np.isnan(U)]
U = U[~np.isnan(U)]
# %% Plot the time series

fig = plt.figure(1)
ax = fig.add_subplot(1, 1, 1)
ax.plot(time, U, 'r')
ax.set_ylabel('Mean wind speed at  150 m (m/s)')
ax.set_xlabel('time')
plt.grid()
plt.show()

# %% Interpolate the power curve over the mean wind speed

turbineModel = 'NREL_15MW.txt'

P, cf = getP_15MW(U,turbineModel)

print('Capacity factor is %1.2f' % cf)


# %% PLot the power curve
fig = plt.figure(1)
ax = fig.add_subplot(1, 1, 1)
ax.plot(U,P/1e6, 'r.')
ax.set_ylabel('Power (MW)')
ax.set_xlabel('Mean wind speed (m/s)')
plt.grid()
plt.show()


# %% PLot the time series of the median power
fig = plt.figure(1)
ax = fig.add_subplot(1, 1, 1)
ax.plot(time[0:1000],P[0:1000]/1e6, 'b.')
ax.set_ylabel('Power (MW)')
ax.set_xlabel('time')
plt.grid()
plt.show()


