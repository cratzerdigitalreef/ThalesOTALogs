
from str import *
import glob
import sys
import csv
	

print(glob.glob("/home/adam/*"))

# files_getCurrentPath ----------------------------------------------------------------------------------------------------------
def files_getCurrentPath():
    #CURRENT PATH
    from pathlib import Path
    #sPath = Path().absolute()
    sPath = Path(__file__).parent.absolute()
    return sPath
    
# files_getFiles ----------------------------------------------------------------------------------------------------------
def files_getFiles(sPattern):
    return glob.glob(sPattern)

# files_OpenCSVForRead ----------------------------------------------------------------------------------------------------------
def files_OpenCSVForRead(csvFile, sSeparaCSV):
    return csv.reader(open(csvFile, 'r'), delimiter=sSeparaCSV)