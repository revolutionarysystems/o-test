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
