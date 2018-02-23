#WIP source
import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import beta, gamma

'''
plot shtuff using basic plotting
TBD: Make the graph actually useful. 
'''

def plot_things (xaxis, yaxis):
    
    plt.plot(xaxis, yaxis, '--o')
    plt.show()

def csvread (filename, ftype):
    
    with open(filename, newline='') as csvfile:
        csvarray=np.loadtxt(csvfile, dtype=ftype, skiprows=1, delimiter=',')

    return csvarray
    '''
    csv list to ndarray conversions. 
    If there is better solution, please fix and comment
    '''

csvx=[]
csvy=[]
csvint = csvread('/home/kranep/MapGD/Project-Data/csv-files/ICARUS.csv','float') #.astype(float)     
for x in range(0,np.ma.size(csvint,0)):
    csvx.append([csvint[x][0]])
    csvy.append([csvint[x][1]])
xn = np.array(csvx)
yn = np.array(csvy)
print(xn)

