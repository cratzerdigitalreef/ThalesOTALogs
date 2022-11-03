CSVProcessPython_ThalesOTALogs:
-------------------------------

IMPORTANT:
----------
For any doubt, call me or send me an email:
carlos.ratzer@gmail.com


Steps:
------

1) Install Python.
Install Python. One suggested version is 3.10.5.
https://www.python.org/downloads/

2) Copy all "*.csv" files from Thales OTA to one directory in your PC.

3) Prepare .bat file in Windows:
File: 
csvprocThalesOTALogs.bat

Example:
REM ******************************************************************
REM csvprocThalesOTALogs.py: Parameters
REM 1. Process Description. Example: "Argentina"
REM 2. Path/pattern for csv files. Example: "D:\GoogleDrive\My Drive\Public\Desar\Python\CSVProcessPython_ThalesOTALogs\*.csv"
REM 3. CSV separator. Example: ","
REM 4. Output file Prefix. Example: "out"
REM 5. Miles separator. Example: "."

python csvprocThalesOTALogs.py "Argentina" "D:\GoogleDrive\My Drive\Public\Desar\Python\CSVProcessPython_ThalesOTALogs\*.csv" "," "out" "."

4) Execute file .bat
csvprocThalesOTALogs.bat

5) Check output.
In the example, the output is:
"out_yyyyMMdd_hhmmss"
where:
yyyy = year
MM = month
dd = day
hh = hour
mm = minute
ss = second

it is generated one file per execution.



