import sys
import urllib
import HttpCall
reload(HttpCall)
import t_utils
reload(t_utils)

server = "http://localhost:8080/"

null = None;

def loadTemplate(case, name="", uid="", trace=0):
    contextExtension = ""
    if (uid!=""):
        contextExtension=uid
    if (name!=""):
        contextExtension="name/"+name
    if trace:
        print case
        print name
        print uid
    response = HttpCall.callHttpPOST(server, "objectology/templates/"+contextExtension, {"data":case}).strip()
    return response

def loadTemplateFromFile(definitionFile):
    testTemplate = t_utils.getTestData(definitionFile)
    print testTemplate
    template = eval(loadTemplate(testTemplate))
    templateId = template["id"]
    return templateId



def deleteTemplate(uid): 
    response = HttpCall.callHttpDELETE(server, "objectology/templates/"+uid, {}).strip()
    return response

def getTemplateByName(name): 
    response = HttpCall.callHttpGET(server, "objectology/templates/name/"+urllib.quote(name), {}).strip()
    return response

def getTemplateIdByName(name): 
    null = None
    template = getTemplateByName(name)
    attList = eval(template)
    return attList["id"]

def deleteTemplateByName(name): 
    response = HttpCall.callHttpDELETE(server, "objectology/templates/name/"+name, {}).strip()
    return response

def getTemplates():
    response = HttpCall.callHttpGET(server, "objectology/templates/", {}).strip()
    return response

def getId(object):
    attList = object
    return attList["id"]

def getIdFromJSON(objectStr):
    null = None
    attList = eval(objectStr)
    return attList["id"]

def getIdAndName(object, description="name"):
    attList =object
    return attList["id"], attList[description]
        
def getInstanceByProperty(instanceType, propertyName, value): 
    response = HttpCall.callHttpGET(server, "objectology/"+instanceType+"/query", {propertyName: value}).strip()
    return response

def getInstanceIdByProperty(instanceType, propertyName, value): 
    null = None
    template = getInstanceByProperty(instanceType, propertyName, value)
    attList = eval(template)[0]
    return attList["id"]


def getIdsFromObjects(objectsStr):
    uids = []
    null = None
    objects= eval(objectsStr)
    for object in objects:
        uids.append(getId(object))
    return uids
        
def getIdsFromIdResponse(responseStr):
    ids = []
    cleanResponse = responseStr.replace('{"id":','').replace('}','')
    ids= eval(cleanResponse)
    return ids
        
def getIdsAndNamesFromObjects(objectsStr, description="name"):
    uidsAndNames = []
    null = None
    objects= eval(objectsStr)
    for object in objects:
        uidsAndNames.append(getIdAndName(object, description=description))
    return uidsAndNames
        
def getTemplateIds():
    templates = getTemplates()
    return getIdsFromObjects(templates)

def getTemplateIdsAndNames():
    templates = getTemplates()
    return getIdsAndNamesFromObjects(templates)

def getInstanceIdsAndNames(instanceType, description="name"):
    objects = getInstances(instanceType)###
    return getIdsAndNamesFromObjects(objects, description=description)

def getInstanceIds(type):
    response = HttpCall.callHttpGET(server, "objectology/{type}/".replace("{type}", type), {"view":"identifier"}).strip()
    return getIdsFromIdResponse(response)

def getInstances(type):
    response = HttpCall.callHttpGET(server, "objectology/{type}/".replace("{type}", type), {}).strip()
    return response
        
def clearTemplates():
    uids = getTemplateIds()
    for uid in uids:
        deleteTemplate(uid)
        
def createInstance(instanceType, case):
    response = HttpCall.callHttpPOST(server, "objectology/"+instanceType+"/", {"data":case}).strip()
    return response
    
def deleteInstance(instanceType, uid): 
    response = HttpCall.callHttpDELETE(server, "objectology/"+instanceType+"/"+uid, {}).strip()
    return response

def clearInstances(instanceType):
    uids = getInstanceIds(instanceType)
    for uid in uids:
        try:
            deleteInstance(instanceType, uid)
        except:
            print "delete failed", uid

