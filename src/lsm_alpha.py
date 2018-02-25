#WIP source
import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import beta

'''
plot shtuff using basic plotting
TBD: Make the graph actually useful. 
'''

def plot_things (xaxis, yaxis):
    
    plt.plot(xaxis, yaxis, '--o')
    plt.show()

def csvread (filename, ftype):
    
    with open(filename, newline='') as csvfile:
        csvarray=np.loadtxt(csvfile, dtype=ftype, skiprows=0, delimiter=',')

    return csvarray

'''
Flatfiles for all input parameters.
'''
sjr = csvread('filename.csv','int') #Y
betainput = csvread('betafunc.csv','float') #i and p
totalarticles = csvread('articlecount.csv', 'int') #A

'''
setting PSI to 1 and evaluating alpha from Romer model using stochastic model of citation
''' 
alpha = []
alpha.append(np.log(Y) - A*np.log(beta(i,p+1))) / (np.log(T)-A*np.log(beta(i,p+1))))

