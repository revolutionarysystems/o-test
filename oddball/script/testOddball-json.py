import sys
import urllib

import setPath
reload(setPath)
import HttpCall
reload(HttpCall)

from java.io import File
from java.util import Date


uri = "http://localhost:8080"
service = "/oddball-service"

sampleData = [
        '{ "case":"1000"  }',
        '{ "browser":"chrome", "platform":"Win"  }',
        '{ "browser":"firefox", "platform":"Win32"  }',
        '{ "browser":"safari", "platform":"ios"  }',
        '{ "browser":"safari", "platform":"Android"  }',
        '{ "browser":"safari", "platform":"MacOS"  }',
        '{ "browser":"chrome", "platform":"Win", "screen": {"availWidth": 1600}  }',
        '{ "browser":"chrome", "platform":"Win", "screen": {"availWidth": 550}  }',
        '{ "browser":"chrome", "platform":"Win", "availWidth": 550}',
        '{ "browser":"chrome", "platform":"Win", "screen": {"availWidth": 500}  }',
        ]

clearData = {"ruleSet":"ECBaseRules.txt", "action":"clear"}
HttpCall.callHttpGET(uri, service, clearData).strip()
print Date()
for i in range(2000):
    for case in sampleData:
        data = {"ruleSet":"ECBaseRules.txt", "case":case}
        res=HttpCall.callHttpGET(uri, service, data).strip()
        #print res,
print
print Date()
    
