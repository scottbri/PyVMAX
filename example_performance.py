#!/usr/bin/python

import argparse
import time
import pprint

import pyvmax
#################################
### Define and Parse CLI arguments
PARSER = argparse.ArgumentParser(description='Example implementation of a Python REST client for EMC Unisphere for VMAX.')
RFLAGS = PARSER.add_argument_group('Required arguments')
RFLAGS.add_argument('-url', required=True, help='Base Unisphere URL. e.g. https://10.0.0.1:8443')
RFLAGS.add_argument('-user', required=True, help='Unisphere username. e.g. smc')
RFLAGS.add_argument('-passwd', required=True, help='Unisphere password. e.g. smc')
ARGS = PARSER.parse_args()

URL = ARGS.url
USER = ARGS.user
PASSWORD = ARGS.passwd

vmax_api = pyvmax.connect(URL, USER, PASSWORD)

pprint.pprint(vmax_api.version)


def generate_payload(symmetrix_id):
    return {
        "startDate": int(time.time()*1000)-(3600*1000),  # 60 minutes ago
        "endDate": int(time.time()*1000),                # now
        "symmetrixId": symmetrix_id,
        "dataFormat": "Average",
        "metrics": ["IO_RATE", "PERCENT_HIT", "PERCENT_READ"]
    }

# Get all VMAXs for a given Unisphere Instance
try:
    symmetrix_list_response = vmax_api.get_arrays()

    if 'message' in symmetrix_list_response:
        print(symmetrix_list_response.get('message'))
        exit(1)
    else:
        # Assuming no messages, store the list of VMAX's into symmetrix_list
        symmetrix_list = symmetrix_list_response["symmetrixId"]
        print("VMAXs found: " + str(symmetrix_list))

except Exception:
    exit(1)

# For each VMAX in Unisphere, get the array stats
for symm_id in symmetrix_list:
    perf_response = vmax_api.get_perf_array_metrics(generate_payload(symm_id))
    if 'message' in symmetrix_list_response:
        print(symmetrix_list_response.get('message'))
    else:
        pprint.pprint(perf_response)
