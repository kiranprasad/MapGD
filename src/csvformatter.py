#WIP source code
import numpy as np
import csv
import os

inCSV = "./Project-Data/csv-files/astrodocs.csv"
outCSV = "./Project-Data/csv-files/AnA_clean.csv"
year = []
totaldoc = []

def csvops (filename, ftype, rw):
    if rw == 'r':
        with open(filename, newline='') as csvfile:
                csvarray=np.loadtxt(csvfile, dtype=ftype, skiprows=1, delimiter=',')
                return csvarray
    elif rw == 'w':
        with open(filename, 'w', newline='') as csvout:
            np.savetxt(csvout, totaldoc, fmt='%d', delimiter=',')        

                
def evalcsv(csvinput):
  
    array_length = np.ma.size(csvinput,0)
    '''
    Astrodocs csv has the format:
    Doc_type, Year, Citation_numeric_count 
    Ordered Non-citable first followed by all citable docs.
    '''
    for x in range(0,array_length):
        if x < int(array_length/2):
            year.append([int(csvinput[x][1])])
            totaldoc.append([int(csvinput[x+int((array_length-1)/2)+1][2]) + int(csvinput[x][2])])

    doc = np.column_stack((year, totaldoc))
    return doc

totaldoc = evalcsv(csvops(inCSV,'str','r'))
try:
    csvops(outCSV,'str','w')
except:
    FileNotFoundError
