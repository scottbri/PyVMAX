#!/usr/bin/python

import requests, json, pprint, time, socket

################
## make the json GET call to the public api
################
def jsonGet(targetUrl, userId, password):
    # set the headers for how we want the response
    headers = {'content-type': 'application/json','accept':'application/json'}

    #make the actual request, specifying the URL, the JSON from above, standard basic auth, the headers and not to verify the SSL cert.
    #r = requests.post(target_uri, requestJSON, auth=('smc', 'smc'), headers=headers, verify=False)
    r = requests.get(targetUrl, auth=(userId, password), headers=headers, verify=False)

    #take the raw response text and deserialize it into a python object.
    try:
        responseObj = json.loads(r.text)
    except:
        print "Exception"
        print r.text
    #prettyPrint(responseObj)
    return responseObj

################
## make the json POST call to the public api
################
def jsonPost(targetUrl, requestObj, userId, password):
    # set the headers for how we want the response
    headers = {'content-type': 'application/json','accept':'application/json'}

   #turn this into a JSON string
    requestJSON = json.dumps(requestObj, sort_keys=True, indent=4)
    #print requestJSON

    #make the actual request, specifying the URL, the JSON from above, standard basic auth, the headers and not to verify the SSL cert.
    r = requests.post(targetUrl, requestJSON, auth=(userId, password), headers=headers, verify=False)

    #take the raw response text and deserialize it into a python object.
    try:
        responseObj = json.loads(r.text)
    except:
        print "Exception"
        print r.text
    #prettyPrint(responseObj)
    return responseObj


################
## print a json object nicely
################
def prettyPrint(jsonObj):
	print json.dumps(jsonObj, sort_keys=False, indent=2)


################
## get the version of Unisphere (the API)
################
def getVersion(URL, userId, password):
    target_uri = "%s/univmax/restapi/system/version" % (URL)
    responseObj = jsonGet(target_uri, user, password)
    if not responseObj.get("success", True):
        print responseObj.get("message", "API failed to return expected result")
        prettyPrint(responseObj)
        return None
    return responseObj['version']

################
## get a list of symmetrix serial #'s known by Unisphere
################
def getSymms(URL, userId, password):
    target_uri = "%s/univmax/restapi/system/symmetrix" % (URL)
    responseObj = jsonGet(target_uri, user, password)
    if not responseObj.get("success", True):
        print responseObj.get("message", "API failed to return expected result")
        print json.dumps(responseObj, sort_keys=False, indent=2)
        return None
    return responseObj['symmetrixId']

################
## This call queries for a specific Authorized Symmetrix Object that is compatible with slo provisioning using its ID
################
def getSymm(URL, symmId, userId, password):
    target_uri = "%s/univmax/restapi/system/symmetrix/%s" % (URL, symmId)
    responseObj = jsonGet(target_uri, user, password)
    if not responseObj.get("success", True):
        print responseObj.get("message", "API failed to return expected result")
        print json.dumps(responseObj, sort_keys=False, indent=2)
        return None
    return responseObj['symmetrix'][0]

################
## get a list of Storage Resource Pools on a given Symmetrix
################
def getSrpList(URL, symmId, userId, password):
    target_uri = "%s/univmax/restapi/sloprovisioning/symmetrix/%s/srp" % (URL, symmId)
    responseObj = jsonGet(target_uri, user, password)
    if not responseObj.get("success", True):
        print responseObj.get("message", "API failed to return expected result")
	prettyPrint(responseObj)
        return None
    return responseObj['srpId']

################
## get the details of a particular SRP
################
def getSrp(URL, symmId, srpId, userId, password):
    target_uri = "%s/univmax/restapi/sloprovisioning/symmetrix/%s/srp/%s" % (URL, symmId, srpId)
    responseObj = jsonGet(target_uri, user, password)
    if not responseObj.get("success", True):
        print responseObj.get("message", "API failed to return expected result")
	prettyPrint(responseObj)
        return None
    return responseObj['srp'][0]

################
## get a list of Storage Groups on a given SLO Symmetrix
################
def getSgList(URL, symmId, userId, password):
    target_uri = "%s/univmax/restapi/sloprovisioning/symmetrix/%s/storagegroup" % (URL, symmId)
    responseObj = jsonGet(target_uri, user, password)
    if not responseObj.get("success", True):
        print responseObj.get("message", "API failed to return expected result")
	prettyPrint(responseObj)
        return None
    prettyPrint(responseObj)
    return responseObj['storageGroupId']

################
## get the details of a particular SLO managed Storage Group
################
def getSg(URL, symmId, sgId, userId, password):
    #sgId = "ESX01_SQL"
    target_uri = "%s/univmax/restapi/sloprovisioning/symmetrix/%s/storagegroup/%s" % (URL, symmId, sgId)
    responseObj = jsonGet(target_uri, user, password)
    if not responseObj.get("success", True):
        print responseObj.get("message", "API failed to return expected result")
	prettyPrint(responseObj)
        return None
    prettyPrint(responseObj)
    return responseObj['storageGroup'][0]

################
## get a list of Thin Pools on a given Symmetrix
################
def getThinPoolList(URL, symmId, userId, password):
    target_uri = "%s/univmax/restapi/provisioning/symmetrix/%s/thinpool" % (URL, symmId)
    responseObj = jsonGet(target_uri, user, password)
    if not responseObj.get("success", True):
        print responseObj.get("message", "API failed to return expected result")
	prettyPrint(responseObj)
        return None
    return responseObj['poolId']

################
## get the details of a particular Thin Pool
################
def getThinPool(URL, symmId, tpId, userId, password):
    target_uri = "%s/univmax/restapi/provisioning/symmetrix/%s/thinpool/%s" % (URL, symmId, tpId)
    responseObj = jsonGet(target_uri, user, password)
    if not responseObj.get("success", True):
        print responseObj.get("message", "API failed to return expected result")
	prettyPrint(responseObj)
        return None
    return responseObj['thinPool'][0]


#################################


# TODO: Really need to bring these fields in from the command line rather than hard coding them
#URL = "https://localhost:8443"
URL = "https://192.168.250.250:8443"
user = "smc"
password = "smc"

# TODO: Do something based on the version of Unisphere
unisphereVersion = getVersion(URL, user, password)

# discover the known symmetrix serial #'s
symmIdList = getSymms(URL, user, password)

# going to build a list of dicts, each one a symmetrix
symmList = list()
for symmId in symmIdList:
    # get the array details
    symmetrix = getSymm(URL, symmId, user, password)

    # now gather more details and add them to the array dict

    # examine first two chars of ucode
    if symmetrix['ucode'][:2] == '59':
	    # VMAX3 with SRP and SLO based Provisioning

        # for this symmetrix, go ahead and build a list of SRP's
        srpList = list()
        for srpId in getSrpList(URL, symmId, user, password):
            srp = getSrp(URL, symmId, srpId, user, password)
            srpList.append(srp)

        # add a dict entry for the SRP list data structure we just created
        symmetrix['srp'] = srpList

        # for this symmetrix, go ahead and build a list of Storage Groups
        sgList = list()
        for sgId in getSgList(URL, symmId, user, password):
            sg = getSg(URL, symmId, sgId, user, password)
            sgList.append(sg)

        # add a dict entry for the Storage Group list data structure we just created
        symmetrix['storageGroup'] = sgList

    else:
        # this is an older Symmetrix with virtual provisioning

        # for this symmetrix, go ahead and build a list of Thin Pools
        tpList = list()
        for tpId in getThinPoolList(URL, symmId, user, password):
            tp = getThinPool(URL, symmId, tpId, user, password)
            tpList.append(tp)

        # add a dict entry for the SRP list data structure we just created
        symmetrix['thinpool'] = tpList

    # finally add this symmetrix dict data structure to the list of arrays
    symmList.append(symmetrix)

# do something useful with all this data, like print it out ;-)
prettyPrint(symmList)


##### END ####
# stuff I want to save


#requestObj = {'arrayParam':
#            {'endDate': int(time.time()*1000), #End time to specify is now.
#             'startDate': int(time.time()*1000)-(3600*1000), #start time is 60 minutes before that
#             'metrics': ['IO_RATE'], #array of what metrics we want
#             'symmetrixId': '000194900728' #symmetrix ID (full 12 digits)
#            }
#          }

#make sure we actually get a value back.
##data = None
#if len(responseObj["iterator"]["resultList"]["result"]) > 0:
#    data = float(responseObj["iterator"]["resultList"]["result"][0]['IO_RATE'])
#    line = 'Symmetrix.System.IO_RATE %d %d' % (data, int(time.time()))
#    print line
#else:
#    print "Short response"
