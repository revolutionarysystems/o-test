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
        "Y304RPD",
        "Z304RAX",
        "ABC304R",
        "RE02UBD",
        "423ABC113",
        "123X113",
        "89HJ67",
        "RE52UAD",
        "ABC123",
        "AB12CD",
        "123D113",
        "AB12CD",
        ]

for case in sampleData:
    data = {"ruleSet":"Reg.txt", "case":case}
    print HttpCall.callHttpGET(uri, service, data)