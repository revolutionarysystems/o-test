import sys
import urllib

import setPath
reload(setPath)
import o_utils
reload(o_utils)

from java.io import File

def createProductInstance(productTemplateUid, subscriptionTemplateUid, definition):
    testInstance = o_utils.getTestData(definition, substitutions = {"{templateUid}":productTemplateUid, "{subscriptionTemplateUid}":subscriptionTemplateUid})
    return o_utils.createInstance(testInstance)            
    
def createUserInstance(userTemplateUid, definition):
    testInstance = o_utils.getTestData(definition, substitutions = {"{templateUid}":userTemplateUid})
    return o_utils.createInstance(testInstance)            
    
def createSubscriptionInstance(subscriptionTemplateUid, userTemplateUid, productUid, userUid, definition):
    testInstance = o_utils.getTestData(definition, substitutions = {"{templateUid}":subscriptionTemplateUid,"{userTemplateUid}":userTemplateUid,"{productUid}":productUid,"{userUid}":userUid})
    return o_utils.createInstance(testInstance)            

def show(list, type):
    for item in list:
        print "http://localhost:8080/objectology/"+type+"/"+item[0], " - ", item[1]

def catalog(type):
    if type == "templates":
        print "Templates"
        show(o_utils.getTemplateUidsAndNames(), type)   
    elif type == "product":
        print "Products"
        show(o_utils.getInstanceUidsAndNames("product", description="title"), type)
    elif type == "subscription":
        print "Subscriptions"
        show(o_utils.getInstanceUidsAndNames("subscription", description="title"), type)
    elif type == "user":
        print "Users"
        show(o_utils.getInstanceUidsAndNames("user", description="name"), type)
       
    print "-----"

def catalogs():
    catalog("templates")
    catalog("product")
    catalog("subscription")
    catalog("user")

def clearData():    
    o_utils.clearInstances("user")
    o_utils.clearInstances("subscription")
    o_utils.clearInstances("product")
    o_utils.clearTemplates()


def loadTemplates():
    o_utils.loadTemplateFromFile("../xml-models/userTemplate.xml")
    o_utils.loadTemplateFromFile("../xml-models/subscriptionTemplate.xml")
    o_utils.loadTemplateFromFile("../xml-models/productTemplate.xml")




#Build Sample Data from scratch

clearData()
loadTemplates()

productTemplateUid = o_utils.getTemplateUidByName("EC Product Template")
subscriptionTemplateUid = o_utils.getTemplateUidByName("echoCHECK Subscription Template")
userTemplateUid = o_utils.getTemplateUidByName("echoCentral User Template")

createProductInstance(productTemplateUid, subscriptionTemplateUid,"../xml-models/echoCHECKProduct.xml")
productUid = o_utils.getInstanceUidByProperty("product", "shortCode", "eCKB")

createUserInstance(userTemplateUid,"../xml-models/userAInstance.xml")    
userUidA = o_utils.getInstanceUidByProperty("user", "name", "Alice Anderson")

createSubscriptionInstance(subscriptionTemplateUid, userTemplateUid, productUid, userUidA, "../xml-models/subscriptionAInstance.xml")

createUserInstance(userTemplateUid,"../xml-models/userBInstance.xml")    
userUidB = o_utils.getInstanceUidByProperty("user", "name", "Bernard Bates")

createSubscriptionInstance(subscriptionTemplateUid, userTemplateUid, productUid, userUidB, "../xml-models/subscriptionBInstance.xml")


catalogs()
    