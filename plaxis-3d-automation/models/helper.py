def cleanOneValue(num):
    if num == None:
        return
    try:
        result = float(num)
    except ValueError:
        result = None
    return result

def cleanList(numList):
    if numList == None:
        return
    split = numList.split(",")
    result = [cleanOneValue(num) for num in split]
    return result

def extract_N_multiple(formula):
    '''
    This function extracts the multiple of N from the a string, i.e. 5N, 4000N, etc...
    '''
    N_multiple = float(formula.strip()[:-1]) #Strip whitespaces, and letter "N" to get the number
    return N_multiple

def extract_cu_multiple(formula):
    '''
    This function extracts the multiple of cu from the a string, i.e. 400cu, 333.3cu, etc...
    '''
    cu_multiple = float(formula.strip()[:-2]) #Strip whitespaces, and letter "cu" to get the number
    return cu_multiple
