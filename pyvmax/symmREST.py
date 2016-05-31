#!/usr/bin/python

import argparse
from symmRestApi import Restful

#################################

### Define and Parse CLI arguments
parser = argparse.ArgumentParser(description='Example implementation of a Python REST client for EMC Unisphere for VMAX.')
rflags = parser.add_argument_group('Required arguments')
rflags.add_argument('-url',         required=True, help='Base Unisphere URL. e.g. https://10.0.0.1:8443')
rflags.add_argument('-user',        required=True, help='Unisphere username. e.g. smc')
rflags.add_argument('-passwd',      required=True, help='Unisphere password. e.g. smc')
args = parser.parse_args()

URL = args.url
user = args.user
password = args.passwd

api = Restful(URL,user,password)

# TODO: Do something based on the version of Unisphere
unisphereVersion = api.getVersion(URL)['version']

# discover the known symmetrix serial #'s
symmIdList = api.getSymms(URL)

# going to build a list of dicts, each one a symmetrix
symmList = list()
for symmId in symmIdList:
    # get the array details
    symmetrix = api.getSymm(URL, symmId)

    # now gather more details and add them to the array dict

    # examine first two chars of ucode
    if symmetrix['ucode'][:2] == '59':
	    # VMAX3 with SRP and SLO based Provisioning

        # for this symmetrix, go ahead and build a list of SRP's
        srpList = list()
        for srpId in api.getSrps(URL, symmId):
            srp = api.getSrp(URL, symmId, srpId)
            srpList.append(srp)

        # add a dict entry for the SRP list data structure we just created
        symmetrix['srp'] = srpList

        # for this symmetrix, go ahead and build a list of Storage Groups
        sgList = list()
        for sgId in api.getSgList(URL, symmId):
            sg = api.getSg(URL, symmId, sgId)
            sgList.append(sg)

        # add a dict entry for the Storage Group list data structure we just created
        symmetrix['storageGroup'] = sgList

    else:
        # this is an older Symmetrix with virtual provisioning

        # for this symmetrix, go ahead and build a list of Thin Pools
        tpList = list()
        for tpId in api.getThinPoolList(URL, symmId):
            tp = api.getThinPool(URL, symmId, tpId)
            tpList.append(tp)

        # add a dict entry for the SRP list data structure we just created
        symmetrix['thinpool'] = tpList

    # finally add this symmetrix dict data structure to the list of arrays
    symmList.append(symmetrix)

# do something useful with all this data, like print it out ;-)
api.jsonPrint(symmList)


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
