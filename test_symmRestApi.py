#!/usr/bin/python

import pytest
from symmRestApi import Restful

######################################
## COMMON Resource group
######################################

######################################
## MANAGEMENT Resource group
######################################

def test_management(variables):
    # in the following, 'resource_id' or similar string is a valid type string but
    # will never be successfully found by the api
    api = Restful(variables['URL'], variables['user'], variables['pass'])

    assert isinstance(api.get_usage_stats(variables['URL']), list)

######################################
## PERFORMANCE Resource group
######################################

######################################
## SLOPROVISIONING and PROVISIONING Resource groups
######################################

def test_provisioning(variables):
    # in the following, 'resource_id' or similar string is a valid type string but
    # will never be successfully found by the api
    api = Restful(variables['URL'], variables['user'], variables['pass'])

    assert isinstance(api.get_arrays(variables['URL']), 'SLO', list)
    assert isinstance(api.get_array_directors(variables['URL'], 'SLO', 'array_id'), list)
    assert isinstance(api.get_array_director(variables['URL'], 'SLO', 'array_id', 'director_id'), dict)
    assert isinstance(api.get_array_director_ports(variables['URL'], 'SLO', 'array_id', 'director_id'), list)
    assert isinstance(api.get_array_director_port(variables['URL'], 'SLO', 'array_id', 'director_id', 'port_id'), dict)
    assert isinstance(api.get_array_fastpolicies(variables['URL'], 'SLO', 'array_id'), list)
    assert isinstance(api.get_array_fastpolicy(variables['URL'], 'SLO', 'array_id', 'policy_id'), dict)
    assert isinstance(api.get_array_hosts(variables['URL'], 'SLO', 'array_id'), list)
    assert isinstance(api.get_array_host(variables['URL'], 'SLO', 'array_id', 'host_id'), dict)
    assert isinstance(api.get_array_hostgroups(variables['URL'], 'SLO', 'array_id'), list)
    assert isinstance(api.get_array_hostgroup(variables['URL'], 'SLO', 'array_id', 'hostgroup_id'), dict)
    assert isinstance(api.get_array_initiators(variables['URL'], 'SLO', 'array_id'), list)
    assert isinstance(api.get_array_initiator(variables['URL'], 'SLO', 'array_id', 'initiator_id'), dict)
    assert isinstance(api.get_array_maskingviews(variables['URL'], 'SLO', 'array_id'), list)
    assert isinstance(api.get_array_maskingview(variables['URL'], 'SLO', 'array_id', 'maskingview_id'), dict)
    assert isinstance(api.get_array_maskingview_connections(variables['URL'], 'SLO', 'array_id'), list)
    assert isinstance(api.get_array_ports(variables['URL'], 'SLO', 'array_id'), list)
    assert isinstance(api.get_array_portgoups(variables['URL'], 'SLO', 'array_id'), list)
    assert isinstance(api.get_array_portgroup(variables['URL'], 'SLO', 'array_id', 'portgroup_id'), dict)
    assert isinstance(api.get_array_slos(variables['URL'], 'SLO', 'array_id'), list)
    assert isinstance(api.get_array_slo(variables['URL'], 'SLO', 'array_id', 'slo_id'), dict)
    assert isinstance(api.get_array_srps(variables['URL'], 'SLO', 'array_id'), list)
    assert isinstance(api.get_array_srp(variables['URL'], 'SLO', 'array_id', 'srp_id'), dict)
    assert isinstance(api.get_array_storagegroups(variables['URL'], 'SLO', 'array_id'), list)
    assert isinstance(api.get_array_storagegroup(variables['URL'], 'SLO', 'array_id', 'storagegroup_id'), dict)
    assert isinstance(api.get_array_volumes(variables['URL'], 'SLO', 'array_id'), list)

    assert isinstance(api.get_arrays(variables['URL']), 'NOTSLO', list)
    assert isinstance(api.get_array_directors(variables['URL'], 'NOTSLO', 'array_id'), list)
    assert isinstance(api.get_array_director(variables['URL'], 'NOTSLO', 'array_id', 'director_id'), dict)
    assert isinstance(api.get_array_director_ports(variables['URL'], 'NOTSLO', 'array_id', 'director_id'), list)
    assert isinstance(api.get_array_director_port(variables['URL'], 'NOTSLO', 'array_id', 'director_id', 'port_id'), dict)
    assert isinstance(api.get_array_fastpolicies(variables['URL'], 'NOTSLO', 'array_id'), list)
    assert isinstance(api.get_array_fastpolicy(variables['URL'], 'NOTSLO', 'array_id', 'policy_id'), dict)
    assert isinstance(api.get_array_hosts(variables['URL'], 'NOTSLO', 'array_id'), list)
    assert isinstance(api.get_array_host(variables['URL'], 'NOTSLO', 'array_id', 'host_id'), dict)
    assert isinstance(api.get_array_hostgroups(variables['URL'], 'NOTSLO', 'array_id'), list)
    assert isinstance(api.get_array_hostgroup(variables['URL'], 'NOTSLO', 'array_id', 'hostgroup_id'), dict)
    assert isinstance(api.get_array_initiators(variables['URL'], 'NOTSLO', 'array_id'), list)
    assert isinstance(api.get_array_initiator(variables['URL'], 'NOTSLO', 'array_id', 'initiator_id'), dict)
    assert isinstance(api.get_array_maskingviews(variables['URL'], 'NOTSLO', 'array_id'), list)
    assert isinstance(api.get_array_maskingview(variables['URL'], 'NOTSLO', 'array_id', 'maskingview_id'), dict)
    assert isinstance(api.get_array_maskingview_connections(variables['URL'], 'NOTSLO', 'array_id'), list)
    assert isinstance(api.get_array_ports(variables['URL'], 'NOTSLO', 'array_id'), list)
    assert isinstance(api.get_array_portgoups(variables['URL'], 'NOTSLO', 'array_id'), list)
    assert isinstance(api.get_array_portgroup(variables['URL'], 'NOTSLO', 'array_id', 'portgroup_id'), dict)
    assert isinstance(api.get_array_storagegroups(variables['URL'], 'NOTSLO', 'array_id'), list)
    assert isinstance(api.get_array_storagegroup(variables['URL'], 'NOTSLO', 'array_id', 'storagegroup_id'), dict)
    assert isinstance(api.get_array_thinpools(variables['URL'], 'NOTSLO', 'array_id'), list)
    assert isinstance(api.get_array_thinpool(variables['URL'], 'NOTSLO', 'array_id', 'thinpool_id'), dict)
    assert isinstance(api.get_array_tiers(variables['URL'], 'NOTSLO', 'array_id'), list)
    assert isinstance(api.get_array_tier(variables['URL'], 'NOTSLO', 'array_id', 'tier_id'), dict)
    assert isinstance(api.get_array_volumes(variables['URL'], 'NOTSLO', 'array_id'), list)
    assert isinstance(api.get_array_volume(variables['URL'], 'NOTSLO', 'array_id', 'volume_id'), dict)


######################################
## REPLICATION Resource group
######################################
def test_replication(variables):
    # in the following, 'resource_id' or similar string is a valid type string but
    # will never be successfully found by the api
    api = Restful(variables['URL'], variables['user'], variables['pass'])

    assert isinstance(api.get_replica_abilities(variables['URL']), list)
    assert isinstance(api.get_replica_devicegroups(variables['URL']), list)
    assert isinstance(api.get_replica_devicegroup(variables['URL'], 'array_id', 'devicegroup_id'), dict)
    assert isinstance(api.get_replica_devicegroup_number(variables['URL'], 'array_id', 'devicegroup_id'), dict)
    assert isinstance(api.get_replica_arrays(variables['URL']), list)
    assert isinstance(api.get_replica_array(variables['URL'], 'array_id'), dict)
    assert isinstance(api.get_replica_rdfgroups(variables['URL'], 'array_id'), list)
    assert isinstance(api.get_replica_rdfgroup(variables['URL'], 'array_id', 'rdfg_num'), dict)
    assert isinstance(api.get_replica_storagegroups(variables['URL'], 'array_id'), list)
    assert isinstance(api.get_replica_storagegroup(variables['URL'], 'array_id', 'storagegroup_id'), dict)
    assert isinstance(api.get_replica_storagegroup_snaps(variables['URL'], 'array_id', 'storagegroup_id'), list)
    assert isinstance(api.get_replica_storagegroup_snap(variables['URL'], 'array_id', 'storagegroup_id', 'snap_id'), dict)
    assert isinstance(api.get_replica_storagegroup_snap_generations(variables['URL'], 'array_id', 'storagegroup_id', 'snap_id'), list)
    assert isinstance(api.get_replica_storagegroup_snap_generation(variables['URL'], 'array_id', 'storagegroup_id', 'snap_id', 'generation_num'), dict)

'''
######################################
## SYSTEM Resource group
######################################

def getAlerts(self, URL):

def getAlert(self, URL, resourceId):

def getJobs(self, URL):

def getJob(self, URL, resourceId):

def getSymms(self, URL):

def getSymm(self, URL, resourceId):

def getSymmAlerts(self, URL, resourceId):

def getSymmAlert(self, URL, symId, alertId):

def getSymmJobs(self, URL, resourceId):

def getSymmJob(self, URL, symId, jobId):

def getVersion(self, URL):

######################################
## WORKLOAD Resource group
######################################
'''
