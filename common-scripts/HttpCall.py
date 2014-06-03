import sys
from java.net import URL
from java.net import URLEncoder
from java.io import DataOutputStream
from java.io import BufferedReader
from java.io import InputStreamReader

def post(targetURL, params, contentType="text/xml"):

    paramStr = params["data"]
    url = URL(targetURL)
    #print targetURL
    #print paramStr
    #print contentType
    connection = url.openConnection()
    connection.setRequestMethod("POST")
    connection.setRequestProperty("Content-Type", contentType)
    connection.setRequestProperty("Content-Length", str(len(paramStr)))
    connection.setRequestProperty("Content-Language", "en-GB")
    connection.setUseCaches(0)
    connection.setDoInput(1)
    connection.setDoOutput(2)
    
    wr= DataOutputStream(connection.getOutputStream())
    wr.writeBytes(paramStr)
    wr.flush()
    wr.close()
    
    inStream= connection.getInputStream()
    rd= BufferedReader(InputStreamReader(inStream))
    response = ""
    line = rd.readLine()
    while line != None:
        response +=line+"\r"
        line = rd.readLine()
    rd.close()
    return response
    
def get(targetURL, params):

    paramStr = ""
    for aKey in params.keys():
        paramStr+=aKey+"="+URLEncoder.encode(params[aKey], "UTF-8")+"&"
    paramStr=paramStr[:-1]
    url = URL(targetURL+"?"+paramStr)
    #print url
    connection = url.openConnection()
    connection.setRequestMethod("GET")    
    connection.setRequestProperty("Content-Language", "en-GB")
    connection.setUseCaches(0)
    connection.setDoOutput(2)
    
    inStream= connection.getInputStream()
    rd= BufferedReader(InputStreamReader(inStream))
    response = ""
    line = rd.readLine()
    while line != None:
        response +=line+"\r"
        line = rd.readLine()
    rd.close()
    return response
    
def delete(targetURL, params):
    url = URL(targetURL)
    connection = url.openConnection()
    connection.setRequestMethod("DELETE")    
    connection.setRequestProperty("Content-Language", "en-GB")
    connection.setUseCaches(0)
    connection.setDoOutput(2)
    inStream= connection.getInputStream()
    rd= BufferedReader(InputStreamReader(inStream))
    response = ""
    line = rd.readLine()
    while line != None:
        response +=line+"\r"
        line = rd.readLine()
    rd.close()
    return response
    

def callHttpPOST(uri, service, data, contentType="text/xml"):
    response = post(uri+service, data, contentType=contentType)
    return response

def callHttpDELETE(uri, service, data):
    response = delete(uri+service, data)
    return response
    
def callHttpGET(uri, service, data):
    response = get(uri+service, data)
    return response
    
    
       

    
    
    
    
        

