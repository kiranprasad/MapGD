#WIP source
import csv
import math
import os
import re
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import beta
from scipy.integrate import quad

FLATFILE_DIR = './Project-Data/csv-files'
'''
plot shtuff using basic plotting
TBD: Make the graph actually useful. 
'''

def plot_things (xaxis,yaxis):
    
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
            alpha.append([(math.log(scjr)-math.log(arts)-math.log(beta(icrp+1,cite))) / (math.log(hind)-math.log(beta(icrp+1,cite)))])
        else:
            alpha.append([0])
        
    alphaout = np.column_stack((year,alpha))
    return alphaout

def betaout(a,b):
    res = math.exp(math.lgamma(a) + math.lgamma(b) - math.lgamma(a+b))
    return res

def integrand(solution):
    return solution

def sjrcompute(data,alpha):
    sjr = []
    sjroriginal = []
    year = []
    size = np.ma.size(data,0)
    hind = int(data[size-1][0])
    
    for x in range(size-1):
        year.append(int(data[x][0]))
        cite = int(data[x][1])
        icrp = float(data[x][2])/100
        arts = int(data[x][3])
        sjroriginal.append([float(data[x][4])])
        if cite != 0:
            # solution = betaout(cite,icrp+1)
            # #beta = (math.gamma(cite)*math.gamma(icrp+1)/math.gamma(icrp+1+cite))^(alpha)
            # intg, err = quad(integrand,0,arts)
            outp = alpha*math.log(hind)+math.log(arts)+(1-alpha)*math.log(beta(cite,icrp+1))
            sjr.append([math.exp(outp)])
        else:
            sjr.append([0])
        
    alphaout = np.column_stack((year,sjr))
    plot_things(year, sjr)
    return alphaout


'''
Flatfile for all input parameters
# '''
# directory_listing = os.listdir(FLATFILE_DIR)

# for filename in directory_listing:
#     filepath = os.path.join(FLATFILE_DIR, filename)
#     data = csvops(filepath,'str','r')
#     journalpha = alpha_compute(data)
#     outfile = os.path.join(FLATFILE_DIR,"alpha_"+filename)
#     csvops(outfile,'%s','w')

# #SJR compute
# directory_listing = os.listdir(FLATFILE_DIR)

# for filename in directory_listing:
#     filepath = os.path.join(FLATFILE_DIR, filename)
#     data = csvops(filepath,'str','r')
#     journalpha = sjrcompute(data)
#     outfile = os.path.join(FLATFILE_DIR,"sjr_"+filename)
#     csvops(outfile,'%s','w')
alphapath = os.path.join("./Project-Data/alpha","alpha_ICARUS.csv")
alphadata = csvops(alphapath,'float','r')
alphaval = np.median(alphadata,0)
filepath = os.path.join(FLATFILE_DIR,"ICARUS.csv")
data = csvops(filepath,'str','r')
journalpha = sjrcompute(data,alphaval[1])
outfile = os.path.join(FLATFILE_DIR,"sjr_ICARUS.csv")
csvops(outfile, '%s','w')