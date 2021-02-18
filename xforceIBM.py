import requests
from requests.auth import HTTPBasicAuth
# python -m pip install requests

import json

def myXForceChecker(url):

    # Auth first

    printResult = []
    # e.g. url = "https://exchange.xforce.ibmcloud.com/ip//114.200.4.207"
    # you need the api key and password from xforce ibm.
    # register here: https://exchange.xforce.ibmcloud.com/
    #
	  # 
    
    myResult1 = requests.get(url, auth=HTTPBasicAuth('API-KEI-FROM-XFORCE-IBM',
                                                     'API-PASSWORD-FROM-XFORCE-IBM'))
    c1 = myResult1.content
    myJson1 = json.loads(c1)

    # >>>>>>>>>>>  IP/Domain Report Check <<<<<<<<<<<<<

    #----------These three keys are for IP checker----------
    # [Print] Geo information
    if "geo" in myJson1:
        for key, value in myJson1["geo"].items():
            geo = str(value)
            #print geo
            printResult.append(geo)
            # Only print country
            # (Ignore country code)
            break
    # [Print] Overrall Risk Score
    if "score" in myJson1:
        if myJson1["score"] == 1:
            #print "Risk Score: " + str(myJson1["score"]) + " (low)"
            printResult.append(str(myJson1["score"]) + " (low)")
        else:
            #print "Risk Score: " + str(myJson1["score"])
            printResult.append(str(myJson1["score"]))
    # [Print] Categorization:
    if "cats" in myJson1:
        if myJson1["cats"]:
            for key, value in myJson1["cats"].items():
                cat = str(key) + " (" + str(value) + "%)"
                #print "Categorization: " + cat
                printResult.append(cat)
        else:
            #print "Categorization: Unsuspicious"
            printResult.append("Unsuspicious")

    return printResult
