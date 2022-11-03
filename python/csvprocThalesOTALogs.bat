REM ******************************************************************
REM csvprocThalesOTALogs.py: Parameters
REM 1. Process Description. Example: "ClaroArgentina"
REM 2. Path/pattern for csv files. Example: "D:\Carlos\DigitalReef\Projects\COTA\Python\CSVProcessPython_ThalesOTALogs\*.csv"
REM 3. CSV separator. Example: ","
REM 4. Output file Prefix. Example: "out"
REM 5. Miles separator. Example: "."

python csvprocThalesOTALogs.py "ClaroArgentina" "D:\Carlos\DigitalReef\Projects\COTA\Python\CSVProcessPython_ThalesOTALogs\*.csv" "," "out" "."
python csvprocThalesOTALogs.py "ClaroArgentina" "D:\Carlos\DigitalReef\Projects\COTA\Python\CSVProcessPython_ThalesOTALogs_v2\*.lst" ";" "out" "."

pause