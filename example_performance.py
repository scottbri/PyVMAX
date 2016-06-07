#!/usr/bin/python

import argparse
import datetime
import time
import pprint

import pyvmax
#################################
### Define and Parse CLI arguments
PARSER = argparse.ArgumentParser(description='Example implementation of a Python REST client for EMC Unisphere for VMAX performance statistics.')
RFLAGS = PARSER.add_argument_group('Required arguments')
RFLAGS.add_argument('-url', required=True, help='Base Unisphere URL. e.g. https://10.0.0.1:8443')
RFLAGS.add_argument('-user', required=True, help='Unisphere username. e.g. smc')
RFLAGS.add_argument('-passwd', required=True, help='Unisphere password. e.g. smc')
ARGS = PARSER.parse_args()

URL = ARGS.url
USER = ARGS.user
PASSWORD = ARGS.passwd

vmax_api = pyvmax.connect(URL, USER, PASSWORD)

vmax_api.rest.print_json(vmax_api.version)

def time_now():
    return int(time.time() * 1000)

def time_hours_ago(hours=1):
    return int(time_now() - (hours * 3600 * 1000))

def time_days_ago(days=1):
    return int(time_now() - (days * 24 * 3600 * 1000))

def time_weeks_ago(weeks=1):
    return int(time_now() - (weeks * 7 * 24 * 3600 * 1000))

def time_last_midnight():
    today = datetime.date.today()
    return int(time.mktime(today.timetuple()) * 1000)

def time_midnights_ago(midnight=1):
    return int(time_last_midnight() - (midnights * 24 * 3600 * 1000))

def generate_payload(symmetrix_id):
    return {
        "startDate": time_midnights_ago(1),     # 60 minutes ago
        "endDate": time_last_midnight(),              # now
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
        vmax_api.rest.print_json(perf_response)
