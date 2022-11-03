# -*- coding: UTF-8 -*-

import sys
sys.path.append('../libs')
 
import csv
from datetime import *
from dt import *
from str import *
from files import *
from validanro import *


#------------------------------------------------------------------------------------
# csv_proc => Start processing all CSV Files
#------------------------------------------------------------------------------------
def csv_proc(sProc, csvFiles, sSeparaCSV, sOut, sComments, sMilesSepara):

    sPrint = sComments
    
    #Separator for the csv_procFile returning data
    sReturnSepara = "#"
    sSeparaMiles = sMilesSepara
    
    #CURRENT PATH
    sPath = files_getCurrentPath()
    sPrint = sPrint + "\n" + "Directory Path: " + str(sPath)

    #GET DATETIME NOW
    sdtFormat = "%Y-%m-%d %H:%M:%S.%f"
    dateStart = datetime.now()    
    sdateStart = dateStart.strftime(sdtFormat)
    sPrint = sPrint + "\n" + "Processing CSV file started at: " + str(sdateStart) + "\n"

    # Get CSV files
    sPrint = sPrint + "\n" + "Processing files from " + csvFiles + ". "
    lcsvFiles = files_getFiles(csvFiles)
    nlcsvFiles = len(lcsvFiles)
    sPrint = sPrint + "\nTotal Files: " + str(nlcsvFiles)
    sList = str_Replace(str(lcsvFiles),",",str_GetENTER())
    sList = str_Replace(sList, "[", " ")
    sList = str_CleanPattern(sList, "]")
    sPrint = sPrint + "\nList of Files to process: \n" + sList + "\n"

    #print("FILES: " + str(lcsvFiles))
    #exit()
    
    #CREATE LOG FILE
    sdateStart_prn = dateStart.strftime("%Y%m%d_%H%M%S")
    sFileOut = sOut + "_" + str(sdateStart_prn) + ".txt"
    file2write=open(sFileOut,'a')
    file2write.write(sPrint + "\n")

    # Close output file
    file2write.close()

    # FOR TOTALS
    nSUCCEEDED = 0
    nFAILED = 0
    nINPROCESS = 0
    nICCIDs = 0
    nLines = 0
    nCANCELED = 0
    sRAPDUlstItem = []
    sRAPDUlstCount = []

    
    n=0
    while n < nlcsvFiles:
    
        csvFile = lcsvFiles[n]
        #print("csvFile: " + csvFile) 
        
        sReturn = csv_procFile(n+1, nlcsvFiles, sProc, csvFile, sSeparaCSV, sFileOut, sReturnSepara, sSeparaMiles)
 
        print("sReturn: " + sReturn)
        
        m = 0
        nLines = nLines + float(csv_ReturnGet(sReturnSepara, sReturn, m))
        
        m = m + 1 
        nSUCCEEDED = nSUCCEEDED + float(csv_ReturnGet(sReturnSepara, sReturn, m))
        print("nSUCCEEDED: " + str(nSUCCEEDED))
        
        m = m + 1 
        nFAILED = nFAILED + float(csv_ReturnGet(sReturnSepara, sReturn, m))

        m = m + 1 
        nINPROCESS = nINPROCESS + float(csv_ReturnGet(sReturnSepara, sReturn, m))

        m = m + 1 
        nICCIDs = nICCIDs + float(csv_ReturnGet(sReturnSepara, sReturn, m))

        m = m + 1 
        nCANCELED = nCANCELED + float(csv_ReturnGet(sReturnSepara, sReturn, m))
        
        #COUNT RAPDU
        m = m + 1 
        sRAPDUTemp = csv_ReturnGet(sReturnSepara, sReturn, m)
        if sRAPDUTemp != "0":
           
           while sRAPDUTemp != "":
                 
                 m = m + 1
                 sRAPDUCount = csv_ReturnGet(sReturnSepara, sReturn, m)
                 
                 mTot = len(sRAPDUlstItem)
                 bRAPDUFound = False
                 i = 0
                 while i < mTot and bRAPDUFound == False:
                       if sRAPDUlstItem[i]==sRAPDUTemp:
                          #ADD COUNT TO THE RAPDU COUNTER
                          sRAPDUlstCount[i] = str(int(sRAPDUlstCount[i]) + int(sRAPDUCount))
                          bRAPDUFound = True
                       i = i + 1 
                 if bRAPDUFound == False:
                    #ADD RAPDU IN THE LIST
                    sRAPDUlstItem.append(sRAPDUTemp)
                    sRAPDUlstCount.append(sRAPDUCount)

                 m = m + 1 
                 sRAPDUTemp = csv_ReturnGet(sReturnSepara, sReturn, m)

        n=n+1


    sRepeat = str_RepeatString(100, "*")

    #PREPARING RESULTS
    sLines = csv_PreparingResults(nLines, sSeparaMiles)
    sSUCCEEDED = csv_PreparingResults(nSUCCEEDED, sSeparaMiles)
    sFAILED = csv_PreparingResults(nFAILED, sSeparaMiles)
    sINPROCESS = csv_PreparingResults(nINPROCESS, sSeparaMiles)
    sICCIDs = csv_PreparingResults(nICCIDs, sSeparaMiles)
    sCANCELED = csv_PreparingResults(nCANCELED, sSeparaMiles)

    
    #TOTAL LINES PROCESSED
    sPrint = "\n" + sRepeat + "\n\n"
    sPrint = sPrint + "Result for all Files: \n" + sLines + " lines processed.\n"

    #RESULTS
    sPrint = sPrint + "\n"
    sPrint = sPrint + "TOTAL FILES: " + str(nlcsvFiles) + "\n"
    sPrint = sPrint + "TOTAL ALL FILES - SUCCEEDDED: " + sSUCCEEDED + "\n"
    sPrint = sPrint + "TOTAL ALL FILES - FAILED: " + sFAILED + "\n"
    sPrint = sPrint + "TOTAL ALL FILES - IN-PROCESS: " + sINPROCESS + "\n"
    sPrint = sPrint + "TOTAL ALL FILES - CANCELED: " + sCANCELED + "\n"
    sPrint = sPrint + "TOTAL ALL FILES - ICCIDs: " + sICCIDs + "\n"

    #RAPDU TOTALS
    mTot = len(sRAPDUlstItem)
    m = 0
    while m < mTot:
          if m == 0:
             sPrint = sPrint + "\n"
          sPrint = sPrint + "TOTAL ALL FILES - FAILED - TOTAL RAPDU " + sRAPDUlstItem[m] + " : " + str(sRAPDUlstCount[m]) + "\n"
          m = m + 1 
    
    # GET DATETIME NOW
    dateEnd = datetime.now()    
    sdateEnd = dateEnd.strftime(sdtFormat)
    delta = dt_difference(sdtFormat, dateStart, dateEnd, False)
    sPrint = sPrint + "\n" + "Processed files to '" + str(sFileOut) + "', finished: " + str(sdateEnd) + "\nElapsed: " + str(delta)
    
    #PRINT END
    sPrint = sPrint + "\n\n"
    sPrint = sPrint + sRepeat + "\n\n"
    print(sPrint)
    file2write=open(sFileOut,'a')
    file2write.write(sPrint)
    file2write.close()

    return nLines

#------------------------------------------------------------------------------------
# csv_procFile => Process specific CSV file
#------------------------------------------------------------------------------------
def csv_procFile(nFile, nTotalFiles, sProc, csvFile, sSeparaCSV, sFileOut, sReturnSepara, sSeparaMiles):

    sRepeat = str_RepeatString(100, "-")
    sRAPDU = "RAPDU"
    
    sRAPDUlstItem = []
    sRAPDUlstCount = []
    
    sStatusSUCCEDDED = "SUCCEEDED"
    sStatusFAILED = "FAILED"
    sStatusINPROGRESS = "IN-PROCESS"
    sStatusCANCELED = "CANCELED"
    
    sSeparaListas = ","
    
    sPrint = sRepeat
    
    #GET DATETIME NOW
    sdtFormat = "%Y-%m-%d %H:%M:%S.%f"
    dateStart = datetime.now()    
    sdateStart = dateStart.strftime(sdtFormat)
    sPrint = sPrint + "\n\nProcessing CSV file " + str(nFile) + " of " + str(nTotalFiles) + " - '" + csvFile + "' started at: " + str(sdateStart) + "\n"

    #UPDATE LOG FILE
    file2write=open(sFileOut,'a')
    file2write.write(sPrint)
    # Close output file
    file2write.close()

    # OPEN CSV FILE
    reader = csv.reader(open(csvFile, 'r'), delimiter=sSeparaCSV)

    nSUCCEEDED = 0
    nFAILED = 0
    nINPROCESS = 0
    nICCIDs = 0
    nCANCELED = 0
    
    n=0
    for row in reader:

        datenow = datetime.now()    
        sdatenow = datenow.strftime(sdtFormat)
        sProcessingFile = "Processing file " + str(nFile) + " of " + str(nTotalFiles) + " - '" + csvFile + "', line " + str(n) + "... at " + str(sdatenow)
        sPrint = sProcessingFile
        
        #VALIDATE IT IS AN ICCID
        bProcess = False
        
        #print("ROW: " + str(row) + " - SEPARATOR: " + sSeparaCSV)
        sICCID = ""
        
        if str_instrBool(str(row),sSeparaListas): 
           sICCID = csv_GetICCID(row)
           if sICCID != "":
              bProcess = True
        
        #print("ICCID: " + sICCID) 
         
        sStatus = ""       
        if bProcess:    
           sStatus = csv_GetSTATUS(row, sStatusSUCCEDDED, sStatusFAILED, sStatusINPROGRESS, sStatusCANCELED)

        if bProcess:

           #sPrint = sPrint + " - Processed Line: " + str(bProcess) + " - " + str(row)
           sPrint = sPrint + " - Processed Line: " + str(bProcess)
           if sICCID != "":
              sPrint = sPrint + " - ICCID: " + sICCID + " - STATUS: " + sStatus
           print(sPrint)
        
           nICCIDs = nICCIDs + 1
           
           #------------------------------------------------------------------------------------
           #IT IS MANDATORY TO GET THE COLUMN TO PROCESS
           #------------------------------------------------------------------------------------
           #GET STATUS

           if sStatus == sStatusSUCCEDDED:
              nSUCCEEDED = nSUCCEEDED + 1
              
           if sStatus == sStatusFAILED:
              nFAILED = nFAILED + 1
              sRAPDUf = csv_GetPattern(row, sRAPDU, sSeparaCSV)
              if sRAPDUf != "":
                 #WRITE RPADU
                 sPrint = "\n+++ ICCID: " + sICCID + " - RAPDU: " + sRAPDUf
                 sPrint = sPrint + ". " + sProcessingFile

                 #WRITE RAPDU IN THE LOG 
                 file2write=open(sFileOut,'a')
                 file2write.write(sPrint)
                 file2write.close()
                 
                 #COUNT RAPDU
                 mTot = len(sRAPDUlstItem)
                 m = 0
                 bRAPDUFound = False
                 while m < mTot and bRAPDUFound == False:
                       if sRAPDUlstItem[m]==sRAPDUf:
                          #ADD 1 TO THE RAPDU COUNTER
                          sRAPDUlstCount[m] = str(int(sRAPDUlstCount[m]) + 1)
                          bRAPDUFound = True
                       m = m + 1 
                 if bRAPDUFound == False:
                    #ADD RAPDU IN THE LIST
                    sRAPDUlstItem.append(sRAPDUf)
                    sRAPDUlstCount.append("1")


           if sStatus == sStatusINPROGRESS:
              nINPROCESS = nINPROCESS + 1

           if sStatus == sStatusCANCELED:
              nCANCELED = nCANCELED + 1
            
           #------------------------------------------------------------------------------------

        n=n+1

    n=n-1
    
    #PREPARING RESULTS
    sLines = csv_PreparingResults(n, sSeparaMiles)
    sSUCCEEDED = csv_PreparingResults(nSUCCEEDED, sSeparaMiles)
    sFAILED = csv_PreparingResults(nFAILED, sSeparaMiles)
    sINPROCESS = csv_PreparingResults(nINPROCESS, sSeparaMiles)
    sICCIDs = csv_PreparingResults(nICCIDs, sSeparaMiles)
    sCANCELED = csv_PreparingResults(nCANCELED, sSeparaMiles)

    #TOTAL LINES PROCESSED
    sPrint = "\nResult for file '" + csvFile + "': \n" + sLines + " lines processed.\n"

    #RESULTS
    sPrint = sPrint + "\n"
    sPrint = sPrint + "File '" + csvFile + "' - TOTAL SUCCEEDDED: " + sSUCCEEDED + "\n"
    sPrint = sPrint + "File '" + csvFile + "' - TOTAL FAILED: " + sFAILED + "\n"
    sPrint = sPrint + "File '" + csvFile + "' - TOTAL IN-PROCESS: " + sINPROCESS + "\n"
    sPrint = sPrint + "File '" + csvFile + "' - TOTAL CANCELED: " + sCANCELED + "\n"
    sPrint = sPrint + "File '" + csvFile + "' - TOTAL ICCIDs: " + sICCIDs + "\n"
    
    #RAPDU TOTALS
    mTot = len(sRAPDUlstItem)
    m = 0
    while m < mTot:
          if m == 0:
             sPrint = sPrint + "\n"
          sPrint = sPrint + "File '" + csvFile + "' - FAILED - TOTAL RAPDU " + sRAPDUlstItem[m] + " : " + str(sRAPDUlstCount[m]) + "\n"
          m = m + 1 

    
    # GET DATETIME NOW
    dateEnd = datetime.now()    
    sdateEnd = dateEnd.strftime(sdtFormat)
    delta = dt_difference(sdtFormat, dateStart, dateEnd, False)
    sPrint = sPrint + "\n" + "Processed file '" + str(csvFile) + "' to '" + str(sFileOut) + "', finished: " + str(sdateEnd) + "\nElapsed: " + str(delta)

    sPrint = sPrint + "\n\n" + str_RepeatString(50, "-")
    
    #PRINT END
    print(sPrint)
    sPrint = sPrint + "\n"
    file2write=open(sFileOut,'a')
    file2write.write(sPrint)
    file2write.close()

    if sReturnSepara == "":
       sReturnSepara = "#"
       
    sReturn = csv_ReturnPrepare(sReturnSepara, False, str(n)) 
    sReturn = sReturn + csv_ReturnPrepare(sReturnSepara, True, str(nSUCCEEDED)) 
    sReturn = sReturn + csv_ReturnPrepare(sReturnSepara, True, str(nFAILED)) 
    sReturn = sReturn + csv_ReturnPrepare(sReturnSepara, True, str(nINPROCESS)) 
    sReturn = sReturn + csv_ReturnPrepare(sReturnSepara, True, str(nICCIDs)) 
    sReturn = sReturn + csv_ReturnPrepare(sReturnSepara, True, str(nCANCELED)) 
    
    #RAPDU TOTALS ADDED TO RETURN
    mTot = len(sRAPDUlstItem)
    if mTot == 0:
       sReturn = sReturn + csv_ReturnPrepare(sReturnSepara, True, "0") 
    else:
       m = 0
       while m < mTot:
             sReturn = sReturn + csv_ReturnPrepare(sReturnSepara, True, sRAPDUlstItem[m]) 
             sReturn = sReturn + csv_ReturnPrepare(sReturnSepara, True, str(sRAPDUlstCount[m])) 
             m = m + 1 
    
     
    return sReturn


#------------------------------------------------------------------------------------
# is_ICCID => check that value is an ICCID
#------------------------------------------------------------------------------------
def is_ICCID(sData):
    bReturn = False
    bProcess = False

    sICCID = str_SpacesOut(sData.upper())
    
    #REMOVING LAST F
    if str_right(sICCID,1) == "F":
       sICCID = str_left(sICCID, len(sICCID)-1)
    
    if len(sICCID) >= 18 and len(sICCID) <= 20:
       if str_nro0To9FromString(sICCID):
          bProcess = True
    
    return bProcess

#------------------------------------------------------------------------------------
# csv_ReturnPrepare => Prepare all data for return
#------------------------------------------------------------------------------------
def csv_ReturnPrepare(sReturnSepara, bAddSepara, nValue):
    sReturn = ""
    if bAddSepara:
       sReturn = sReturn + sReturnSepara
    sReturn = sReturn + str(nValue)
    return sReturn     


#------------------------------------------------------------------------------------
# csv_ReturnGet => Get data from return
#------------------------------------------------------------------------------------
def csv_ReturnGet(sReturnSepara, sReturnData, nReference):
    sReturn = ""
    
    sReturn = str_getSubStringFromOcur(sReturnData, sReturnSepara, nReference)
    if valid_nro_float(sReturn):
       return sReturn
    else:
       return ""

#------------------------------------------------------------------------------------
# csv_PreparingResults => Formatting results
#------------------------------------------------------------------------------------
def csv_PreparingResults(nNro, sSeparaMiles):
    if len(str(nNro)) > 0:
       sNro = str_RemoveFromNumberDecimals(nNro, ".")
       sNro = str_AddThousandToNumber(sNro, sSeparaMiles)
       return sNro
    else:
       return ""   
    
#------------------------------------------------------------------------------------
# csv_GetPattern => Getting pattern from a line
#------------------------------------------------------------------------------------
def csv_GetPattern(lst, sPattern, sSepara):
    
    sReturn = ""
    
    nLst = len(lst)
    #print("LST: " + str(lst) + " - Items: " + str(nLst))
    
    n = 0
    while n < nLst:
          sField = lst[n]
          if str_instrBool(sField, sPattern):
             sReturn = str_getSubStringFromOcur(sField, sPattern, 1)
             #print("Return: " + sReturn)
             #exit()
             return sReturn
          n = n + 1   
            
    return sReturn

#------------------------------------------------------------------------------------
# csv_GetICCID => Getting ICCID from a line
#------------------------------------------------------------------------------------
def csv_GetICCID(lst):
    
    sReturn = ""
    
    nLst = len(lst)
    #print("ICCID LST: " + str(lst) + " - Items: " + str(nLst))
    
    n = 0
    while n < nLst:
          sField = lst[n]
          if is_ICCID(sField):
             sReturn = sField
             #print("RETURN ICCID: " + sReturn)
             return sReturn
          n = n + 1   
            
    return sReturn

#------------------------------------------------------------------------------------
# csv_GetSTATUS => Getting STATUS from a line
#------------------------------------------------------------------------------------
def csv_GetSTATUS(lst, sStatusSUCCEDDED, sStatusFAILED, sStatusINPROGRESS, sStatusCANCELED):
    
    sReturn = ""
    
    nLst = len(lst)
    #print("STATUS LST: " + str(lst) + " - Items: " + str(nLst))
    
    n = 0
    while n < nLst:
          sField = lst[n]
          #print("STATUS FIELD: " + sField)
          sTemp = is_STATUS(sField, sStatusSUCCEDDED, sStatusFAILED, sStatusINPROGRESS, sStatusCANCELED)
          if sTemp != "":
             sReturn = sTemp
             #print("STATUS RETURN: " + sReturn)
             return sReturn
          n = n + 1   
            
    return sReturn
      
#------------------------------------------------------------------------------------
# is_STATUS => Getting STATUS from a line
#------------------------------------------------------------------------------------
def is_STATUS(sData, sStatusSUCCEDDED, sStatusFAILED, sStatusINPROGRESS, sStatusCANCELED):
    sStatus = str_SpacesOut(sData.upper())
    #print("IS_STATUS FIELD: " + sStatus)
    if sStatus == sStatusSUCCEDDED or sStatus == sStatusFAILED or sStatus == sStatusINPROGRESS or sStatus == sStatusCANCELED:
       return sStatus
    else:
       return ""
