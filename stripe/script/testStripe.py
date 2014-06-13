print "."
import sys
import urllib

print "."
import setPath
reload(setPath)
import HttpCall
reload(HttpCall)

from java.io import File
from java.util import Date



uri = "https://api.stripe.com/v1"

#list plans
#service = "/plans"
#print HttpCall.callHttpGET(uri, service, {}, username="sk_test_4qo3vbZaV6CI9l3ITyox2St3")

#get card token
def getCardToken():
    service = "/tokens"
    params = {
                "card[number]":"4242424242424242",
                "card[exp_month]":"12",
                "card[exp_year]":"2015",
                "card[cvc]":"123",
             }
    res = HttpCall.callHttpPOST(uri, service, params, contentType=None, username="sk_test_4qo3vbZaV6CI9l3ITyox2St3")
    res2 = res.replace("\r", "")
    null=None
    false=0
    true=1
    cardDict = eval(res2)
    return cardDict["id"]

def createCustomer():
    service = "/customers"
    params = {
                "card":getCardToken(),
                "description":"test example for revsys",
             }
    res = HttpCall.callHttpPOST(uri, service, params, contentType=None, username="sk_test_4qo3vbZaV6CI9l3ITyox2St3")
    res2 = res.replace("\r", "")
    null=None
    false=0
    true=1
    dict = eval(res2)
    return dict["id"]


def createSubscription(customerId):
    service = "/customers/"+customerId+"/subscriptions"
    params = {
                "plan":"eCKB-t",
             }
    res = HttpCall.callHttpPOST(uri, service, params, contentType=None, username="sk_test_4qo3vbZaV6CI9l3ITyox2St3")
    res2 = res.replace("\r", "")
    null=None
    false=0
    true=1
    dict = eval(res2)
    return dict["id"]

customerId = createCustomer()
subscriptionId = createSubscription(customerId)

print subscriptionId

