
################
## get the version of Unisphere (the API)
################
def getVersion(URL, userId, password):
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
def getSymms(URL, userId, password):
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
def getSymm(URL, symmId, userId, password):
    target_uri = "%s/univmax/restapi/system/symmetrix/%s" % (URL, symmId)
    responseKey = 'symmetrix'
    responseObj = jsonGet(target_uri, user, password)
    if responseKey in responseObj:
        return responseObj[responseKey][0]
    else:
        return dict()


def getSloSymms(URL, userId, password):
    target_uri = "%s/univmax/restapi/sloprovisioning/symmetrix" % (URL)
    responseKey = 'symmetrixId'
    responseObj = jsonGet(target_uri, user, password)
    if responseKey in responseObj:
        return responseObj[responseKey]
    else:
        return dict()

def getSloSymm(URL, symmId, userId, password):
    target_uri = "%s/univmax/restapi/sloprovisioning/symmetrix/%s" % (URL, symmId)
    responseKey = 'symmetrix'
    responseObj = jsonGet(target_uri, user, password)
    if responseKey in responseObj:
        return responseObj[responseKey][0]
    else:
        return dict()

def getSloDirectors(URL, symmId, userId, password):
    target_uri = "%s/univmax/restapi/sloprovisioning/symmetrix/%s/director" % (URL, symmId)
    responseKey = 'directorId'
    responseObj = jsonGet(target_uri, user, password)
    if responseKey in responseObj:
        return responseObj[responseKey]
    else:
        return dict()

def getSloDirector(URL, symmId, directorId, userId, password):
    target_uri = "%s/univmax/restapi/sloprovisioning/symmetrix/%s/director/%s" % (URL, symmId, directorId)
    responseKey = 'director'
    responseObj = jsonGet(target_uri, user, password)
    if responseKey in responseObj:
        return responseObj[responseKey][0]
    else:
        return dict()

def getSloPorts(URL, symmId, directorId, userId, password):
    target_uri = "%s/univmax/restapi/sloprovisioning/symmetrix/%s/director/%s/port" % (URL, symmId, directorId)
    responseKey = 'symmetrixPortKey'
    responseObj = jsonGet(target_uri, user, password)
    if responseKey in responseObj:
        return responseObj[responseKey]
    else:
        return dict()

def getSloPort(URL, symmId, directorId, portId, userId, password):
    target_uri = "%s/univmax/restapi/sloprovisioning/symmetrix/%s/director/%s/port/%s" % (URL, symmId, directorId, portId)
    responseKey = 'symmetrixPort'
    responseObj = jsonGet(target_uri, user, password)
    if responseKey in responseObj:
        return responseObj[responseKey][0]
    else:
        return dict()

def getSloHosts(URL, symmId, userId, password):
    target_uri = "%s/univmax/restapi/sloprovisioning/symmetrix/%s/host" % (URL, symmId)
    responseKey = 'hostId'
    responseObj = jsonGet(target_uri, user, password)
    if responseKey in responseObj:
        return responseObj[responseKey]
    else:
        return dict()

def getSloHost(URL, symmId, hostId, userId, password):
    target_uri = "%s/univmax/restapi/sloprovisioning/symmetrix/%s/host/%s" % (URL, symmId, hostId)
    responseKey = 'host'
    responseObj = jsonGet(target_uri, user, password)
    if responseKey in responseObj:
        return responseObj[responseKey][0]
    else:
        return dict()

def getSloHostgrps(URL, symmId, userId, password):
    target_uri = "%s/univmax/restapi/sloprovisioning/symmetrix/%s/hostgroup" % (URL, symmId)
    responseKey = 'hostGroupId'
    responseObj = jsonGet(target_uri, user, password)
    if responseKey in responseObj:
        return responseObj[responseKey]
    else:
        return dict()

def getSloHostgrp(URL, symmId, grpId, userId, password):
    target_uri = "%s/univmax/restapi/sloprovisioning/symmetrix/%s/hostgroup/%s" % (URL, symmId, grpId)
    responseKey = 'hostGroup'
    responseObj = jsonGet(target_uri, user, password)
    if responseKey in responseObj:
        return responseObj[responseKey][0]
    else:
        return dict()

def getSloInitiators(URL, symmId, userId, password):
    target_uri = "%s/univmax/restapi/sloprovisioning/symmetrix/%s/initiator" % (URL, symmId)
    responseKey = 'initiatorId'
    responseObj = jsonGet(target_uri, user, password)
    if responseKey in responseObj:
        return responseObj[responseKey]
    else:
        return dict()

def getSloInitator(URL, symmId, initiatorId, userId, password):
    target_uri = "%s/univmax/restapi/sloprovisioning/symmetrix/%s/initiator/%s" % (URL, symmId, initatorId)
    responseKey = 'initiator'
    responseObj = jsonGet(target_uri, user, password)
    if responseKey in responseObj:
        return responseObj[responseKey][0]
    else:
        return dict()

def getSloMaskingviews(URL, symmId, userId, password):
    target_uri = "%s/univmax/restapi/sloprovisioning/symmetrix/%s/maskingview" % (URL, symmId)
    responseKey = 'maskingViewId'
    responseObj = jsonGet(target_uri, user, password)
    if responseKey in responseObj:
        return responseObj[responseKey]
    else:
        return dict()

def getSloMaskingview(URL, symmId, mvId, userId, password):
    target_uri = "%s/univmax/restapi/sloprovisioning/symmetrix/%s/maskingview/%s" % (URL, symmId, mvId)
    responseKey = 'maskingView'
    responseObj = jsonGet(target_uri, user, password)
    if responseKey in responseObj:
        return responseObj[responseKey][0]
    else:
        return dict()

def getSloMvConnections(URL, symmId, mvId, userId, password):
    target_uri = "%s/univmax/restapi/sloprovisioning/symmetrix/%s/maskingview/%s/connections" % (URL, symmId, mvId)
    responseKey = 'maskingViewConnection'
    responseObj = jsonGet(target_uri, user, password)
    if responseKey in responseObj:
        return responseObj[responseKey]
    else:
        return dict()

def getSloPorts(URL, symmId, userId, password):
    target_uri = "%s/univmax/restapi/sloprovisioning/symmetrix/%s/port" % (URL, symmId)
    responseKey = 'symmetrixPortKey'
    responseObj = jsonGet(target_uri, user, password)
    if responseKey in responseObj:
        return responseObj[responseKey]
    else:
        return dict()

def getSloPortgrps(URL, symmId, userId, password):
    target_uri = "%s/univmax/restapi/sloprovisioning/symmetrix/%s/portgroup" % (URL, symmId)
    responseKey = 'portGroupId'
    responseObj = jsonGet(target_uri, user, password)
    if responseKey in responseObj:
        return responseObj[responseKey]
    else:
        return dict()

def getSloPortgrp(URL, symmId, pgId, userId, password):
    target_uri = "%s/univmax/restapi/sloprovisioning/symmetrix/%s/portgroup/%s" % (URL, symmId, pgId)
    responseKey = 'portGroup'
    responseObj = jsonGet(target_uri, user, password)
    if responseKey in responseObj:
        return responseObj[responseKey][0]
    else:
        return dict()

def getSlos(URL, symmId, userId, password):
    target_uri = "%s/univmax/restapi/sloprovisioning/symmetrix/%s/slo" % (URL, symmId)
    responseKey = 'sloId'
    responseObj = jsonGet(target_uri, user, password)
    if responseKey in responseObj:
        return responseObj[responseKey]
    else:
        return dict()

def getSlo(URL, symmId, sloId, userId, password):
    target_uri = "%s/univmax/restapi/sloprovisioning/symmetrix/%s/slo/%s" % (URL, symmId, sloId)
    responseKey = 'slo'
    responseObj = jsonGet(target_uri, user, password)
    if responseKey in responseObj:
        return responseObj[responseKey][0]
    else:
        return dict()

def getSrps(URL, symmId, userId, password):
    target_uri = "%s/univmax/restapi/sloprovisioning/symmetrix/%s/srp" % (URL, symmId)
    responseKey = 'srpId'
    responseObj = jsonGet(target_uri, user, password)
    if responseKey in responseObj:
        return responseObj[responseKey]
    else:
        return dict()

def getSrp(URL, symmId, srpId, userId, password):
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
def getSgList(URL, symmId, userId, password):
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
def getSg(URL, symmId, sgId, userId, password):
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
def getThinPoolList(URL, symmId, userId, password):
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
def getThinPool(URL, symmId, tpId, userId, password):
    target_uri = "%s/univmax/restapi/provisioning/symmetrix/%s/thinpool/%s" % (URL, symmId, tpId)
    responseKey = 'poolId'
    responseObj = jsonGet(target_uri, user, password)
    if responseKey in responseObj:
        return responseObj[responseKey][0]
    else:
        return dict()

