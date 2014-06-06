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

def randomBoolean(chance, case=None):
    if case==None:
        r = Random()
    else:    
        r = Random(case)
    b = r.nextFloat()<chance
    return b

def randomFirstName(case=None):
    if case==None:
        r = Random()
    else:    
        r = Random(case)
    firstNames = ["Alan", "Betty", "Carlos", "Denise", "Edward", "Felicity", "Graham", "Harriet", "Ivan", "Judith", "Keith", "Lucy", "Michael", "Nicola", "Owen", "Patsy", "Quentin", "Rosemary", "Stephen", "Tracey", "Ulrich", "Viola", "William"]
    return firstNames[r.nextInt(len(firstNames))]


def randomPostCode(case=None):
    if case==None:
        r = Random()
    else:    
        r = Random(case)
        
    postCodesA1 = ["E", "W", "N", "S", "SO", "GU", "PO", "NO", "BT"]        
    postCodeA1 = postCodesA1[r.nextInt(len(postCodesA1))]
    numeric1 = str(1+r.nextInt(25))
    numeric2 = str(1+r.nextInt(10))
    postCodesA2 = ["AB", "HJ", "GR", "OP", "GA", "NM", "GC", "DS", "AV"]        
    postCodeA2 = postCodesA2[r.nextInt(len(postCodesA2))]
    
    return postCodeA1+numeric1+" "+numeric2+postCodeA2
        

def randomName(case=None):
    return randomFirstName(case=case)+" "+randomLastName(case=case)

def randomLastName(case=None):
    if case==None:
        r = Random()
    else:    
        r = Random(case)
    lastNames = ["Anderson", "Baker", "Collins", "Delacruz", "Evans", "Forster", "Gardener", "Hoskins", "Iverson", "Jacoby", "Kelwell", "Lewis", "MacDonald", "Neville", "O'Malley", "Petersen", "Quinn", "Roberts", "Sullivan", "Thomas", "Ulverston", "Vickers", "Watson"]
    return lastNames[r.nextInt(len(lastNames))]

def resolveOneEvalSubstitution(string, case=0):
    if string.find("{=")<0:
        return string
    else:
        evalString = string[2+string.find("{="):]
        evalString = evalString[:evalString.find("}")]
        evalResult = eval(evalString)
        return string.replace("{="+evalString+"}",str(evalResult))
        
def resolveEvalSubstitutions(string, case=0):
    while string.find("{=")>=0:
        string = resolveOneEvalSubstitution(string, case=case)
    return string

def buildLinkCollection(collectionTag, memberTag, ids, format="xml"):
    if format=="xml":
        xml= "<"+collectionTag+">"
        for id in ids:
            xml += "<"+memberTag+">"
            xml += id
            xml += "</"+memberTag+">"
        xml += "</"+collectionTag+">"
        return xml
    elif format == "json":
        json = "\"users\": ["
        for id in ids:
            json += "\""+id+"\""+", "
        json = json[:-2]+"]"
        return json
    else:
        return str(ids)

def getTestData(fileStr, substitutions={}, case=0):
    file = open(fileStr, "r")
    lines = file.readlines()
    file.close
    result = ""
    for line in lines:
        result+=line
    for key in substitutions.keys():
        result=result.replace(key, substitutions[key])
    result = resolveEvalSubstitutions(result, case=case) 
    return result

