import requests, json, pprint, time, socket

# Disable warnings from untrusted server certificates
try:
    from requests.packages.urllib3.exceptions import InsecureRequestWarning
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
except Exception:
    print("Ignore messages related to insecure SSL certificates")

################
## make the json GET call to the public api
################
def jsonGet(targetUrl, user, password):
    # set the headers for how we want the response
    headers = {'content-type': 'application/json','accept':'application/json'}

    #make the actual request, specifying the URL, the JSON from above, standard basic auth, the headers and not to verify the SSL cert.
    #r = requests.post(target_uri, requestJSON, auth=('smc', 'smc'), headers=headers, verify=False)
    try:
        r = requests.get(targetUrl, auth=(user, password), headers=headers, verify=False)
    except:
        print("Exception:  Can't connect to API server URL:  " + targetUrl)
        print("Exiting")
        exit(1)

    #take the raw response text and deserialize it into a python object.
    try:
        responseObj = json.loads(r.text)
    except:
        print("Exception")
        print(r.text)

    # this test is specific to the contents of the Unisphere API
    if not responseObj.get("success", True):
        print(responseObj.get("message", "API failed to return expected result"))
        jsonPrint(responseObj)
        return dict()

    return responseObj

################
## make the json POST call to the public api
################
def jsonPost(targetUrl, requestObj, user, password):
    # set the headers for how we want the response
    headers = {'content-type': 'application/json','accept':'application/json'}

   #turn this into a JSON string
    requestJSON = json.dumps(requestObj, sort_keys=True, indent=4)
    #print(requestJSON)

    #make the actual request, specifying the URL, the JSON from above, standard basic auth, the headers and not to verify the SSL cert.
    try:
        r = requests.post(targetUrl, requestJSON, auth=(user, password), headers=headers, verify=False)
    except:
        print("Exception:  Can't connect to API server URL:  " + targetUrl)
        print("Exiting")
        exit(1)

    #take the raw response text and deserialize it into a python object.
    try:
        responseObj = json.loads(r.text)
    except:
        print("Exception")
        print(r.text)
    #jsonPrint(responseObj)
    return responseObj


################
## print a json object nicely
################
def jsonPrint(jsonObj):
	print(json.dumps(jsonObj, sort_keys=False, indent=2))


#################################################################
## Functions to implement Unisphere REST API for VMAX3
#################################################################


################
## get the version of Unisphere (the API)
################
def getVersion(URL, user, password):
    target_uri = "%s/univmax/restapi/system/version" % (URL)
    responseKey = 'version'
    responseObj = jsonGet(target_uri, user, password)
    if responseKey in responseObj:
        return responseObj[responseKey]
    else:
        return dict()

################
## get a list of symmetrix serial #'s known by Unisphere
################
def getSymms(URL, user, password):
    target_uri = "%s/univmax/restapi/system/symmetrix" % (URL)
    responseKey = 'symmetrixId'
    responseObj = jsonGet(target_uri, user, password)
    if responseKey in responseObj:
        return responseObj[responseKey]
    else:
        return dict()

################
## This call queries for a specific Authorized Symmetrix Object that is compatible with slo provisioning using its ID
################
def getSymm(URL, symmId, user, password):
    target_uri = "%s/univmax/restapi/system/symmetrix/%s" % (URL, symmId)
    responseKey = 'symmetrix'
    responseObj = jsonGet(target_uri, user, password)
    if responseKey in responseObj:
        return responseObj[responseKey][0]
    else:
        return dict()


def getSloSymms(URL, user, password):
    target_uri = "%s/univmax/restapi/sloprovisioning/symmetrix" % (URL)
    responseKey = 'symmetrixId'
    responseObj = jsonGet(target_uri, user, password)
    if responseKey in responseObj:
        return responseObj[responseKey]
    else:
        return dict()

def getSloSymm(URL, symmId, user, password):
    target_uri = "%s/univmax/restapi/sloprovisioning/symmetrix/%s" % (URL, symmId)
    responseKey = 'symmetrix'
    responseObj = jsonGet(target_uri, user, password)
    if responseKey in responseObj:
        return responseObj[responseKey][0]
    else:
        return dict()

def getSloDirectors(URL, symmId, user, password):
    target_uri = "%s/univmax/restapi/sloprovisioning/symmetrix/%s/director" % (URL, symmId)
    responseKey = 'directorId'
    responseObj = jsonGet(target_uri, user, password)
    if responseKey in responseObj:
        return responseObj[responseKey]
    else:
        return dict()

def getSloDirector(URL, symmId, directorId, user, password):
    target_uri = "%s/univmax/restapi/sloprovisioning/symmetrix/%s/director/%s" % (URL, symmId, directorId)
    responseKey = 'director'
    responseObj = jsonGet(target_uri, user, password)
    if responseKey in responseObj:
        return responseObj[responseKey][0]
    else:
        return dict()

def getSloPorts(URL, symmId, directorId, user, password):
    target_uri = "%s/univmax/restapi/sloprovisioning/symmetrix/%s/director/%s/port" % (URL, symmId, directorId)
    responseKey = 'symmetrixPortKey'
    responseObj = jsonGet(target_uri, user, password)
    if responseKey in responseObj:
        return responseObj[responseKey]
    else:
        return dict()

def getSloPort(URL, symmId, directorId, portId, user, password):
    target_uri = "%s/univmax/restapi/sloprovisioning/symmetrix/%s/director/%s/port/%s" % (URL, symmId, directorId, portId)
    responseKey = 'symmetrixPort'
    responseObj = jsonGet(target_uri, user, password)
    if responseKey in responseObj:
        return responseObj[responseKey][0]
    else:
        return dict()

def getSloHosts(URL, symmId, user, password):
    target_uri = "%s/univmax/restapi/sloprovisioning/symmetrix/%s/host" % (URL, symmId)
    responseKey = 'hostId'
    responseObj = jsonGet(target_uri, user, password)
    if responseKey in responseObj:
        return responseObj[responseKey]
    else:
        return dict()

def getSloHost(URL, symmId, hostId, user, password):
    target_uri = "%s/univmax/restapi/sloprovisioning/symmetrix/%s/host/%s" % (URL, symmId, hostId)
    responseKey = 'host'
    responseObj = jsonGet(target_uri, user, password)
    if responseKey in responseObj:
        return responseObj[responseKey][0]
    else:
        return dict()

def getSloHostgrps(URL, symmId, user, password):
    target_uri = "%s/univmax/restapi/sloprovisioning/symmetrix/%s/hostgroup" % (URL, symmId)
    responseKey = 'hostGroupId'
    responseObj = jsonGet(target_uri, user, password)
    if responseKey in responseObj:
        return responseObj[responseKey]
    else:
        return dict()

def getSloHostgrp(URL, symmId, grpId, user, password):
    target_uri = "%s/univmax/restapi/sloprovisioning/symmetrix/%s/hostgroup/%s" % (URL, symmId, grpId)
    responseKey = 'hostGroup'
    responseObj = jsonGet(target_uri, user, password)
    if responseKey in responseObj:
        return responseObj[responseKey][0]
    else:
        return dict()

def getSloInitiators(URL, symmId, user, password):
    target_uri = "%s/univmax/restapi/sloprovisioning/symmetrix/%s/initiator" % (URL, symmId)
    responseKey = 'initiatorId'
    responseObj = jsonGet(target_uri, user, password)
    if responseKey in responseObj:
        return responseObj[responseKey]
    else:
        return dict()

def getSloInitator(URL, symmId, initiatorId, user, password):
    target_uri = "%s/univmax/restapi/sloprovisioning/symmetrix/%s/initiator/%s" % (URL, symmId, initatorId)
    responseKey = 'initiator'
    responseObj = jsonGet(target_uri, user, password)
    if responseKey in responseObj:
        return responseObj[responseKey][0]
    else:
        return dict()

def getSloMaskingviews(URL, symmId, user, password):
    target_uri = "%s/univmax/restapi/sloprovisioning/symmetrix/%s/maskingview" % (URL, symmId)
    responseKey = 'maskingViewId'
    responseObj = jsonGet(target_uri, user, password)
    if responseKey in responseObj:
        return responseObj[responseKey]
    else:
        return dict()

def getSloMaskingview(URL, symmId, mvId, user, password):
    target_uri = "%s/univmax/restapi/sloprovisioning/symmetrix/%s/maskingview/%s" % (URL, symmId, mvId)
    responseKey = 'maskingView'
    responseObj = jsonGet(target_uri, user, password)
    if responseKey in responseObj:
        return responseObj[responseKey][0]
    else:
        return dict()

def getSloMvConnections(URL, symmId, mvId, user, password):
    target_uri = "%s/univmax/restapi/sloprovisioning/symmetrix/%s/maskingview/%s/connections" % (URL, symmId, mvId)
    responseKey = 'maskingViewConnection'
    responseObj = jsonGet(target_uri, user, password)
    if responseKey in responseObj:
        return responseObj[responseKey]
    else:
        return dict()

def getSloPorts(URL, symmId, user, password):
    target_uri = "%s/univmax/restapi/sloprovisioning/symmetrix/%s/port" % (URL, symmId)
    responseKey = 'symmetrixPortKey'
    responseObj = jsonGet(target_uri, user, password)
    if responseKey in responseObj:
        return responseObj[responseKey]
    else:
        return dict()

def getSloPortgrps(URL, symmId, user, password):
    target_uri = "%s/univmax/restapi/sloprovisioning/symmetrix/%s/portgroup" % (URL, symmId)
    responseKey = 'portGroupId'
    responseObj = jsonGet(target_uri, user, password)
    if responseKey in responseObj:
        return responseObj[responseKey]
    else:
        return dict()

def getSloPortgrp(URL, symmId, pgId, user, password):
    target_uri = "%s/univmax/restapi/sloprovisioning/symmetrix/%s/portgroup/%s" % (URL, symmId, pgId)
    responseKey = 'portGroup'
    responseObj = jsonGet(target_uri, user, password)
    if responseKey in responseObj:
        return responseObj[responseKey][0]
    else:
        return dict()

def getSlos(URL, symmId, user, password):
    target_uri = "%s/univmax/restapi/sloprovisioning/symmetrix/%s/slo" % (URL, symmId)
    responseKey = 'sloId'
    responseObj = jsonGet(target_uri, user, password)
    if responseKey in responseObj:
        return responseObj[responseKey]
    else:
        return dict()

def getSlo(URL, symmId, sloId, user, password):
    target_uri = "%s/univmax/restapi/sloprovisioning/symmetrix/%s/slo/%s" % (URL, symmId, sloId)
    responseKey = 'slo'
    responseObj = jsonGet(target_uri, user, password)
    if responseKey in responseObj:
        return responseObj[responseKey][0]
    else:
        return dict()

def getSrps(URL, symmId, user, password):
    target_uri = "%s/univmax/restapi/sloprovisioning/symmetrix/%s/srp" % (URL, symmId)
    responseKey = 'srpId'
    responseObj = jsonGet(target_uri, user, password)
    if responseKey in responseObj:
        return responseObj[responseKey]
    else:
        return dict()

def getSrp(URL, symmId, srpId, user, password):
    target_uri = "%s/univmax/restapi/sloprovisioning/symmetrix/%s/srp/%s" % (URL, symmId, srpId)
    responseKey = 'srp'
    responseObj = jsonGet(target_uri, user, password)
    if responseKey in responseObj:
        return responseObj[responseKey][0]
    else:
        return dict()

################
## get a list of Storage Groups on a given SLO Symmetrix
################
def getSgList(URL, symmId, user, password):
    target_uri = "%s/univmax/restapi/sloprovisioning/symmetrix/%s/storagegroup" % (URL, symmId)
    responseKey = 'storageGroupId'
    responseObj = jsonGet(target_uri, user, password)
    if responseKey in responseObj:
        return responseObj[responseKey]
    else:
        return dict()

################
## get the details of a particular SLO managed Storage Group
################
def getSg(URL, symmId, sgId, user, password):
    target_uri = "%s/univmax/restapi/sloprovisioning/symmetrix/%s/storagegroup/%s" % (URL, symmId, sgId)
    responseKey = 'storageGroup'
    responseObj = jsonGet(target_uri, user, password)
    if responseKey in responseObj:
        return responseObj[responseKey][0]
    else:
        return dict()

################
## get a list of Thin Pools on a given Symmetrix
################
def getThinPoolList(URL, symmId, user, password):
    target_uri = "%s/univmax/restapi/provisioning/symmetrix/%s/thinpool" % (URL, symmId)
    responseKey = 'poolId'
    responseObj = jsonGet(target_uri, user, password)
    if responseKey in responseObj:
        return responseObj[responseKey]
    else:
        return dict()

################
## get the details of a particular Thin Pool
################
def getThinPool(URL, symmId, tpId, user, password):
    target_uri = "%s/univmax/restapi/provisioning/symmetrix/%s/thinpool/%s" % (URL, symmId, tpId)
    responseKey = 'poolId'
    responseObj = jsonGet(target_uri, user, password)
    if responseKey in responseObj:
        return responseObj[responseKey][0]
    else:
        return dict()

