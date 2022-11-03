# -*- coding: UTF-8 -*-
import sys
global str

from validanro import *

# str_ExitEjecution ----------------------------------------------------------------------------------------------------------------------
def str_ExitEjecution():
    exit(0)
    
# str_instr ----------------------------------------------------------------------------------------------------------------------
def str_instr(str, pattern):
    
    index = -1

    if str is None:
       return index
    if pattern is None:
       return index

    if pattern in str:
       index = str.find(pattern)
   
    return index

# str_instrBool ----------------------------------------------------------------------------------------------------------------------
def str_instrBool(str, pattern):
    
    isInSTR = True
    
    if str_instr(str,pattern) <= -1:
       isInSTR = False

    return isInSTR

# str_getSubStringFrom ----------------------------------------------------------------------------------------------------------------------
def str_getSubStringFrom(str, pattern):
    index = str_instr(str, pattern)
    if index >= 0:
        return str[index+1:]
    return str

# str_getSubStringTo ----------------------------------------------------------------------------------------------------------------------
def str_getSubStringTo(st, pattern):
    index = str_instr(st, pattern)
    if index >= 0:
        return st[0:index]
    return st
        
# str_getSubString ----------------------------------------------------------------------------------------------------------------------
def str_getSubString(st, patternFrom, patterTo):
     #print("STRING: " + st)
     #print("PATTERN FROM: " + patternFrom)
     #print("PATTERN TO: " + patterTo)
     
     stemp1 = str_getSubStringFrom(st, patternFrom)
     #print("AFTER PATTERN FROM: " + stemp1)
     sreturn = str_getSubStringTo(stemp1, patterTo)
     #print("RETURN: " + sreturn)
     
     return sreturn
     
     
# str_mid ----------------------------------------------------------------------------------------------------------------------
def str_mid(st, nFrom, nLen):
#s = s[ beginning : beginning + LENGTH]
     if st is None:
        return st

     if nFrom is None:
        nFrom = 0
     if nLen is None:
        return st
        
# start: The starting index of the substring. The character at this index is included in the substring. If start is not included, it is assumed to equal to 0.
# end: The terminating index of the substring. The character at this index is not included in the substring. If end is not included, or if the specified value exceeds the string length, it is assumed to be equal to the length of the string by default.
     
     nFrom = int(nFrom)
     nLen = int(nLen)
     #print("nFrom: " + str(nFrom) + ". nLen: " + str(nLen))
     
     return st[nFrom: nFrom + nLen]

# str_left ----------------------------------------------------------------------------------------------------------------------
def str_left(st, ln):
     if st is None:
        return st

     if ln > 0:
        return st[:ln] 
     else:
        return st       

# str_midToEnd ----------------------------------------------------------------------------------------------------------------------
def str_midToEnd(st, nFrom):
     if st is None:
        return st

     return st[nFrom:] 
    

# str_right ----------------------------------------------------------------------------------------------------------------------
def str_right(st, ln):
     if st is None:
        return st

     n=int(len(st) - ln)
     if n > 0:
        return st[n:] 
     else:
        return st       

     
# str_reverse ----------------------------------------------------------------------------------------------------------------------
def str_reverse(data):
    datarev = ""
    n=0
    while n < len(data):
          l=data[n:n+1]
          r=data[n+1:n+2]
          datarev+=r+l
          n+=2
         
    return datarev


# str_getSubStringFromOcurFirst ----------------------------------------------------------------------------------------------------------------------
def str_getSubStringFromOcurFirst(st, pattern):
    return str_getSubStringFromOcur(st, pattern, 0)

# str_getSubStringFromOcurLast ----------------------------------------------------------------------------------------------------------------------
def str_getSubStringFromOcurLast(st, pattern):
    return str_getSubStringFromOcur(st, pattern, -1)
    
# str_getSubStringFromOcur ----------------------------------------------------------------------------------------------------------------------
def str_getSubStringFromOcur(st, pattern, ocur):
    
    nPatterns = str_CountPattern(st, pattern)
    #print("str_getSubStringFromOcur: For String '" + st + "', amount of pattern '" + pattern + "': " + str(nPatterns) + ", ocur=" + str(ocur))

    nLen = len(st)
    nLenPat = len(pattern)
    #print("str_getSubStringFromOcur. Len st '" + st + "': " + str(nLen))
    #print("str_getSubStringFromOcur. Len pattern '" + pattern + "': " + str(nLenPat))
    
    out = ""
    n = 0
    i = 0
    j = i
    s = ""
    while i < nLen:
          s = st[i:i+nLenPat]
          if len(s)<nLenPat:
             s=st[i-1:]
             out=out[:len(out)-1]
             
          #print("str_getSubStringFromOcur. Check " + str(i) + " : " + s)
          if s==pattern:
             if n==ocur:
                #print("str_getSubStringFromOcur. Out: " + out + ", ocur=" + str(ocur))
                return out
             else:
                #print("str_getSubStringFromOcur. Out " + str(n) + " : " + out + ", ocur=" + str(ocur))
                out = ""
                i=i+nLenPat-1
                j=i+1   
             
             n = n + 1
             
          else:
             out=st[j:i+nLenPat]
             #print("str_getSubStringFromOcur. Out " + str(i) + " : " + out)
          #i = i+nLenPat
          i = i+1
    
    if ocur==-1 or n==ocur:
       return out
    else:
       return ""
       

# str_CountPattern ----------------------------------------------------------------------------------------------------------------------
def str_CountPattern(st, pattern):
    n = 0
    nLen = len(st)
    nLenPat = len(pattern)
    #print("str_CountPattern. Len st '" + st + "': " + str(nLen))
    #print("str_CountPattern. Len pattern '" + pattern + "': " + str(nLenPat))
    
    i = 0
    while i < nLen:
          s = st[i:i+nLenPat]
          #print("str_CountPattern. Check: " + s)
          if s==pattern:
             n = n + 1
          i = i+1
           
    #print("str_CountPattern. For String '" + st + "', count of pattern '" + pattern + "': " + str(n))
    return n           


# str_getListFromStringPattern ----------------------------------------------------------------------------------------------------------------------
def str_getListFromStringPattern(st, pattern):
    out = []
    
    nPatterns = str_CountPattern(st, pattern)
    print("str_getListFromStringPattern: For String '" + st + "', amount of pattern '" + pattern + "': " + str(nPatterns))
    
    n=0
    while n <= nPatterns:
          t = str_getSubStringFromOcur(st,pattern,n)
          print("str_getListFromStringPattern: " + t)
          if t!="":
             out.append(t)
          n=n+1 
          
    print("str_getListFromStringPattern: Result=" + str(out))        
    return out

# str_RemoveLastPattern ----------------------------------------------------------------------------------------------------------------------
def str_RemoveLastPattern(st, pattern):
    nlenst = len(st)
    nlenpattern = len(pattern)
    out=st
    if st[nlenst-nlenpattern:]==pattern:
       out = st[:nlenst-nlenpattern]
    return out

# str_RemoveFirstPattern ----------------------------------------------------------------------------------------------------------------------
def str_RemoveFirstPattern(st, pattern):
    nlenst = len(st)
    nlenpattern = len(pattern)
    out=st
    if st[:nlenpattern]==pattern:
       out = st[nlenpattern:]
    return out

# str_RemoveItemFromPatternList ----------------------------------------------------------------------------------------------------------------------
def str_RemoveItemFromPatternList(st, pattern, nItem, bTransformToStr):
    outret = []
    out = str_getListFromStringPattern(st, pattern)
    print(out)
    n = 0
    for i in out:
        if n!=nItem:
           outret.append(i)
        n = n +1   
    
    if nItem==-1:
       del outret[-1]

    print(outret)       
    
    if bTransformToStr:
       out = ""
       for i in outret:
           out = out + i + pattern
       out = str_RemoveLastPattern(out, pattern)    
       return out
    else:   
       return outret

# str_ReplaceComillaDobleOld ----------------------------------------------------------------------------------------------------------------------
def str_ReplaceComillaDobleOld(st, new):
    # decimal 34 = "
    # https://ascii.cl/
    return str_Replace(st, chr(34), new)

# str_ReplaceComillaDobleNew ----------------------------------------------------------------------------------------------------------------------
def str_ReplaceComillaDobleNew(st, old):
    # decimal 34 = "
    # https://ascii.cl/
    return str_Replace(st, old, chr(34))
    
# str_Replace ----------------------------------------------------------------------------------------------------------------------
def str_Replace(st, old, new):
    out=""
    for i in st:
        if i==old:
           out = out + new
        else:
           out = out + i
    return out

# str_TrimCleanSpaces ----------------------------------------------------------------------------------------------------------------------
def str_TrimCleanSpaces(st):
    return str_CleanPattern(st, " ")

# str_SpacesOut ----------------------------------------------------------------------------------------------------------------------
def str_SpacesOut(st):
    return str_CleanPattern(st, " ")

# str_CleanPattern ----------------------------------------------------------------------------------------------------------------------
def str_CleanPattern(st, sPattern):
    if st == "" or len(st)==0:
       return st
    out=""
    nLen = len(st)
    nLenPat = len(sPattern)
    i = 0
    s = ""
    while i < nLen:
          s = st[i:i+nLenPat]
          if len(s)<nLenPat:
             s=st[i-1:]
             out=out[:len(out)-1]
             
          if not s==sPattern:
             out=out+st[i:i+nLenPat]
             #print("str_CleanPattern. Out: " + out)
          i = i+nLenPat
    
    return out
          
# str_StringToList ----------------------------------------------------------------------------------------------------------------------
def str_StringToList(st, delimiter):
    li = list(st.split(delimiter))
    return li
    
# str_ListToString ----------------------------------------------------------------------------------------------------------------------
def str_ListToString(lst):
    return ''.join(lst)
    
# str_ListToStringWithSeparator ----------------------------------------------------------------------------------------------------------------------
def str_ListToStringWithSeparator(lst, ssep):
    out=""
    for i in lst:
        out = out + i + ssep
    out = str_RemoveLastPattern(out, ssep)    
    return out
     
# str_AddSpaceHexa ----------------------------------------------------------------------------------------------------------------------
def str_AddSpaceHexa(sstr):
    nTogether = 2
    sstr = str(sstr)
    if sstr[:2].upper() == "0X":
       nTogether = 4
    
    sOut = str_AddCharToString(sstr, nTogether, " ")
    return sOut

# str_SpaceHexa ----------------------------------------------------------------------------------------------------------------------
def str_SpaceHexa(sstr):
    sstr =str_SpacesOut(sstr)
    return str_AddSpaceHexa(sstr)

# str_AddCharToString ----------------------------------------------------------------------------------------------------------------------
def str_AddCharToString(sstr, nTogether, sChar):
    if nTogether <= 0:
       return sstr
    
    sstr = str_TrimCleanSpaces(sstr)
    #print("str_AddCharToString: sstr = " + sstr)
        
    nLen = len(sstr)
    sOut = ""
    n = 0
    while n < nLen:
          if (n % nTogether) == 0:
             if n > 0:
                sOut = sOut + sChar
          sOut = sOut + sstr[n:n+1]      
          #print("str_AddCharToString: " + sOut)
          n = n + 1
    
    return sOut      

# str_formatNro ----------------------------------------------------------------------------------------------------------------------
def str_formatNro(nNro, nPaddingLeft):
    sNro = ("{:0>" + str(nPaddingLeft) + "}").format(nNro)
    return sNro
    
# str_RepeatString ----------------------------------------------------------------------------------------------------------------------
def str_RepeatString(nNro, sChar):
    sReturn = ""
    if nNro > 0 and sChar != "":
       n = 0
       while n < nNro:
             sReturn = sReturn + sChar
             n = n + 1
             
    return sReturn
  
# str_StringToNumberFloat ----------------------------------------------------------------------------------------------------------------------
def str_StringToNumberFloat(sIn):
    nReturn = 0
    if sIn != "" and valid_nro(sIn):
       nReturn = float(sIn)         
    return nReturn
   
# str_StringToNumberInt ----------------------------------------------------------------------------------------------------------------------
def str_StringToNumberInt(sIn):
    nReturn = 0
    if sIn != "" and valid_nro(sIn):
       nReturn = int(sIn)         
    return nReturn
  
# str_GetComillaDoble ----------------------------------------------------------------------------------------------------------------------
def str_GetComillaDoble():
    return chr(34)    
    
# str_GetComillaItalic ----------------------------------------------------------------------------------------------------------------------
def str_GetComillaItalic():
    return chr(44)    

# str_GetENTER ----------------------------------------------------------------------------------------------------------------------
def str_GetENTER():
    return chr(13) + chr(10)    

# str_AddThousandToNumber ----------------------------------------------------------------------------------------------------------------------
def str_AddThousandToNumber(sNro, sSepara):

    sNro = str_SpacesOut(sNro)
    
    #FOR THOSE CASES WHERE IT IS, FOR EXAMPLE, IN FLOAT 12345.0, REMOVING THE FLOAT PART
    sNro = str_RemoveFromNumberDecimals(sNro, sSepara)
    
    nMod = 3
    
    sSepara = str_SpacesOut(sSepara)
    if sSepara == "":
       sSepara = "."

    #print("Nro: " + sNro + ", Separator: " + sSepara)
       
    sOut = ""
    nMax = len(sNro)
    n = 0
    while nMax >= 0:
          sChr = str_mid(sNro, nMax, 1)

          if n >= nMod:
             sChr = sChr + sSepara
             n = 0          
          n = n + 1
       
          sOut = sOut + sChr
          nMax = nMax - 1
    
    #print("Out to reverse: " + sOut)
    
    sOut = str_reverseAll(sOut)      
    
    if sOut[:1] == sSepara:
       sOut = sOut[1:]
       
    #print("Out reversed: " + sOut)
    
    return sOut

 
# str_reverseAll ----------------------------------------------------------------------------------------------------------------------
def str_reverseAll(data):
    sOut = ""
    nMax = len(data)
    n = 0
    while nMax >= 0:
          sChr = str_mid(data, nMax, 1)
          sOut = sOut + sChr
          nMax = nMax - 1

    return sOut

# str_RemoveFromNumberDecimals ----------------------------------------------------------------------------------------------------------------------
def str_RemoveFromNumberDecimals(sNro, sSeparaComa):

    #print("sNro: " + str(sNro) + ", sSeparaComa: " + str(sSeparaComa))
    sNro = str_SpacesOut(str(sNro))
    
    if str_instrBool(sNro, sSeparaComa):
       sNro = str_getSubStringFromOcurFirst(sNro, sSeparaComa)
       
    return sNro
    
    
  