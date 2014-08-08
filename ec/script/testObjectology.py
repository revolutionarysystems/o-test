import sys
import urllib

import setPath
reload(setPath)
import o_utils
reload(o_utils)
import t_utils
reload(t_utils)
import s_utils
reload(s_utils)

from java.io import File
from java.io import FileNotFoundException
from java.util import Date



def loadTemplates():
    o_utils.loadTemplateFromFile("../haven_artifacts/main/subscription-manager-templates/user.xml")
    o_utils.loadTemplateFromFile("../haven_artifacts/main/subscription-manager-templates/account.xml")
    o_utils.loadTemplateFromFile("../haven_artifacts/main/subscription-manager-templates/product.xml")



def simpleDataSet():
    #Build Sample Data from scratch

    print Date()
    s_utils.clearData()
    loadTemplates()

    productTemplateId = o_utils.getTemplateIdByName("Product Template")
    accountTemplateId = o_utils.getTemplateIdByName("Account Template")
    userTemplateId = o_utils.getTemplateIdByName("User Template")

    s_utils.createProductInstance(productTemplateId, accountTemplateId,"../xml/echoCHECKProduct.xml")
    eCKBProdId = o_utils.getInstanceIdByProperty("product", "shortCode", "eCKB")
    s_utils.createProductInstance(productTemplateId, accountTemplateId,"../xml/echoCHATProduct.xml")
    eCTBProdId = o_utils.getInstanceIdByProperty("product", "shortCode", "eCTB")
    s_utils.createProductInstance(productTemplateId, accountTemplateId,"../xml/echoCentralBaseProduct.xml")
    eCntBProdId = o_utils.getInstanceIdByProperty("product", "shortCode", "eCntB")
    s_utils.createProductInstance(productTemplateId, accountTemplateId,"../xml/echoCentralAccountProduct.xml")
    shortCode="eCnt"
    productId = o_utils.getInstanceIdByProperty("product", "shortCode", shortCode)

    print Date()
    for i in range(10):
        if i%100==0:
            print "account #", i
        userId = o_utils.getIdFromJSON(s_utils.createUserInstance(userTemplateId,"","../xml/userInstance.xml"))
        accountId = o_utils.getIdFromJSON(s_utils.createAccountInstance(accountTemplateId, userTemplateId, productId, eCntBProdId, eCKBProdId, userId, shortCode, "../xml/accountInstance.xml", case=i))
        s_utils.addAccountUser(accountId, userId, "../xml/accountAddUser.xml", case=i)
        for j in range(9):
            userId = o_utils.getIdFromJSON(s_utils.createUserInstance(userTemplateId,accountId,"../xml/userInstance.xml", case=10000*i+j))
            s_utils.addAccountUser(accountId, userId, "../xml/accountAddUser.xml", case=i)
        if t_utils.randomBoolean(0.6):
            s_utils.setStatus("account", accountId, "Live", "../xml/accountSetDeepStatus.xml", case=i)
        if t_utils.randomBoolean(0.6):
            s_utils.updateAccount(accountId, "../xml/accountAddSubscription.xml", substitutions = {"{eCTProductId}":eCTBProdId}, case=i)


    print Date()
    #s_utils.catalogs()
    s_utils.idCatalogs()
    print Date()



def contentType(format):
    if format=="xml":
        return "text/xml"
    elif format == "json":
        return "application/json"
    else:
        return "text/plain"
    


def servicesCatalog(format="xml"):
    #account.list
    def account_list():
        return o_utils.getInstanceSummaries("account")
    #print account_list()


    #account.create
    def createAccount(contentType="xml"):
        productTemplateId = o_utils.getTemplateIdByName("Product Template")
        accountTemplateId = o_utils.getTemplateIdByName("Account Template")
        userTemplateId = o_utils.getTemplateIdByName("User Template")
        productId = o_utils.getInstanceIdByProperty("product", "shortCode", "eCnt")
        eCntBProdId = o_utils.getInstanceIdByProperty("product", "shortCode", "eCntB")
        eCKBProdId = o_utils.getInstanceIdByProperty("product", "shortCode", "eCKB")
        userId=""
        accountId = o_utils.getIdFromJSON(s_utils.createAccountInstance(accountTemplateId, userTemplateId, productId, eCntBProdId, eCKBProdId, userId, "eCnt", "../"+format+"/accountInstance."+format, contentType=contentType))
        return accountId
    accountId=createAccount(contentType=contentType(format))
    s_utils.showLink(accountId,"account/")

    #account.update
    def accountMainUser(accountId, contentType="xml"):
        userTemplateId = o_utils.getTemplateIdByName("User Template")
        userId = o_utils.getIdFromJSON(s_utils.createUserInstance(userTemplateId,accountId,"../"+format+"/userInstance."+format, contentType=contentType))
        s_utils.setAccountMainUser(accountId, userId, "../"+format+"/accountMainUser."+format, contentType=contentType)
        return userId
    userId = accountMainUser(accountId, contentType=contentType(format))
    s_utils.showLink(userId,"user/")

    #account.details
    s_utils.showLink(accountId,"account/")

    #(user.details)
    s_utils.showLink(userId,"user/")

    #account.delete
    o_utils.deleteInstance("account", accountId)

    #try:
    #    print o_utils.getIdFromJSON(o_utils.getInstance("account", accountId))
    #except FileNotFoundException, e:
    #    print "Not Found:",e



    #subscription.list
    #subscription.details
    accountId=createAccount(contentType=contentType(format))
    s_utils.showLink(accountId,"account/")
    subscriptions = o_utils.getCollectionFromJSON(o_utils.getInstance("account", accountId), "subscriptions")

    #subscription.create
    eCTBProdId = o_utils.getInstanceIdByProperty("product", "shortCode", "eCTB")
    s_utils.updateAccount(accountId, "../"+format+"/accountAddSubscription."+format, substitutions = {"{eCTProductId}":eCTBProdId}, contentType=contentType(format))
    s_utils.showLink(accountId,"account/")


    #subscription.update
    eCntBProdId = o_utils.getInstanceIdByProperty("product", "shortCode", "eCntB")
    eCKBProdId = o_utils.getInstanceIdByProperty("product", "shortCode", "eCKB")
    eCTBProdId = o_utils.getInstanceIdByProperty("product", "shortCode", "eCTB")
    s_utils.updateAccount(accountId, "../"+format+"/accountUpdateSubscriptions."+format, substitutions = {"{eCTProductId}":eCTBProdId,"{eCKProductId}":eCKBProdId,"{eCntProductId}":eCntBProdId}, contentType=contentType(format))
    s_utils.showLink(accountId,"account/")


    #subscription.delete
    eCntBProdId = o_utils.getInstanceIdByProperty("product", "shortCode", "eCntB")
    eCTBProdId = o_utils.getInstanceIdByProperty("product", "shortCode", "eCTB")
    s_utils.updateAccount(accountId, "../"+format+"/accountDeleteSubscription."+format, substitutions = {"{eCTProductId}":eCTBProdId,"{eCKProductId}":eCKBProdId,"{eCntProductId}":eCntBProdId}, contentType=contentType(format))
    s_utils.showLink(accountId,"account/")


    userTemplateId = o_utils.getTemplateIdByName("User Template")
    for i in range(1):
        userId = o_utils.getIdFromJSON(s_utils.createUserInstance(userTemplateId,accountId,"../"+format+"/userInstance."+format, contentType=contentType(format)))
        #s_utils.addAccountUser(accountId, userId, "../"+format+"/accountAddUser."+format, contentType=contentType(format))
    s_utils.showLink(accountId,"account/")


    #user.list
    #user.details
    users = o_utils.getCollectionFromJSON(o_utils.getInstance("account", accountId), "users")
    for user in users:
        s_utils.showLink(user,"user/query?view=summary&_id=")
        s_utils.showLink(user,"user/")

    #user.create
    userId = o_utils.getIdFromJSON(s_utils.createUserInstance(userTemplateId,accountId,"../"+format+"/userInstance."+format, contentType=contentType(format)))
    s_utils.addAccountUser(accountId, userId, "../"+format+"/accountAddUser."+format, contentType=contentType(format))
    s_utils.showLink(accountId,"account/")

    #user.update
    s_utils.updateUser(userId, "../"+format+"/userUpdateAddress."+format,contentType=contentType(format))
    s_utils.showLink(userId,"user/")

    #user.delete
    userIds = o_utils.getCollectionFromJSON(o_utils.getInstance("account", accountId), "users")
    userIds.remove(userIds[0])
    s_utils.updateAccount(accountId, "../"+format+"/accountDeleteUsers."+format, substitutions = {"{users}":t_utils.buildLinkCollection("users", "user", userIds, format=format)}, contentType=contentType(format))


simpleDataSet()    

#servicesCatalog(format="xml")
#servicesCatalog(format="json")

def queryCatalog():

    #result = queryInstance("user", "../json/queryUserName.json", substitutions={"{name}":"Viola Sullivan"})
    result = s_utils.queryInstance("user", "../json/queryFieldLike.json", substitutions={"{field}":"name", "{fragment}":"Kel"})

    #result = queryInstance("user", "../json/queryFieldLike.json", substitutions={"{field}":"contactDetails", "{fragment}":"gu6 6a"})
    #result = queryInstance("user", "../json/queryFieldLike.json", substitutions={"{field}":"user-manager-id", "{fragment}":"X45V-2241"})

    #result = queryInstance("user", "../json/queryFieldLike.json", substitutions={"{field}":"name", "{fragment}":"Kel"})
    #print queryInstance("user", "../json/query_id.json", substitutions={"{id}":"eb498e8a-05e2-4f46-a459-26aab43832a0"})

    for instance in result:
        print instance

#queryCatalog()
