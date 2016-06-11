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

log = logging.getLogger('example_capacities.py')
vmax_api = pyvmax.connect(URL, USER, PASSWORD)

# discover the known slo symmetrix serial #'s
slo_array_ids = vmax_api.get_slo_arrays()['symmetrixId']
log.info("discovered arrays")

# going to build a list of dicts, each one a symmetrix
slo_array_list = list()
for symm_id in slo_array_ids:
    # get the array details
    log.info("symmetrix loop")
    symm_result = vmax_api.get_slo_array(symm_id)['symmetrix'][0]
    symmetrix = {'symmetrix_id' : symm_result['symmetrixId'],
                 'array_usable_gb' : symm_result['virtualCapacity']['total_capacity_gb'],
                 'srps_total_subscribed_gb' : 0,
                 'srps_total_usable_gb' : 0,
                 'srps_total_allocated_gb' : 0,
                 'srps_total_host_allocated_gb' : 0,
                 'srps_total_dse_gb' : 0,
                 'srps_total_snaps_gb' : 0,
                 'srps_virtual_replica_gb' : 0}
#                'array_raw_gb' : symm_result['physicalCapacity'],

    # for this symmetrix, go ahead and build a list of SRP's
    srp_list = list()
    srps_result = vmax_api.get_slo_array_srps(symm_id)
    if 'srpId' in srps_result:
        for srp_id in vmax_api.get_slo_array_srps(symm_id)['srpId']:
            log.info("srp loop")
            srp_result = vmax_api.get_slo_array_srp(symm_id, srp_id)['srp'][0]
            srp = {'srp_id' : srp_result['srpId'],
                   'srp_usable_cap_gb' : srp_result['total_usable_cap_gb'],
                   'srp_allocated_cap_gb' : srp_result['total_allocated_cap_gb'],
                   'srp_snapshot_allocated_cap_gb' : srp_result['total_snapshot_allocated_cap_gb'],
                   'srp_srdf_dse_allocated_cap_gb' : srp_result['total_srdf_dse_allocated_cap_gb'],
                   'srp_subscribed_cap_gb' : srp_result['total_subscribed_cap_gb'],
                   'srp_host_allocated_cap_gb' : srp_result['total_allocated_cap_gb'] - srp_result['total_snapshot_allocated_cap_gb'] - srp_result['total_srdf_dse_allocated_cap_gb'],
                   'sgs_cap_gb' : 0,
                   'sgs_replica_cap_gb' : 0}

            # for this SRP, build a list of Storage Groups
            sg_list = list()
            # make sure to check whether any sg results returned.. not every SRP has storage groups!
            result_filter = {'srp_name' : srp['srp_id']}
            sgs_result = vmax_api.get_slo_array_storagegroups(symm_id, result_filter)
            if 'storageGroupId' in sgs_result:
                # iterate through the sg's, get their details and build a list
                for sg_id in sgs_result['storageGroupId']:
                    log.info("storagegroup loop")
                    sg_result = vmax_api.get_slo_array_storagegroup(symm_id, sg_id)['storageGroup'][0]
                    sg = {'sg_id' : sg_result['storageGroupId'],
                          'sg_cap_gb' : sg_result['cap_gb'],
                          'num_snapshots' : sg_result['num_of_snapshots'],
                          'sg_replica_cap_gb' : sg_result['cap_gb'] * sg_result['num_of_snapshots']}

                    # before we loop, update parent SRP's calculated values for this sg
                    srp['sgs_cap_gb'] += sg['sg_cap_gb']
                    srp['sgs_replica_cap_gb'] += sg['sg_replica_cap_gb']

                    # append this sg to the running list for this SRP
                    sg_list.append(sg)

            # add a dict entry for the Storage Group list data structure we just created
            srp['storage_groups'] = sg_list

            # before we loop, update parent array's calculated values for this SRP
            symmetrix['srps_total_subscribed_gb'] += srp['srp_subscribed_cap_gb']
            symmetrix['srps_total_usable_gb'] += srp['srp_usable_cap_gb']
            symmetrix['srps_total_allocated_gb'] += srp['srp_allocated_cap_gb']
            symmetrix['srps_total_host_allocated_gb'] += srp['srp_host_allocated_cap_gb']
            symmetrix['srps_total_dse_gb'] += srp['srp_srdf_dse_allocated_cap_gb']
            symmetrix['srps_total_snaps_gb'] += srp['srp_snapshot_allocated_cap_gb']
            symmetrix['srps_virtual_replica_gb'] += srp['sgs_replica_cap_gb']

            # append this SRP to the running list for this array
            srp_list.append(srp)

    # add a dict entry for the SRP list data structure we just created
    symmetrix['srp'] = srp_list

    slo_array_list.append(symmetrix)

# do something with this great list of symmetrix capacities
# print it out!! (the json printer is good for lists and dicts too)
#vmax_api.rest.print_json(slo_array_list)
print("Array Id,Array Usable GB,Array Subscribed GB,Array Total Allocated GB,Array % Used, Array % Subscribed, Host Allocated GB,Snaps Allocated GB,DSE Allocated GB,Virtual Replica GB")
for element in slo_array_list:
    print(element['symmetrix_id'], ",",
          element['array_usable_gb'], ",",
          element['srps_total_subscribed_gb'], ",",
          element['srps_total_allocated_gb'], ",",
          element['srps_total_allocated_gb'] / element['array_usable_gb'], ",",
          element['srps_total_subscribed_gb'] / element['array_usable_gb'], ",",
          element['srps_total_host_allocated_gb'], ",",
          element['srps_total_snaps_gb'], ",",
          element['srps_total_dse_gb'], ",",
          element['srps_virtual_replica_gb'], sep='')
