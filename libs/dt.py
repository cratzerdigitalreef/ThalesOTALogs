from datetime import datetime
from datetime import timedelta

def dt_now(sFormat):
    if str(sFormat)=="":
       sFormat = "%d/%m/%Y-%H:%M:%S"
    
    dateStart = datetime.now()    
    return dateStart.strftime(sFormat)
    
def dt_difference_sec(dtStart, dtEnd):
    dt = dtStart - dtEnd
    return str(dt.total_seconds())

def dt_difference(sdtFormat, dtStart, dtEnd, bReturnCompleteMsg):
    #print("Start: " + str(dtStart))
    #print("End: " + str(dtEnd))
    
    #sFormatDT = "%d/%m/%Y-%H:%M:%S"
    #sFormatDT = "%Y%m%d%H%M%S"
    dtStart = datetime.strptime(str(dtStart),sdtFormat)
    dtEnd = datetime.strptime(str(dtEnd),sdtFormat)
    
    dt = dtEnd - dtStart
    
    sec = int(dt.total_seconds())
    nmin = int(sec//60)
    nhor = int(sec//3600)
    nday = int(nhor//24)
    
    #print("sec: " + str(sec))
    #print("min: " + str(nmin))
    #print("hor: " + str(nhor))
    #print("day: " + str(nday))
    
    if nhor > 24:
       nhor_rest = int(nhor & 24)
    else:
       nhor_rest = nhor
    if nmin > 60:      
       nmin_rest = int(nmin & 60)
    else:
       nmin_rest = nmin
    if sec > 60:      
       nsec_rest = int(sec & 60)
    else:
       nsec_rest = sec
       
    #print("sec rest: " + str(nsec_rest))
    #print("min rest: " + str(nmin_rest))
    #print("hor rest: " + str(nhor_rest))
    
    sdtStart = dtStart.strftime(sdtFormat)
    sdtEnd = dtEnd.strftime(sdtFormat)
    
    sRet = ""
    if bReturnCompleteMsg:
       sRet = "Difference between - Start: " + str(sdtStart) + " - End: " + str(sdtEnd) + "\n"
       #print(sRet)
       #sRet = sRet + "Elapsed: " + str(sday) + " days, " + str(shor) + " hours, " + str(smin) + " minutes, " + str(sec) + " seconds."
       sRet = sRet + "Elapsed: "
       
    sRet = sRet + str(nday) + " days, " + str(nhor_rest) + " hours, " + str(nmin_rest) + " minutes, " + str(nsec_rest) + " seconds."
    
    #dt_difference(sdtFormat, "2022/08/17-22:28:52", "2022/08/18-06:35:06", False)

    print(sRet)
    
    return sRet
    
