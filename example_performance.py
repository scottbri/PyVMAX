#!/usr/bin/python

import argparse
import pyvmax
import time

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

vmax_api.rest.printJSON(vmax_api.version)

def generate_payload(symmetrix_id):
    return {
        "startDate": int(time.time()*1000)-(3600*1000), # 60 minutes ago
        "endDate": int(time.time()*1000),               # now
        "symmetrixId": symmetrix_id,
	"dataFormat": "Average",
        "metrics": ["IO_RATE", "PERCENT_HIT", "PERCENT_READ"]
    }

# Get all VMAXs for a given Unisphere Instance
try:
    symmetrix_list_response = vmax_api.get_arrays()

    if 'message' in symmetrix_list_response:
        print symmetrix_list_response.get('message')
        sys.exit(1)
    else:
        # Assuming no messages, store the list of VMAX's into symmetrix_list
        symmetrix_list = symmetrix_list_response["symmetrixId"]
        print("VMAXs found: " + str(symmetrix_list))

except Exception as e:
	sys.exit(1)

# For each VMAX in Unisphere, get the array stats
for symmetrix_id in symmetrix_list:
    perf_response = vmax_api.get_perf_array_metrics(generate_payload(symmetrix_id))
    if 'message' in symmetrix_list_response:
        print symmetrix_list_response.get('message')
    else:
	vmax_api.rest.printJSON(perf_response)

