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
    template = eval(loadTemplate(testTemplate))
    templateUid = template["id"]
    return templateUid



def deleteTemplate(uid): 
    response = HttpCall.callHttpDELETE(server, "objectology/templates/"+uid, {}).strip()
    return response

def getTemplateByName(name): 
    response = HttpCall.callHttpGET(server, "objectology/templates/name/"+urllib.quote(name), {}).strip()
    return response

def getTemplateUidByName(name): 
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

def getUid(object):
    attList = object
    return attList["id"]

def getUidAndName(object, description="name"):
    attList =object
    return attList["id"], attList[description]
        
def getInstanceByProperty(instanceType, propertyName, value): 
    response = HttpCall.callHttpGET(server, "objectology/"+instanceType+"/"+propertyName+"/"+urllib.quote(value), {}).strip()
    return response

def getInstanceUidByProperty(instanceType, propertyName, value): 
    null = None
    template = getInstanceByProperty(instanceType, propertyName, value)
    attList = eval(template)
    return attList["id"]


def getUidsFromObjects(objectsStr):
    uids = []
    null = None
    objects= eval(objectsStr)
    for object in objects:
        uids.append(getUid(object))
    return uids
        
def getUidsAndNamesFromObjects(objectsStr, description="name"):
    uidsAndNames = []
    null = None
    objects= eval(objectsStr)
    for object in objects:
        uidsAndNames.append(getUidAndName(object, description=description))
    return uidsAndNames
        
def getTemplateUids():
    templates = getTemplates()
    return getUidsFromObjects(templates)

def getTemplateUidsAndNames():
    templates = getTemplates()
    return getUidsAndNamesFromObjects(templates)

def getInstanceUidsAndNames(instanceType, description="name"):
    objects = getInstances(instanceType)###
    return getUidsAndNamesFromObjects(objects, description=description)


def getInstanceUids(type):
    instances = getInstances(type)
    return getUidsFromObjects(instances)

def getInstances(type):
    response = HttpCall.callHttpGET(server, "objectology/{type}/".replace("{type}", type), {}).strip()
    return response
        
def clearTemplates():
    uids = getTemplateUids()
    for uid in uids:
        deleteTemplate(uid)
        
def createInstance(case):
    response = HttpCall.callHttpPOST(server, "objectology/subscription/", {"data":case}).strip()
    return response
    
def deleteInstance(instanceType, uid): 
    response = HttpCall.callHttpDELETE(server, "objectology/"+instanceType+"/"+uid, {}).strip()
    return response

def clearInstances(instanceType):
    uids = getInstanceUids(instanceType)
    for uid in uids:
        try:
            deleteInstance(instanceType, uid)
        except:
            print "delete failed", uid

