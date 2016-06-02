#!/usr/bin/python

import argparse
import pyvmax

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

vmax_api = pyvmax.vmax_connect(URL,user,password)

# TODO: Do something based on the version of Unisphere
#unisphereVersion = vmax_api.getVersion(URL)['version']
print vmax_api.version

# discover the known symmetrix serial #'s
symmIdList = vmax_api.getSymms(URL)

# going to build a list of dicts, each one a symmetrix
symmList = list()
for symmId in symmIdList:
    # get the array details
    symmetrix = vmax_api.getSymm(URL, symmId)

    # now gather more details and add them to the array dict

    # examine first two chars of ucode
    if symmetrix['ucode'][:2] == '59':
	    # VMAX3 with SRP and SLO based Provisioning

        # for this symmetrix, go ahead and build a list of SRP's
        srpList = list()
        for srpId in vmax_api.getSrps(URL, symmId):
            srp = vmax_api.getSrp(URL, symmId, srpId)
            srpList.append(srp)

        # add a dict entry for the SRP list data structure we just created
        symmetrix['srp'] = srpList

        # for this symmetrix, go ahead and build a list of Storage Groups
        sgList = list()
        for sgId in vmax_api.getSgList(URL, symmId):
            sg = vmax_api.getSg(URL, symmId, sgId)
            sgList.append(sg)

        # add a dict entry for the Storage Group list data structure we just created
        symmetrix['storageGroup'] = sgList

    else:
        # this is an older Symmetrix with virtual provisioning

        # for this symmetrix, go ahead and build a list of Thin Pools
        tpList = list()
        for tpId in vmax_api.getThinPoolList(URL, symmId):
            tp = vmax_api.getThinPool(URL, symmId, tpId)
            tpList.append(tp)

        # add a dict entry for the SRP list data structure we just created
        symmetrix['thinpool'] = tpList

    # finally add this symmetrix dict data structure to the list of arrays
    symmList.append(symmetrix)

# do something useful with all this data, like print it out ;-)
vmax_api.jsonPrint(symmList)

