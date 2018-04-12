import os
import numpy as np
import matplotlib.pyplot as plt

SJR_DIR = './Project-Data/SJR'

def csvops (csvdata, ftype, rw):
    
    if (rw=='r'):
        with open(csvdata, newline='') as csvfile:
            csvarray=np.loadtxt(csvfile, dtype=ftype, skiprows=1, delimiter=',')

        return csvarray
    elif(rw=='w'):
        with open(csvdata, 'w', newline='') as csvfile:
            np.savetxt(csvfile, journaldata, fmt=ftype, delimiter=',') 

def plot_things (xaxis1,yaxis1): 
    plt.plot(xaxis1, yaxis1, '--o')
    # plt.plot(xaxis1, yaxis2, '--or')
    plt.xticks(np.arange(min(xaxis1), max(xaxis1)+1, 1.0))
    # plt.yticks(np.arange(min(yaxis1),0.1+max(yaxis1), 0.5))
    plt.xlabel("Year")
    plt.ylabel("Predicted SJR")
    #plt.title(filename)
    plt.show()


anapath = os.path.join(SJR_DIR,'AstronomyandAstrophysics.csv')
mnrpath = os.path.join(SJR_DIR,'MonthlyNotices_of_TheRoyal_Astronomical_Society.csv')
apjpath = os.path.join(SJR_DIR,'Astrophysical_Journal.csv')
output=[]
year=[]
ana = csvops(anapath, 'str', 'r')
mnr = csvops(mnrpath, 'str','r')
apj = csvops(apjpath,'str','r')
size = np.ma.size(ana,0)
for x in range(size-1):
    year.append(float(ana[x][0]))
    #print(year)
    output.append([float(ana[x][1]), float(mnr[x][1]), float(apj[x][1])])

outarr = np.array(output)
meansjr = np.median(outarr,1)
mediansjr = np.median(outarr, 0)
print(meansjr)
print(mediansjr)
plot_things(year, meansjr)