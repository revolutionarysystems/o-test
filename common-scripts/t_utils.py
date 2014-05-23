import sys
from java.util import Random

#=========TEST UTILS===========



def randomInt(n, case=None):
    if case==None:
        r = Random()
    else:    
        r = Random(case)
    i = r.nextInt(n)
    return i

def randomFirstName(case=None):
    if case==None:
        r = Random()
    else:    
        r = Random(case)
    firstNames = ["Alan", "Betty", "Carlos", "Denise", "Edward", "Felicity", "Graham", "Harriet", "Ivan", "Judith", "Keith", "Lucy", "Michael", "Nicola", "Owen", "Patsy", "Quentin", "Rosemary", "Stephen", "Tracey", "Ulrich", "Viola", "William"]
    return firstNames[r.nextInt(len(firstNames))]

def randomName(case=None):
    return randomFirstName(case=case)+" "+randomLastName(case=case)

def randomLastName(case=None):
    if case==None:
        r = Random()
    else:    
        r = Random(case)
    lastNames = ["Anderson", "Baker", "Collins", "Delacruz", "Evans", "Forster", "Gardener", "Hoskins", "Iverson", "Jacoby", "Kelwell", "Lewis", "MacDonald", "Neville", "O'Malley", "Petersen", "Quinn", "Roberts", "Sullivan", "Thomas", "Ulverston", "Vickers", "Watson"]
    return lastNames[r.nextInt(len(lastNames))]

def resolveOneEvalSubstitution(string):
    if string.find("{=")<0:
        return string
    else:
        evalString = string[2+string.find("{="):]
        evalString = evalString[:evalString.find("}")]
        evalResult = eval(evalString)
        return string.replace("{="+evalString+"}",str(evalResult))
        
def resolveEvalSubstitutions(string):
    while string.find("{=")>=0:
        string = resolveOneEvalSubstitution(string)
    return string



def getTestData(fileStr, substitutions={}):
    file = open(fileStr, "r")
    lines = file.readlines()
    file.close
    result = ""
    for line in lines:
        result+=line
    for key in substitutions.keys():
        result=result.replace(key, substitutions[key])
    result = resolveEvalSubstitutions(result)  
    return result

