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

vmax_api = pyvmax.connect(URL,user,password)

# TODO: Do something based on the version of Unisphere
#unisphereVersion = vmax_api.getVersion(URL)['version']
vmax_api.rest.printJSON(vmax_api.version)


# discover the known symmetrix serial #'s
prov_array_ids = vmax_api.get_prov_arrays()['symmetrixId']

# going to build a list of dicts, each one a symmetrix
prov_array_list = list()
for symmId in prov_array_ids:
    # get the array details
    symmetrix = vmax_api.get_prov_array(symmId)['symmetrix'][0]

    # for this symmetrix, go ahead and build a list of thin pools
    tpList = list()

    # make sure to check whether any list results returned..
    tp_result = vmax_api.get_prov_array_thinpools(symmId)
    if tp_result.has_key('poolId'):
        # iterate through the thin pools, get their details and build a list
        for tpId in vmax_api.get_prov_array_thinpools(symmId)['poolId']:
            tp = vmax_api.get_prov_array_thinpool(symmId, tpId)['thinPool'][0]
            tpList.append(tp)

    # add a dict entry for the thin pool list data structure we just created
    symmetrix['thinpools'] = tpList

    prov_array_list.append(symmetrix)

# do something with this great list of thin provisioned arrays
# print it out!! (the json printer is good for lists and dicts too)
vmax_api.rest.printJSON(prov_array_list)


# discover the known slo symmetrix serial #'s
slo_array_ids = vmax_api.get_slo_arrays()['symmetrixId']

# going to build a list of dicts, each one a symmetrix
slo_array_list = list()
for symmId in slo_array_ids:
    # get the array details
    symmetrix = vmax_api.get_slo_array(symmId)['symmetrix'][0]
    # now gather more details and add them to the array dict

    # for this symmetrix, go ahead and build a list of SRP's
    srpList = list()
    srp_result = vmax_api.get_slo_array_srps(symmId)
    if srp_result.has_key('srpId'):
        for srpId in vmax_api.get_slo_array_srps(symmId)['srpId']:
            srp = vmax_api.get_slo_array_srp(symmId, srpId)['srp']
            srpList.append(srp)

    # add a dict entry for the SRP list data structure we just created
    symmetrix['srp'] = srpList

    # for this symmetrix, go ahead and build a list of Storage Groups
    sgList = list()

    # make sure to check whether any list results returned.. not every array has storage groups!
    sg_result = vmax_api.get_slo_array_storagegroups(symmId)
    if sg_result.has_key('storageGroupId'):
        # iterate through the sg's, get their details and build a list
        for sgId in sg_result['storageGroupId']:
            sg = vmax_api.get_slo_array_storagegroup(symmId, sgId)['storageGroup']
            sgList.append(sg)

    # add a dict entry for the Storage Group list data structure we just created
    symmetrix['storageGroups'] = sgList

    slo_array_list.append(symmetrix)

# do something with this great list of thin provisioned arrays
# print it out!! (the json printer is good for lists and dicts too)
vmax_api.rest.printJSON(slo_array_list)
