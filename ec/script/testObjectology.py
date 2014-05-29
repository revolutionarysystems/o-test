import sys
import urllib

import setPath
reload(setPath)
import o_utils
reload(o_utils)
import t_utils
reload(t_utils)

from java.io import File
from java.util import Date

def createProductInstance(productTemplateId, accountTemplateId, definition):
    testInstance = t_utils.getTestData(definition, substitutions = {"{templateId}":productTemplateId, "{accountTemplateId}":accountTemplateId})
    return o_utils.createInstance("product", testInstance)            
    
def createUserInstance(userTemplateId, definition):
    testInstance = t_utils.getTestData(definition, substitutions = {"{templateId}":userTemplateId})
    return o_utils.createInstance("user", testInstance)            
    
def createSubscriptionInstance(subscriptionTemplateId, userTemplateId, productId, userId, shortCode, definition):
    testInstance = t_utils.getTestData(definition, substitutions = {"{templateId}":subscriptionTemplateId,"{userTemplateId}":userTemplateId,"{productId}":productId,"{userId}":userId,"{shortCode}":shortCode})
    return o_utils.createInstance("subscription", testInstance)            

def createAccountInstance(accountTemplateId, userTemplateId, productId, userId, shortCode, definition):
    testInstance = t_utils.getTestData(definition, substitutions = {"{templateId}":accountTemplateId,"{userTemplateId}":userTemplateId,"{productId}":productId,"{userId}":userId,"{shortCode}":shortCode})
    return o_utils.createInstance("account", testInstance)            

def show(list, type):
    for item in list:
        print "http://localhost:8080/objectology/"+type+"/"+item[0], " - ", item[1]

def showId(list, type):
    for item in list:
        print "http://localhost:8080/objectology/"+type+"/"+item

def catalog(type):
    if type == "templates":
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
    catalog("templates")
    catalog("product")
    catalog("account")
    catalog("subscription")
    catalog("user")

def idCatalogs():
    catalog("templates")
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
    o_utils.loadTemplateFromFile("../xml-models/userTemplate.xml")
    o_utils.loadTemplateFromFile("../xml-models/echoCentralAccountTemplate.xml")
    #o_utils.loadTemplateFromFile("../xml-models/subscriptionTemplate.xml")
    o_utils.loadTemplateFromFile("../xml-models/productTemplate.xml")



def simpleDataSet():
    #Build Sample Data from scratch

    print Date()
    clearData()
    loadTemplates()

    productTemplateId = o_utils.getTemplateIdByName("EC Product Template")
    #subscriptionTemplateId = o_utils.getTemplateIdByName("echoCHECK Subscription Template")
    accountTemplateId = o_utils.getTemplateIdByName("echoCentral Account Template")
    userTemplateId = o_utils.getTemplateIdByName("echoCentral User Template")

    createProductInstance(productTemplateId, accountTemplateId,"../xml-models/echoCHECKProduct.xml")
    shortCode="eCKB"
    productId = o_utils.getInstanceIdByProperty("product", "shortCode", shortCode)

    print Date()
    for i in range(25):
        userId = o_utils.getIdFromJSON(createUserInstance(userTemplateId,"../xml-models/userInstance.xml"))
        createAccountInstance(accountTemplateId, userTemplateId, productId, userId, shortCode, "../xml-models/accountInstance.xml")

    print Date()
    catalogs()
    #idCatalogs()
    print Date()



#simpleDataSet()    
loadTemplates()
idCatalogs()