# read .mat File with python

## Summary
This Python code is an example of how to import wind data from a .mat file and interpolate the power output of a 15 MW wind turbine model over the range of wind speed used as input.
Getting Started

## Libraries
The following libraries are required to run the code:

    numpy
    matplotlib.pyplot
    scipy
    datetime
    pandas

## Content

The code contains two functions, datenum_to_datetime and getP_15MW.

 - datenum_to_datetime: This function converts the datenum (Matlab datenum format) to datetime. It takes an input argument datenums (array of datenums) and returns an output time (array of datetime).
 
 - getP_15MW: This function interpolates the power output of the wind turbine model over the range of wind speed used as input. The interpolation scheme used is Akima. It takes two input arguments: (1) U: array of wind speed (2) turbineModel: string giving the text file with the power curve. The file is obtained from https://nrel.github.io/turbine-models/Offshore.html. It returns two outputs:(1) P: Power output of the wind turbine for each wind speed  and (2) cf: The total capacity factor
