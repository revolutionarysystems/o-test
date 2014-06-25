import sys
import base64
from java.net import URL
from java.net import URLEncoder
from java.io import DataOutputStream
from java.io import BufferedReader
from java.io import InputStreamReader

def post(targetURL, params, contentType="text/xml", username=None):
    
    if(type(params) is dict):
        paramStr = ""
        for aKey in params.keys():
            paramStr+=aKey+"="+URLEncoder.encode(params[aKey], "UTF-8")+"&"
        paramStr=paramStr[:-1]
    else:
        paramStr = params
        
    url = URL(targetURL)
    print targetURL
    print paramStr
    print contentType
    connection = url.openConnection()
    if username!=None:    
        userpass = username
        basicAuth = "Basic " + base64.b64encode(userpass);
        connection.setRequestProperty ("Authorization", basicAuth);
    connection.setRequestMethod("POST")
    if contentType != None:
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
    return getResponse(connection);
    
def get(targetURL, params, username=None):

    paramStr = ""
    for aKey in params.keys():
        paramStr+=aKey+"="+URLEncoder.encode(params[aKey], "UTF-8")+"&"
    paramStr=paramStr[:-1]
    url = URL(targetURL+"?"+paramStr)
    print url
    connection = url.openConnection()

    if username!=None:    
        userpass = username
        basicAuth = "Basic " + base64.b64encode(userpass);
        print basicAuth
        connection.setRequestProperty ("Authorization", basicAuth);
    
    connection.setRequestMethod("GET")    
    connection.setRequestProperty("Content-Language", "en-GB")
    connection.setUseCaches(0)
    connection.setDoOutput(2)
    
    return getResponse(connection);
    
def delete(targetURL, params):
    url = URL(targetURL)
    connection = url.openConnection()
    connection.setRequestMethod("DELETE")    
    connection.setRequestProperty("Content-Language", "en-GB")
    connection.setUseCaches(0)
    connection.setDoOutput(2)
    return getResponse(connection);
    

def callHttpPOST(uri, service, data, contentType="text/xml", username=None):
    response = post(uri+service, data, contentType=contentType, username=username)
    return response

def callHttpDELETE(uri, service, data):
    response = delete(uri+service, data)
    return response
    
def callHttpGET(uri, service, data, username=None):
    response = get(uri+service, data, username=username)
    return response
    
def getResponse(connection):
    responseCode = connection.getResponseCode()
    if(responseCode >= 400):
        inStream = connection.getErrorStream()
        errorMessage = readInputStreamToString(inStream)
        raise Exception("Server return HTTP response code: " + str(responseCode) + " (" + errorMessage + ") for URL: " + connection.getURL().toString())
    inStream= connection.getInputStream()
    response = readInputStreamToString(inStream)
    return response
    
def readInputStreamToString(inStream):
    if(inStream == None):
        return "";
    rd= BufferedReader(InputStreamReader(inStream))
    response = ""
    line = rd.readLine()
    while line != None:
        response +=line+"\r"
        line = rd.readLine()
    rd.close()
    return response
    
    
       

    
    
    
    
        

