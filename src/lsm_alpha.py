#WIP source
import csv
import math
import os

import matplotlib.pyplot as plt
import numpy as np
from scipy.special import beta

FLATFILE_DIR = './Project-Data/csv-files/'
'''
plot shtuff using basic plotting
TBD: Make the graph actually useful. 
'''

def plot_things (xaxis, yaxis):
    
    plt.plot(xaxis, yaxis, '--o')
    plt.show()

def csvops (csvdata, ftype, rw):
    
    if (rw=='r'):
        with open(csvdata, newline='') as csvfile:
            csvarray=np.loadtxt(csvfile, dtype=ftype, skiprows=1, delimiter=',')

        return csvarray
    elif(rw=='w'):
        with open(csvdata, 'w', newline='') as csvfile:
            np.savetxt(csvfile, journalpha, fmt=ftype, delimiter=',') 


def alpha_compute(data):
    alpha = []
    year = []
    size = np.ma.size(data,0)
    hind = int(data[size-1][0])
    
    for x in range(size-1):
        year.append(int(data[x][0]))
        cite = int(data[x][1])
        icrp = float(data[x][2])/100
        arts = int(data[x][3])
        scjr = float(data[x][4])
        if cite != 0:
            alpha.append([(math.log(scjr)-arts*math.log(0.1*beta(icrp+1,hind))) / (math.log(cite)-arts*math.log(0.1*beta(icrp+1,hind)))/2])
        else:
            alpha.append([0])
        
    alphaout = np.column_stack((year,alpha))
    return alphaout

'''
Flatfile for all input parameters
'''
directory_listing = os.listdir(FLATFILE_DIR)

for filename in directory_listing:
    filepath = os.path.join(FLATFILE_DIR, filename)
    data = csvops(filepath,'str','r')
    journalpha = alpha_compute(data)
    outfile = os.path.join(FLATFILE_DIR,"alpha_"+filename)
    csvops(outfile,'%s','w')