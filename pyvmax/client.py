import requests, json, pprint, time, socket

# Disable warnings from untrusted server certificates
try:
    from requests.packages.urllib3.exceptions import InsecureRequestWarning
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
except Exception:
    print("Ignore messages related to insecure SSL certificates")


class UnisphereClient(object):

    def __init__(self, base_url, username, passwd, verifySSL=False):

        self.url = "%s/univmax/restapi" % (base_url)
        self.user = username
        self.password = passwd
        self.verify_SSL = verifySSL
        self.version = self.getVersion()

        # set the headers for how we want the response
        self.headers = {'content-type': 'application/json','accept':'application/json'}

    ################
    ## make the json GET call to the public api
    ################
    def get(self, targetUrl):

        #make the actual request, specifying the URL, the JSON from above, standard basic auth, the headers and not to verify the SSL cert.
        #r = requests.post(target_uri, requestJSON, auth=('smc', 'smc'), headers=headers, verify=False)
        try:
            r = requests.get(targetUrl, auth=(self.user, self.password), headers=self.headers, verify=self.verify_SSL)
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

            print(responseObj.get("message", "API failed to return expected result"))
            self.jsonPrint(responseObj)
            return dict()

        return responseObj

    ################
    ## make the json POST call to the public api
    ################
    def post(self, targetUrl, requestObj=None):

        #turn this into a JSON string
        requestJSON = json.dumps(requestObj, sort_keys=True, indent=4)
        #print(requestJSON)

        #make the actual request, specifying the URL, the JSON from above, standard basic auth, the headers and not to verify the SSL cert.
        try:
            r = requests.post(targetUrl, requestJSON, auth=(self.user, self.password), headers=self.headers, verify=verify_ssl)
        except:
            print("Exception:  Can't connect to API server URL:  " + targetUrl)
            print("Exiting")
            exit(1)

        #take the raw response text and deserialize it into a python object.
        try:
            response = json.loads(r.text)
        except:
            print("Exception")
            print(r.text)
        #self.jsonPrint(responseObj)
        return response


    ################
    ## make the json PUT call to the public api
    ################
    def put(self, targetUrl, requestObj=None):

        #turn this into a JSON string
        requestJSON = json.dumps(requestObj, sort_keys=True, indent=4)
        #print(requestJSON)

        #make the actual request, specifying the URL, the JSON from above, standard basic auth, the headers and not to verify the SSL cert.
        try:
            r = requests.put(targetUrl, requestJSON, auth=(self.user, self.password), headers=self.headers, verify=self.verify_ssl)
        except:
            print("Exception:  Can't connect to API server URL:  " + targetUrl)
            print("Exiting")
            exit(1)

        #take the raw response text and deserialize it into a python object.
        try:
            response = json.loads(r.text)
        except:
            print("Exception")
            print(r.text)
        #self.jsonPrint(responseObj)
        return response


    ################
    ## make the json DELETE call to the public api
    ################
    def delete(self, targetUrl, requestObj=None):

        #turn this into a JSON string
        requestJSON = json.dumps(requestObj, sort_keys=True, indent=4)
        #print(requestJSON)

        #make the actual request, specifying the URL, the JSON from above, standard basic auth, the headers and not to verify the SSL cert.
        try:
            r = requests.delete(targetUrl, requestJSON, auth=(self.user, self.password), headers=self.headers, verify=self.verify_ssl)
        except:
            print("Exception:  Can't connect to API server URL:  " + targetUrl)
            print("Exiting")
            exit(1)

        #take the raw response text and deserialize it into a python object.
        try:
            response = json.loads(r.text)
        except:
            print("Exception")
            print(r.text)
        #self.jsonPrint(responseObj)
        return response


    ################
    ## print a json object nicely
    ################
    def printJSON(self, jsonObj):
    	print(json.dumps(jsonObj, sort_keys=False, indent=2))


    #################################################################
    ## Methods to implement Unisphere REST API
    #################################################################

    ######################################
    ## ADMINISTRATION Resource group
    ######################################

    ################
    ## get a list of all applications registered with the server
    ################
    def getApps(self):
        target_uri = "%s/common/Application/list" % (self.url)
        return self.get(target_uri)

    ################
    ## get a list of sharding info
    ################
    def getShards(self):
        target_uri = "%s/common/Sharding/info" % (self.url)
        return self.get(target_uri)

    ######################################
    ## COMMON Resource group
    ######################################

    ######################################
    ## MANAGEMENT Resource group
    ######################################

    ################
    ## get a dump of unisphere server runtime stats
    ################
    def getUsageStats(self):
        target_uri = "%s/management/RuntimeUsage/read" % (self.url)
        return self.get(target_uri)

    ######################################
    ## PERFORMANCE Resource group
    ######################################

    ######################################
    ## PROVISIONING Resource group
    ######################################

    ################
    ## queries for a list of Authorized Symmetrix Ids compatible with provisioning
    ################
    def getProvisionableSymms(self):
        target_uri = "%s/provisioning/symmetrix" % (self.url)
        return self.get(target_uri)

    ################
    ## queries for a specific Authorized Symmetrix using its ID and compatible with provisioning
    ################
    def getProvisionableSymm(self, resourceId):
        target_uri = "%s/provisioning/symmetrix/%s" % (self.url, resourceId)
        return self.get(target_uri)

    ################
    ## get a list of Thin Pools on a given Symmetrix
    ################
    def getThinPoolList(self, resourceId):
        target_uri = "%s/provisioning/symmetrix/%s/thinpool" % (self.url, resourceId)
        return self.get(target_uri)

    ################
    ## get the details of a particular Thin Pool
    ################
    def getThinPool(self, symmId, tpId):
        target_uri = "%s/provisioning/symmetrix/%s/thinpool/%s" % (self.url, symmId, tpId)
        return self.get(target_uri)

    ######################################
    ## REPLICATION Resource group
    ######################################


    ######################################
    ## SLO PROVISIONING Resource group
    ######################################

    def getSloSymms(self):
        target_uri = "%s/sloprovisioning/symmetrix" % (self.url)
        return self.get(target_uri)

    def getSloSymm(self, resourceId):
        target_uri = "%s/sloprovisioning/symmetrix/%s" % (self.url, resourceId)
        return self.get(target_uri)

    def getSloDirectors(self, resourceId):
        target_uri = "%s/sloprovisioning/symmetrix/%s/director" % (self.url, resourceId)
        return self.get(target_uri)

    def getSloDirector(self, symmId, resourceId):
        target_uri = "%s/sloprovisioning/symmetrix/%s/director/%s" % (self.url, symmId, resourceId)
        return self.get(target_uri)

    def getSloPorts(self, symmId, resourceId):
        target_uri = "%s/sloprovisioning/symmetrix/%s/director/%s/port" % (self.url, symmId, resourceId)
        return self.get(target_uri)

    def getSloPort(self, symmId, directorId, portId):
        target_uri = "%s/sloprovisioning/symmetrix/%s/director/%s/port/%s" % (self.url, symmId, directorId, portId)
        return self.get(target_uri)

    def getSloHosts(self, resourceId):
        target_uri = "%s/sloprovisioning/symmetrix/%s/host" % (self.url, resourceId)
        return self.get(target_uri)

    def getSloHost(self, symmId, hostId):
        target_uri = "%s/sloprovisioning/symmetrix/%s/host/%s" % (self.url, symmId, hostId)
        return self.get(target_uri)

    def getSloHostgrps(self, resourceId):
        target_uri = "%s/sloprovisioning/symmetrix/%s/hostgroup" % (self.url, resourceId)
        return self.get(target_uri)

    def getSloHostgrp(self, symmId, grpId):
        target_uri = "%s/sloprovisioning/symmetrix/%s/hostgroup/%s" % (self.url, symmId, grpId)
        return self.get(target_uri)

    def getSloInitiators(self, resourceId):
        target_uri = "%s/sloprovisioning/symmetrix/%s/initiator" % (self.url, resourceId)
        return self.get(target_uri)

    def getSloInitator(self, symmId, initiatorId):
        target_uri = "%s/sloprovisioning/symmetrix/%s/initiator/%s" % (self.url, symmId, initatorId)
        return self.get(target_uri)

    def getSloMaskingviews(self, resourceId):
        target_uri = "%s/sloprovisioning/symmetrix/%s/maskingview" % (self.url, resourceId)
        return self.get(target_uri)

    def getSloMaskingview(self, symmId, mvId):
        target_uri = "%s/sloprovisioning/symmetrix/%s/maskingview/%s" % (self.url, symmId, mvId)
        return self.get(target_uri)

    def getSloMvConnections(self, symmId, mvId):
        target_uri = "%s/sloprovisioning/symmetrix/%s/maskingview/%s/connections" % (self.url, symmId, mvId)
        return self.get(target_uri)

    def getSloPorts(self, resourceId):
        target_uri = "%s/sloprovisioning/symmetrix/%s/port" % (self.url, resourceId)
        return self.get(target_uri)

    def getSloPortgrps(self, resourceId):
        target_uri = "%s/sloprovisioning/symmetrix/%s/portgroup" % (self.url, resourceId)
        return self.get(target_uri)

    def getSloPortgrp(self, symmId, pgId):
        target_uri = "%s/sloprovisioning/symmetrix/%s/portgroup/%s" % (self.url, symmId, pgId)
        return self.get(target_uri)

    def getSlos(self, resourceId):
        target_uri = "%s/sloprovisioning/symmetrix/%s/slo" % (self.url, resourceId)
        return self.get(target_uri)

    def getSlo(self, symmId, sloId):
        target_uri = "%s/sloprovisioning/symmetrix/%s/slo/%s" % (self.url, symmId, sloId)
        return self.get(target_uri)

    def getSrps(self, resourceId):
        target_uri = "%s/sloprovisioning/symmetrix/%s/srp" % (self.url, resourceId)
        return self.get(target_uri)

    def getSrp(self, symmId, srpId):
        target_uri = "%s/sloprovisioning/symmetrix/%s/srp/%s" % (self.url, symmId, srpId)
        return self.get(target_uri)

    ################
    ## get a list of Storage Groups on a given SLO Symmetrix
    ################
    def getSgList(self, resourceId):
        target_uri = "%s/sloprovisioning/symmetrix/%s/storagegroup" % (self.url, resourceId)
        return self.get(target_uri)

    ################
    ## get the details of a particular SLO managed Storage Group
    ################
    def getSg(self, symmId, sgId):
        target_uri = "%s/sloprovisioning/symmetrix/%s/storagegroup/%s" % (self.url, symmId, sgId)
        return self.get(target_uri)


    ######################################
    ## SYSTEM Resource group
    ######################################

    ################
    ## get a list of All Alert ids across all symmetrix arrays
    ################
    def getAlerts(self):
        target_uri = "%s/system/alert" % (self.url)
        return self.get(target_uri)

    ################
    ## queries for a specified Alert
    ################
    def getAlert(self, resourceId):
        target_uri = "%s/system/alert/%s" % (self.url, resourceId)
        return self.get(target_uri)

    ################
    ## queries for a list of Job ids across all symmetrix arrays
    ################
    def getJobs(self):
        target_uri = "%s/system/job" % (self.url)
        return self.get(target_uri)

    ################
    ## queries for a specified job
    ################
    def getJob(self, resourceId):
        target_uri = "%s/system/job/%s" % (self.url, resourceId)
        return self.get(target_uri)

    ################
    ## get a list of symmetrix serial #'s known by Unisphere
    ################
    def getSymms(self):
        target_uri = "%s/system/symmetrix" % (self.url)
        return self.get(target_uri)

    ################
    ## This call queries for a specific Authorized Symmetrix Object that is compatible with slo provisioning using its ID
    ################
    def getSymm(self, resourceId):
        target_uri = "%s/system/symmetrix/%s" % (self.url, resourceId)
        return self.get(target_uri)

    ################
    ## get a list of All Alert ids for a specific array id
    ################
    def getSymmAlerts(self, resourceId):
        target_uri = "%s/system/symmetrix/%s/alert" % (self.url, resourceId)
        return self.get(target_uri)

    ################
    ## queries for a specified Alert on a specified array
    ################
    def getSymmAlert(self, symId, alertId):
        target_uri = "%s/system/symmetrix/%s/alert/%s" % (self.url, symId, alertId)
        return self.get(target_uri)

    ################
    ## queries for a list of Job ids on a specified array
    ################
    def getSymmJobs(self, resourceId):
        target_uri = "%s/system/symmetrix/%s/job" % (self.url, resourceId)
        return self.get(target_uri)

    ################
    ## queries for a specified job on a specified array
    ################
    def getSymmJob(self, symId, jobId):
        target_uri = "%s/system/symmetrix/%s/job/%s" % (self.url, symId, jobId)
        return self.get(target_uri)

    ################
    ## get the version of Unisphere (the API)
    ################
    def getVersion(self):
        target_uri = "%s/system/version" % (self.url)
        return self.get(target_uri)

    ######################################
    ## WORKLOAD Resource group
    ######################################

