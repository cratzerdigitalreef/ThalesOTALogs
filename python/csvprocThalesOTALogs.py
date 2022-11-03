# -*- coding: UTF-8 -*-
 
import sys 
from csvproc import *

print("Starting")

n = 1

sProc = "CSV"
if len(sys.argv) > n:
   sProc = sys.argv[n]
n = n + 1

csvPathPattern = ""
if len(sys.argv) > n:
   csvPathPattern = sys.argv[n]
n = n + 1
 
sSeparaCSV = ";"
if len(sys.argv) > n:
   sSeparaCSV = sys.argv[n]
n = n + 1
   
sOut = "out"
if len(sys.argv) > n:
   sOut = sys.argv[n]
n = n + 1

sMilesSepara = "."
if len(sys.argv) > n:
   sMilesSepara = sys.argv[n]
n = n + 1

sPrint = "PROCESS: " + str(sProc)
sPrint = sPrint + "\n" + "Path and pattern for CSV files: " + str(csvPathPattern)
sPrint = sPrint + "\n" + "Separator CSV: " + str(sSeparaCSV)
sPrint = sPrint + "\n" + "Out File: " + str(sOut)
sPrint = sPrint + "\n" + "Miles Separator: " + str(sMilesSepara)

print(sPrint)
print("\n")

ret = csv_proc(sProc, csvPathPattern, sSeparaCSV, sOut, sPrint, sMilesSepara)

print("\n\nResult: \n" + str_AddThousandToNumber(str(ret), sMilesSepara) + " lines processed.\n")

