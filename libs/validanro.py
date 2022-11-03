
def valid_nro(nro):
    
    isValidNro = True
    
    if nro is None:
       return False

    try:
        #val = int(userInput)
        isinstance(nro, (int, float))
    except ValueError:
        isValidNro = False    
    
    #print("NRO: " + str(nro) + " = RESULT: " + str(isValidNro))    
    
    return isValidNro

def valid_nro_param(nro, type):
    
    isValidNro = True
    
    if nro is None:
       return False

    try:
        #val = int(userInput)
        isinstance(nro, type)
    except ValueError:
        isValidNro = False    
    
    #print("NRO: " + str(nro) + ", TYPE: " + str(type) + " = RESULT: " + str(isValidNro))    
    return isValidNro
    

def valid_nro_int(nro):
    return valid_nro_param(nro, int)

def valid_nro_float(nro):
    return valid_nro_param(nro, float)

 