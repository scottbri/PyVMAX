#!/usr/bin/python

import argparse
import os
import sys
import logging
#sys.path.insert(0, os.path.abspath('..'))

import pyvmax


#################################
### Define and Parse CLI arguments
PARSER = argparse.ArgumentParser(
    description='Example implementation of a Python REST client for EMC Unisphere for VMAX.')
RFLAGS = PARSER.add_argument_group('Required arguments')
RFLAGS.add_argument('-url', required=True, help='Base Unisphere URL. e.g. https://10.0.0.1:8443')
RFLAGS.add_argument('-user', required=True, help='Unisphere username. e.g. smc')
RFLAGS.add_argument('-passwd', required=True, help='Unisphere password. e.g. smc')
ARGS = PARSER.parse_args()

URL = ARGS.url
USER = ARGS.user
PASSWORD = ARGS.passwd
log = logging.getLogger('example.py')

# This is the magical API connection call
# the rest is just figuring out which methods you want to use to gather data
# and parsing the JSON responses to do meaningful work
vmax_api = pyvmax.connect(URL, USER, PASSWORD)

# here's a json printer method you can use to debug the server responses
print(vmax_api.rest.json_to_str(vmax_api.get_version()))

# Instead of printing debugging to the console, use the logger instead
# All log messages go to the log file, and anything warning or above
# also goes to the console... that's why this info worthy log was issued as warning
log.warning(str(vmax_api.api_last_resp_time) + "ms API response time")

# discover the known symmetrix serial #'s
prov_array_ids = vmax_api.get_prov_arrays()['symmetrixId']
log.info(str(vmax_api.api_last_resp_time) + "ms API response time")

# going to build a list of dicts, each one a symmetrix
prov_array_list = list()
for symmId in prov_array_ids:
    # get the array details
    symm_result = vmax_api.get_prov_array(symmId)
    if 'symmetrix' in symm_result:
        symmetrix = symm_result['symmetrix'][0]

    # for this symmetrix, go ahead and build a list of thin pools
    tpList = list()

    # make sure to check whether any list results are returned before iterating
    tp_result = vmax_api.get_prov_array_thinpools(symmId)
    if 'poolId' in tp_result:
        # iterate through the thin pools, get their details and build a list
        for tpId in vmax_api.get_prov_array_thinpools(symmId)['poolId']:
            tp = vmax_api.get_prov_array_thinpool(symmId, tpId)['thinPool'][0]
            tpList.append(tp)

    # add a dict entry for the thin pool list data structure we just created
    symmetrix['thinpools'] = tpList

    prov_array_list.append(symmetrix)

# do something with this great list of thin provisioned arrays like...
# print it out!! (the json printer is good for python lists and dicts too)
print(vmax_api.rest.json_to_str(prov_array_list))

#
# that was Thin Pool arrays (aka VMAX2 and older), now onto VMAX3's
# discover the known slo symmetrix serial #'s
#
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
    if 'srpId' in srp_result:
        for srpId in vmax_api.get_slo_array_srps(symmId)['srpId']:
            srp = vmax_api.get_slo_array_srp(symmId, srpId)
            if 'srp' in srp:
                srpList.append(srp['srp'])

    # add a dict entry for the SRP list data structure we just created
    symmetrix['srp'] = srpList

    # for this symmetrix, go ahead and build a list of Storage Groups
    sgList = list()

    sg_result = vmax_api.get_slo_array_storagegroups(symmId)
    # make sure to check whether any list results returned.. not every array has storage groups!
    if 'storageGroupId' in sg_result:
        # iterate through the sg's, get their details and build a list
        for sgId in sg_result['storageGroupId']:
            sg = vmax_api.get_slo_array_storagegroup(symmId, sgId)
            sgList.append(sg.get('storageGroup', None))

    # add a dict entry for the Storage Group list data structure we just created
    symmetrix['storageGroups'] = sgList

    slo_array_list.append(symmetrix)

# do something with this great list of thin provisioned arrays
# print it out!! (the json printer is good for lists and dicts too)
print(vmax_api.rest.json_to_str(slo_array_list))

# log the # of api calls, total elapsed API wait time, and average time for all calls
log.info(str(vmax_api.api_last_resp_time) + "resp time in ms")
log.info(str(vmax_api.api_counter) + "API calls in this script")
log.info(str(vmax_api.api_timer) + "total accumulated ms waiting on API")
log.info(str(vmax_api.api_average_time()) + "API average response time in ms")
