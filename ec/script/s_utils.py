import sys
import urllib

import setPath
reload(setPath)
import o_utils
reload(o_utils)
import t_utils
reload(t_utils)

from java.io import File
from java.io import FileNotFoundException
from java.util import Date

def createProductInstance(productTemplateId, accountTemplateId, definition, contentType="text/xml"):
    testData = t_utils.getTestData(definition, substitutions = {"{templateId}":productTemplateId, "{accountTemplateId}":accountTemplateId})
    return o_utils.createInstance("product", testData, contentType=contentType)            
    
def createUserInstance(userTemplateId, accountId, definition, case=None, contentType="text/xml"):
    testData = t_utils.getTestData(definition, substitutions = {"{templateId}":userTemplateId, "{accountId}": accountId}, case=case)
    return o_utils.createInstance("user", testData, contentType=contentType)            
    
def createSubscriptionInstance(subscriptionTemplateId, userTemplateId, productId, userId, shortCode, definition):
    testData = t_utils.getTestData(definition, substitutions = {"{templateId}":subscriptionTemplateId,"{userTemplateId}":userTemplateId,"{productId}":productId,"{userId}":userId,"{shortCode}":shortCode})
    return o_utils.createInstance("subscription", testData)            

def createAccountInstance(accountTemplateId, userTemplateId, productId, subProductId1, subProductId2, userId, shortCode, definition, case=0, contentType="text/xml"):
    testData = t_utils.getTestData(definition, substitutions = {"{templateId}":accountTemplateId,"{userTemplateId}":userTemplateId,"{productId}":productId,"{eCntProductId}":subProductId1,"{eCKProductId}":subProductId2,"{userId}":userId,"{shortCode}":shortCode}, case=case)
    #print testData
    return o_utils.createInstance("account", testData, contentType=contentType)            

def addAccountUser(accountId, userId, definition, case=0, contentType="text/xml"):
    testData = t_utils.getTestData(definition, substitutions = {"{userId}":userId}, case=case)
    return o_utils.applyDelta("account/"+accountId, testData, contentType=contentType)            

def setAccountMainUser(accountId, userId, definition, case=0, contentType="text/xml"):
    testData = t_utils.getTestData(definition, substitutions = {"{userId}":userId}, case=case)
    return o_utils.applyDelta("account/"+accountId, testData, contentType=contentType)            

def updateAccount(accountId, definition, substitutions= {}, case=0, contentType="text/xml"):
    testData = t_utils.getTestData(definition, substitutions = substitutions, case=case)
    return o_utils.applyDelta("account/"+accountId, testData, contentType=contentType)            

def updateUser(accountId, definition, case=0, contentType="text/xml"):
    testData = t_utils.getTestData(definition, substitutions = {}, case=case)
    return o_utils.applyDelta("user/"+accountId, testData, contentType=contentType)            

def setStatus(type, objectId, status, definition, case=0):
    testData = t_utils.getTestData(definition, substitutions = {"{status}":status}, case=case)
    return o_utils.applyDelta(type+"/"+objectId, testData)            

def queryInstance(type, definition, substitutions = {}, case=0):
    testData = t_utils.getTestData(definition, substitutions = substitutions, case=case)
    print testData
    return o_utils.makeQuery(type, testData)            
    

def show(list, type):
    for item in list:
        print "http://localhost:8080/objectology/"+type+"/"+item[0], " - ", item[1]

def showId(list, type):
    for item in list:
        print "http://localhost:8080/objectology/"+type+"/"+item

def showLink(id, type):
    print "http://localhost:8080/objectology/"+type+id

def catalog(type):
    if type == "template":
        print "Templates"
        show(o_utils.getTemplateIdsAndNames(), type)   
    elif type == "product":
        print "Products"
        show(o_utils.getInstanceIdsAndNames("product", description="title"), type)
    elif type == "account":
        print "Accounts"
        show(o_utils.getInstanceIdsAndNames("account", description="accountNumber"), type)
    elif type == "subscription":
        print "Subscriptions"
        show(o_utils.getInstanceIdsAndNames("subscription", description="accountNumber"), type)
    elif type == "user":
        print "Users"
        show(o_utils.getInstanceIdsAndNames("user", description="name"), type)
       
    print "-----"

def idCatalog(type):
    if type == "templates":
        print "Templates"
        show(o_utils.getTemplateIdsAndNames(), type)   
    else:
        print type+"(s)"
        showId(o_utils.getInstanceIds(type), type)
    print "-----"

def catalogs():
    catalog("template")
    catalog("product")
    catalog("account")
    catalog("subscription")
    catalog("user")

def idCatalogs():
    catalog("template")
    idCatalog("product")
    idCatalog("account")
    idCatalog("subscription")
    idCatalog("user")

def clearData():    
    o_utils.clearInstances("user")
    o_utils.clearInstances("account")
    o_utils.clearInstances("subscription")
    o_utils.clearInstances("product")
    o_utils.clearTemplates()


def loadTemplates():
    o_utils.loadTemplateFromFile("../xml/templates/userTemplate.xml")
    o_utils.loadTemplateFromFile("../xml/templates/echoCentralAccountTemplate.xml")
    #o_utils.loadTemplateFromFile("../xml/templates/subscriptionTemplate.xml")
    o_utils.loadTemplateFromFile("../xml/templates/productTemplate.xml")



