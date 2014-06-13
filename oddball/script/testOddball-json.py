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


uri = "http://localhost:8080"
service = "/oddball-service"


sessions = ["ab10", "ab11", "ab12", "ab13", "ab14", "ab15", "ab16", "ab17", "ab18", "ab19", "ab20", "ab21", "ab22"]
users = ["a123", "b234", "c345", "d456", "e567", "mikeytest"]
sampleData = [
        '{ "case":"1000"  }',
        '{ "browser":"chrome", "platform":"Win", "sessionId": "{sessionId}", "userId": "{userId}"  }',
        '{ "browser":"firefox", "platform":"Win32", "sessionId": "{sessionId}", "userId": "{userId}"     }',
        '{ "browser":"safari", "platform":"ios", "sessionId": "{sessionId}", "userId": "{userId}"     }',
        '{ "browser":"safari", "platform":"Android", "sessionId": "{sessionId}", "userId": "{userId}"     }',
        '{ "browser":"safari", "platform":"MacOS", "sessionId": "{sessionId}", "userId": "{userId}"     }',
        '{ "browser":"chrome", "platform":"Win32", "screen": {"availWidth": 1600}, "sessionId": "{sessionId}", "userId": "{userId}"     }',
        '{ "browser":"chrome", "platform":"Win32", "screen": {"availWidth": 550}, "sessionId": "{sessionId}", "userId": "{userId}"     }',
        '{ "browser":"chrome", "platform":"Win64", "availWidth": 550, "sessionId": "{sessionId}", "userId": "{userId}"   }',
        '{ "browser":"chrome", "platform":"Win64", "screen": {"availWidth": 500}, "sessionId": "{sessionId}", "userId": "{userId}"     }',
        ]

#clearData = {"ruleSet":"ECBaseRules.txt", "action":"clear"}
#HttpCall.callHttpGET(uri, service+"/ruleSet/"+clearData["ruleSet"], clearData).strip()

retrieveData = {"ruleSet":"ECBaseRules.txt"}
fullUri = uri+service+"/ruleSet/"+retrieveData["ruleSet"]+"/bin/reload"
print fullUri
res = HttpCall.callHttpGET(uri, service+"/ruleSet/"+retrieveData["ruleSet"]+"/bin/reload",{}).strip()
print res

print


print Date()
for i in range(1):
    for case in sampleData:
        data = {"ruleSet":"ECBaseRules.txt", "case":case.replace('{sessionId}', sessions[8 * i%len(sessions)]).replace('{userId}', users[i%len(users)])}
        res=HttpCall.callHttpGET(uri, service+"/ruleSet/"+data["ruleSet"], data).strip()
        print res
print
print Date()
    
retrieveData = {"ruleSet":"ECBaseRules.txt"}
fullUri = uri+service+"/ruleSet/"+retrieveData["ruleSet"]+"/case/"
print fullUri
res = HttpCall.callHttpGET(uri, service+"/ruleSet/"+retrieveData["ruleSet"]+"/case/", {}).strip()
print res

print

retrieveData = {"ruleSet":"ECBaseRules.txt", "sessionId":"ab10"}
fullUri = uri+service+"/ruleSet/"+retrieveData["ruleSet"]+"/sessionId/"+retrieveData["sessionId"]
print fullUri
res = HttpCall.callHttpGET(uri, service+"/ruleSet/"+retrieveData["ruleSet"]+"/sessionId/"+retrieveData["sessionId"], {}).strip()
print res

print

retrieveData = {"ruleSet":"ECBaseRules.txt", "userId":"a123"}
fullUri = uri+service+"/ruleSet/"+retrieveData["ruleSet"]+"/userId/"+retrieveData["userId"]
print fullUri
res = HttpCall.callHttpGET(uri, service+"/ruleSet/"+retrieveData["ruleSet"]+"/userId/"+retrieveData["userId"], {}).strip()
print res

retrieveData = {"ruleSet":"ECBaseRules.txt"}
fullUri = uri+service+"/ruleSet/"+retrieveData["ruleSet"]+"/sessionId/"
print fullUri
res = HttpCall.callHttpGET(uri, service+"/ruleSet/"+retrieveData["ruleSet"]+"/sessionId/", {}).strip()
print res

print

retrieveData = {"ruleSet":"ECBaseRules.txt"}
fullUri = uri+service+"/ruleSet/"+retrieveData["ruleSet"]+"/userId/"
print fullUri
res = HttpCall.callHttpGET(uri, service+"/ruleSet/"+retrieveData["ruleSet"]+"/userId/", {}).strip()
print res

print

retrieveData = {"ruleSet":"ECBaseRules.txt", "query":'{ "case.browser": "firefox" }'}
fullUri = uri+service+"/ruleSet/"+retrieveData["ruleSet"]+"/query/"+retrieveData["query"]
print fullUri
res = HttpCall.callHttpGET(uri, service+"/ruleSet/"+retrieveData["ruleSet"]+"/query/", {"query":retrieveData["query"]}).strip()
print res

print


retrieveData = {"ruleSet":"ECBaseRules.txt", "query":'{ "tags": "WinXX", "case.userId" : "mikeytest"}'}
fullUri = uri+service+"/ruleSet/"+retrieveData["ruleSet"]+"/query/"+retrieveData["query"]
print fullUri
res = HttpCall.callHttpGET(uri, service+"/ruleSet/"+retrieveData["ruleSet"]+"/query/", {"query":retrieveData["query"]}).strip()
print res


mins_ago=Date().getTime() - 18 * 60 * 1000

retrieveData = {"ruleSet":"ECBaseRules.txt", "query":'{ "tags": "WinXX", "case.userId" : "mikeytest", "timeStamp": { "$gt": "'+str(mins_ago)+'"} }'}
fullUri = uri+service+"/ruleSet/"+retrieveData["ruleSet"]+"/query/"+retrieveData["query"]
print fullUri
res = HttpCall.callHttpGET(uri, service+"/ruleSet/"+retrieveData["ruleSet"]+"/query/", {"query":retrieveData["query"]}).strip()
print res

print

retrieveData = {"ruleSet":"ECBaseRules.txt"}
fullUri = uri+service+"/ruleSet/"+retrieveData["ruleSet"]+"/bin/"
print fullUri
res = HttpCall.callHttpGET(uri, service+"/ruleSet/"+retrieveData["ruleSet"]+"/bin/",{}).strip()
print res

print

retrieveData = {"ruleSet":"ECBaseRules.txt","bin":"bin1"}
fullUri = uri+service+"/ruleSet/"+retrieveData["ruleSet"]+"/bin/"+retrieveData["bin"]
print fullUri
res = HttpCall.callHttpGET(uri, service+"/ruleSet/"+retrieveData["ruleSet"]+"/bin/"+retrieveData["bin"],{}).strip()
print res

print


