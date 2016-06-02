
class VmaxApi(object):

    def __init__(self, Restful, base_url):

        self.rest = Restful
        url = "%s/univmax/restapi" % (base_url)
        self.rest.setURL(url)
        self.version = self.get_version()['version']

	supported_versions = {'V8.2.0.5' : '/82', 'V8.0.1.5' : ''}
        self.version_path = ""
	if supported_versions.has_key(self.version):
            self.version_path = supported_versions[self.version]

    ######################################
    ## ADMINISTRATION Resource group
    ######################################
    def get_app_list(self):
        target_uri = "%s/common/Application/list" % (self.rest.url)
        return self.rest.get(target_uri)

    def start_system_backup(self, backup_name):
        target_uri = "%s/common/Application/startSystemBackup" % (self.rest.url)
        request_data = {"systemBackupName":backup_name}
        return self.rest.post(target_uri, request_data)

    def auth_cirrus_user(self):
        target_uri = "%s/common/authenticateCirrusUser" % (self.rest.url)
        return self.rest.get(target_uri)

    def enroll_cirrus_user(self, cirrus_id, revoke_existing=True):
        target_uri = "%s/common/enrollWithCirrus/%s/%s" % (self.rest.url, cirrus_id, revoke_existing)
        return self.rest.get(target_uri)

    def get_sharding_info(self):
        target_uri = "%s/common/Sharding/info" % (self.rest.url)
        return self.rest.get(target_uri)

    def unenroll_cirrus_user(self, token):
        target_uri = "%s/common/unenrollFromCirrus/%s" % (self.rest.url, token)
        return self.rest.delete(target_uri)

    ######################################
    ## COMMON Resource group
    ######################################
    def get_iterator(self, iterator_id):
        target_uri = "%s/common/Iterator/%s" % (self.rest.url, iterator_id)
        return self.rest.get(target_uri)

    def delete_iterator(self, iterator_id):
        target_uri = "%s/common/Iterator/%s" % (self.rest.url, iterator_id)
        return self.rest.delete(target_uri)

    def get_iterator_page(self, iterator_id, params_dict=None):
        target_uri = "%s/common/Iterator/%s/page" % (self.rest.url, iterator_id)
        return self.rest.get(target_uri, params_dict)


    ######################################
    ## MANAGEMENT Resource group
    ######################################

    def get_usage_stats(self):
        target_uri = "%s/management/RuntimeUsage/read" % (self.rest.url)
        return self.rest.get(target_uri)

    ######################################
    ## PERFORMANCE Resource group
    ######################################

    # TODO

    ######################################
    ## PROVISIONING Resource group
    ######################################

    def get_prov_arrays(self):
        target_uri = "%s/provisioning/symmetrix" % (self.rest.url)
        return self.rest.get(target_uri)

    def get_prov_array(self, array_id):
        target_uri = "%s/provisioning/symmetrix/%s" % (self.rest.url, array_id)
        return self.rest.get(target_uri)

    def get_prov_array_directors(self, array_id):
        target_uri = "%s/provisioning/symmetrix/%s/director" % (self.rest.url, array_id)
        return self.rest.get(target_uri)

    def get_prov_array_director(self, array_id, director_id):
        target_uri = "%s/provisioning/symmetrix/%s/director/%s" % (self.rest.url, array_id, director_id)
        return self.rest.get(target_uri)

    def get_prov_array_director_ports(self, array_id, director_id, params_dict=None):
        target_uri = "%s/provisioning/symmetrix/%s/director/%s/port" % (self.rest.url, array_id, director_id)
        return self.rest.get(target_uri, params_dict)

    def get_prov_array_director_port(self, array_id, director_id, port_id):
        target_uri = "%s/provisioning/symmetrix/%s/director/%s/port/%s" % (self.rest.url, array_id, director_id, port_id)
        return self.rest.get(target_uri)

    def get_prov_array_fastpolicies(self, array_id, params_dict=None):
        target_uri = "%s/provisioning/symmetrix/%s/fastpolicy" % (self.rest.url, array_id)
        return self.rest.get(target_uri, params_dict)

    def create_fastpolicy(self, array_id, params_dict):
        target_uri = "%s/provisioning/symmetrix%s/fastpolicy/%s" % (self.rest.url, array_id, policy_name)
        return self.rest.post(target_uri, params_dict)

    def edit_fastpolicy(self, array_id, params_dict):
        target_uri = "%s/provisioning/symmetrix%s/fastpolicy/%s" % (self.rest.url, array_id, policy_name)
        return self.rest.put(target_uri, params_dict)

    def delete_fastpolicy(self, array_id, policy_id):
        target_uri = "%s/provisioning/symmetrix%s/fastpolicy/%s" % (self.rest.url, array_id, policy_id)
        return self.rest.delete(target_uri)

    def get_prov_array_fastpolicy(self, array_id, policy_id):
        target_uri = "%s/provisioning/symmetrix%s/fastpolicy/%s" % (self.rest.url, array_id, policy_id)
        return self.rest.get(target_uri)

    def get_prov_array_hosts(self, array_id):
        target_uri = "%s/provisioning/symmetrix/%s/host" % (self.rest.url, array_id)
        return self.rest.get(target_uri)

    def get_prov_array_host(self, array_id, host_id):
        target_uri = "%s/provisioning/symmetrix%s/host/%s" % (self.rest.url, array_id, host_id)
        return self.rest.get(target_uri)

    def create_prov_array_host(self, array_id, params_dict):
        target_uri = "%s/provisioning/symmetrix%s/host" % (self.rest.url, array_id)
        return self.rest.post(target_uri, params_dict)

    def edit_prov_array_host(self, array_id, host_id, params_dict):
        target_uri = "%s/provisioning/symmetrix%s/host/%s" % (self.rest.url, array_id, host_id)
        return self.rest.put(target_uri, params_dict)

    def delete_prov_array_host(self, array_id, host_id):
        target_uri = "%s/provisioning/symmetrix%s/host/%s" % (self.rest.url, array_id, host_id)
        return self.rest.delete(target_uri)

    def get_prov_array_hostgroups(self, array_id):
        target_uri = "%s/provisioning/symmetrix/%s/hostgroup" % (self.rest.url, array_id)
        return self.rest.get(target_uri)

    def create_prov_array_hostgroup(self, array_id, params_dict):
        target_uri = "%s/provisioning/symmetrix/%s/hostgroup" % (self.rest.url, array_id)
        return self.rest.post(target_uri, params_dict)

    def get_prov_array_hostgroup(self, array_id, hostgroup_id):
        target_uri = "%s/provisioning/symmetrix/%s/hostgroup/%s" % (self.rest.url, array_id, hostgroup_id)
        return self.rest.get(target_uri)

    def edit_prov_array_hostgroup(self, array_id, hostgroup_id, params_dict):
        target_uri = "%s/provisioning/symmetrix/%s/hostgroup/%s" % (self.rest.url, array_id, hostgroup_id)
        return self.rest.put(target_uri, params_dict)

    def delete_prov_array_hostgroup(self, array_id, hostgroup_id):
        target_uri = "%s/provisioning/symmetrix/%s/hostgroup/%s" % (self.rest.url, array_id, hostgroup_id)
        return self.rest.delete(target_uri)

    def get_prov_array_initiators(self, array_id, params_dict=None):
        target_uri = "%s/provisioning/symmetrix/%s/initiator" % (self.rest.url, array_id)
        return self.rest.get(target_uri, params_dict)

    def get_prov_array_initiator(self, array_id, initiator_id):
        target_uri = "%s/provisioning/symmetrix/%s/initiator/%s" % (self.rest.url, array_id, initiator_id)
        return self.rest.get(target_uri)

    def edit_prov_array_initiator(self, array_id, initiator_id, params_dict):
        target_uri = "%s/provisioning/symmetrix/%s/initiator/%s" % (self.rest.url, array_id, initiator_id)
        return self.rest.put(target_uri, params_dict)

    def get_prov_array_maskingviews(self, array_id, params_dict=None):
        target_uri = "%s/provisioning/symmetrix/%s/maskingview" % (self.rest.url, array_id)
        return self.rest.get(target_uri, params_dict)

    def create_prov_array_maskingviews(self, array_id, params_dict):
        target_uri = "%s/provisioning/symmetrix/%s/maskingview" % (self.rest.url, array_id)
        return self.rest.post(target_uri, params_dict)

    def get_prov_array_maskingview(self, array_id, maskingview_id):
        target_uri = "%s/provisioning/symmetrix/%s/maskingview/%s" % (self.rest.url, array_id, maskingview_id)
        return self.rest.get(target_uri)

    def edit_prov_array_maskingview(self, array_id, maskingview_id, params_dict):
        target_uri = "%s/provisioning/symmetrix/%s/maskingview/%s" % (self.rest.url, array_id, maskingview_id)
        return self.rest.put(target_uri, params_dict)

    def delete_prov_array_maskingview(self, array_id, maskingview_id):
        target_uri = "%s/provisioning/symmetrix/%s/maskingview/%s" % (self.rest.url, array_id, maskingview_id)
        return self.rest.delete(target_uri)

    def get_prov_array_maskingview_connections(self, array_id, maskingview_id, params_dict=None):
        target_uri = "%s/provisioning/symmetrix/%s/maskingview/%s/connections" % (self.rest.url, array_id, maskingview_id)
        return self.rest.get(target_uri, params_dict)

    def get_prov_array_ports(self, array_id, params_dict=None):
        target_uri = "%s/provisioning/symmetrix/%s/port" % (self.rest.url, array_id)
        return self.rest.get(target_uri, params_dict)

    def get_prov_array_portgoups(self, array_id, params_dict=None):
        target_uri = "%s/provisioning/symmetrix/%s/portgroup" % (self.rest.url, array_id)
        return self.rest.get(target_uri, params_dict)

    def create_prov_array_portgoups(self, array_id, params_dict):
        target_uri = "%s/provisioning/symmetrix/%s/portgroup" % (self.rest.url, array_id)
        return self.rest.post(target_uri, params_dict)

    def get_prov_array_portgroup(self, array_id, portgroup_id):
        target_uri = "%s/provisioning/symmetrix/%s/portgroup/%s" % (self.rest.url, array_id, portgroup_id)
        return self.rest.get(target_uri)

    def edit_prov_array_portgroup(self, array_id, portgroup_id, params_dict):
        target_uri = "%s/provisioning/symmetrix/%s/portgroup/%s" % (self.rest.url, array_id, portgroup_id)
        return self.rest.put(target_uri, params_dict)

    def delete_prov_array_portgroup(self, array_id, portgroup_id):
        target_uri = "%s/provisioning/symmetrix/%s/portgroup/%s" % (self.rest.url, array_id, portgroup_id)
        return self.rest.delete(target_uri)

    def get_prov_array_storagegroups(self, array_id, params_dict=None):
        target_uri = "%s/provisioning/symmetrix/%s/storagegroup" % (self.rest.url, array_id)
        return self.rest.get(target_uri, params_dict)

    def create_prov_array_storagegroups(self, array_id, params_dict):
        target_uri = "%s/provisioning/symmetrix/%s/storagegroup" % (self.rest.url, array_id)
        return self.rest.post(target_uri, params_dict)

    def get_prov_array_storagegroup(self, array_id, storagegroup_id):
        target_uri = "%s/provisioning/symmetrix/%s/storagegroup/%s" % (self.rest.url, array_id, storagegroup_id)
        return self.rest.get(target_uri)

    def edit_prov_array_storagegroup(self, array_id, storagegroup_id, params_dict):
        target_uri = "%s/provisioning/symmetrix/%s/storagegroup/%s" % (self.rest.url, array_id, storagegroup_id)
        return self.rest.delete(target_uri, params_dict)

    def delete_prov_array_storagegroup(self, array_id, storagegroup_id):
        target_uri = "%s/provisioning/symmetrix/%s/storagegroup/%s" % (self.rest.url, array_id, storagegroup_id)
        return self.rest.delete(target_uri)

    def get_prov_array_thinpools(self, array_id, params_dict=None):
        target_uri = "%s/provisioning/symmetrix/%s/thinpool" % (self.rest.url, array_id)
        return self.rest.get(target_uri, params_dict)

    def create_prov_array_thinpools(self, array_id, params_dict=None):
        target_uri = "%s/provisioning/symmetrix/%s/thinpool" % (self.rest.url, array_id)
        return self.rest.post(target_uri, params_dict)

    def get_prov_array_thinpool(self, array_id, thinpool_id):
        target_uri = "%s/provisioning/symmetrix/%s/thinpool/%s" % (self.rest.url, array_id, thinpool_id)
        return self.rest.get(target_uri)

    def edit_prov_array_thinpool(self, array_id, thinpool_id, params_dict):
        target_uri = "%s/provisioning/symmetrix/%s/thinpool/%s" % (self.rest.url, array_id, thinpool_id)
        return self.rest.put(target_uri, params_dict)

    def delete_prov_array_thinpool(self, array_id, thinpool_id):
        target_uri = "%s/provisioning/symmetrix/%s/thinpool/%s" % (self.rest.url, array_id, thinpool_id)
        return self.rest.delete(target_uri)

    def get_prov_array_tiers(self, array_id, params_dict=None):
        target_uri = "%s/provisioning/symmetrix/%s/tier" % (self.rest.url, array_id)
        return self.rest.get(target_uri, params_dict)

    def create_prov_array_tier(self, array_id, params_dict):
        target_uri = "%s/provisioning/symmetrix/%s/tier" % (self.rest.url, array_id)
        return self.rest.post(target_uri, params_dict)

    def get_prov_array_tier(self, array_id, tier_id):
        target_uri = "%s/provisioning/symmetrix/%s/tier/%s" % (self.rest.url, array_id, tier_id)
        return self.rest.get(target_uri)

    def delete_prov_array_tier(self, array_id, tier_id):
        target_uri = "%s/provisioning/symmetrix/%s/tier/%s" % (self.rest.url, array_id, tier_id)
        return self.rest.delete(target_uri)

    def get_prov_array_volumes(self, array_id, params_dict=None):
        target_uri = "%s/provisioning/symmetrix/%s/volume" % (self.rest.url, array_id)
        return self.rest.get(target_uri, params_dict)

    def get_prov_array_volume(self, array_id, volume_id):
        target_uri = "%s/provisioning/symmetrix/%s/volume/%s" % (self.rest.url, array_id, volume_id)
        return self.rest.get(target_uri)

    def delete_prov_array_volume(self, array_id, volume_id):
        target_uri = "%s/provisioning/symmetrix/%s/volume/%s" % (self.rest.url, array_id, volume_id)
        return self.rest.delete(target_uri)


    ######################################
    ## REPLICATION Resource group
    ######################################

    # TODO

    ######################################
    ## SLO PROVISIONING Resource group
    ######################################

''' TODO: determine a way to manage additional API calls into the future beginning with this set as yet unimplemented
/82/sloprovisioning/symmetrix
/82/sloprovisioning/symmetrix/{symmetrixId}
/82/sloprovisioning/symmetrix/{symmetrixId}/slo
/82/sloprovisioning/symmetrix/{symmetrixId}/split
/82/sloprovisioning/symmetrix/{symmetrixId}/split/{splitId}
/82/sloprovisioning/symmetrix/{symmetrixId}/split/{splitId}/cuimage
/82/sloprovisioning/symmetrix/{symmetrixId}/split/{splitId}/cuimage/{cuImageSSID}
/82/sloprovisioning/symmetrix/{symmetrixId}/split/{splitId}/cuimage/{cuImageSSID}/volume
/82/sloprovisioning/symmetrix/{symmetrixId}/split/{splitId}/cuimage/{cuImageSSID}/volume/{volumeId}
/82/sloprovisioning/symmetrix/{symmetrixId}/split/{splitId}/storageProvisioningToHost
/82/sloprovisioning/symmetrix/{symmetrixId}/srp
/82/sloprovisioning/symmetrix/{symmetrixId}/storagegroup
/82/sloprovisioning/symmetrix/{symmetrixId}/storagegroup/{storageGroupId}
/82/sloprovisioning/symmetrix/{symmetrixId}/volume
/82/sloprovisioning/symmetrix/{symmetrixId}/volume/{volumeId}
'''
    def get_slo_arrays(self):
        target_uri = "%s/sloprovisioning/symmetrix" % (self.rest.url)
        return self.rest.get(target_uri)

    def get_slo_array(self, resourceId):
        target_uri = "%s/sloprovisioning/symmetrix/%s" % (self.rest.url, resourceId)
        return self.rest.get(target_uri)

    def get_slo_array_directors(self, resourceId):
        target_uri = "%s/sloprovisioning/symmetrix/%s/director" % (self.rest.url, resourceId)
        return self.rest.get(target_uri)

    def get_slo_array_director(self, symmId, resourceId):
        target_uri = "%s/sloprovisioning/symmetrix/%s/director/%s" % (self.rest.url, symmId, resourceId)
        return self.rest.get(target_uri)

    def get_slo_array_ports(self, symmId, portId, params_dict):
        target_uri = "%s/sloprovisioning/symmetrix/%s/director/%s/port" % (self.rest.url, symmId, portId)
        return self.rest.get(target_uri, params_dict)

    def get_slo_array_port(self, symmId, directorId, portId):
        target_uri = "%s/sloprovisioning/symmetrix/%s/director/%s/port/%s" % (self.rest.url, symmId, directorId, portId)
        return self.rest.get(target_uri)

    def get_slo_array_hosts(self, resourceId, params_dict):
        target_uri = "%s/sloprovisioning/symmetrix/%s/host" % (self.rest.url, resourceId)
        return self.rest.get(target_uri, params_dict)

    def create_slo_array_host(self, symm_id, params_dict):
        target_uri = "%s/sloprovisioning/symmetrix/%s/host" % (self.rest.url, symm_id)
        return self.rest.post(target_uri, params_dict)

    def get_slo_array_host(self, symmId, hostId):
        target_uri = "%s/sloprovisioning/symmetrix/%s/host/%s" % (self.rest.url, symmId, hostId)
        return self.rest.get(target_uri)

    def edit_slo_array_host(self, symmId, hostId, params_dict):
        target_uri = "%s/sloprovisioning/symmetrix/%s/host/%s" % (self.rest.url, symmId, hostId)
        return self.rest.put(target_uri, params_dict)

    def delete_slo_array_host(self, symmId, hostId):
        target_uri = "%s/sloprovisioning/symmetrix/%s/host/%s" % (self.rest.url, symmId, hostId)
        return self.rest.delete(target_uri)

    def get_slo_array_hostgroups(self, symm_id, params_dict):
        target_uri = "%s/sloprovisioning/symmetrix/%s/hostgroup" % (self.rest.url, symm_id)
        return self.rest.get(target_uri, params_dict)

    def create_slo_array_hostgroup(self, symm_id, params_dict):
        target_uri = "%s/sloprovisioning/symmetrix/%s/hostgroup" % (self.rest.url, symm_id)
        return self.rest.post(target_uri, params_dict)

    def get_slo_array_hostgroup(self, symmId, grpId):
        target_uri = "%s/sloprovisioning/symmetrix/%s/hostgroup/%s" % (self.rest.url, symmId, grpId)
        return self.rest.get(target_uri)

    def edit_slo_array_hostgroup(self, symmId, grpId, params_dict):
        target_uri = "%s/sloprovisioning/symmetrix/%s/hostgroup/%s" % (self.rest.url, symmId, grpId)
        return self.rest.put(target_uri, params_dict)

    def delete_slo_array_hostgroup(self, symmId, grpId):
        target_uri = "%s/sloprovisioning/symmetrix/%s/hostgroup/%s" % (self.rest.url, symmId, grpId)
        return self.rest.delete(target_uri)

    def get_slo_array_initiators(self, resourceId, params_dict):
        target_uri = "%s/sloprovisioning/symmetrix/%s/initiator" % (self.rest.url, resourceId)
        return self.rest.get(target_uri, params_dict)

    def get_slo_array_initiator(self, symmId, initiatorId):
        target_uri = "%s/sloprovisioning/symmetrix/%s/initiator/%s" % (self.rest.url, symmId, initatorId)
        return self.rest.get(target_uri)

    def edit_slo_array_initiator(self, symmId, initiatorId, params_dict):
        target_uri = "%s/sloprovisioning/symmetrix/%s/initiator/%s" % (self.rest.url, symmId, initatorId)
        return self.rest.put(target_uri, params_dict)

    def get_slo_array_maskingviews(self, resourceId, params_dict):
        target_uri = "%s/sloprovisioning/symmetrix/%s/maskingview" % (self.rest.url, resourceId)
        return self.rest.get(target_uri, params_dict)

    def create_slo_array_maskingviews(self, symm_id, params_dict):
        target_uri = "%s/sloprovisioning/symmetrix/%s/maskingview" % (self.rest.url, symm_id)
        return self.rest.post(target_uri, params_dict)

    def get_slo_arary_maskingview(self, symmId, mvId):
        target_uri = "%s/sloprovisioning/symmetrix/%s/maskingview/%s" % (self.rest.url, symmId, mvId)
        return self.rest.get(target_uri)

    def edit_slo_arary_maskingview(self, symmId, mvId, params_dict):
        target_uri = "%s/sloprovisioning/symmetrix/%s/maskingview/%s" % (self.rest.url, symmId, mvId)
        return self.rest.put(target_uri, params_dict)

    def delete_slo_arary_maskingview(self, symmId, mvId):
        target_uri = "%s/sloprovisioning/symmetrix/%s/maskingview/%s" % (self.rest.url, symmId, mvId)
        return self.rest.delete(target_uri)

    def get_slo_array_maskingview_connections(self, symmId, mvId, params_dict):
        target_uri = "%s/sloprovisioning/symmetrix/%s/maskingview/%s/connections" % (self.rest.url, symmId, mvId)
        return self.rest.get(target_uri, params_dict)

    def get_slo_array_ports(self, resourceId, params_dict):
        target_uri = "%s/sloprovisioning/symmetrix/%s/port" % (self.rest.url, resourceId)
        return self.rest.get(target_uri, params_dict)

    def get_slo_array_portgroups(self, resourceId, params_dict):
        target_uri = "%s/sloprovisioning/symmetrix/%s/portgroup" % (self.rest.url, resourceId)
        return self.rest.get(target_uri, params_dict)

    def create_slo_array_portgroup(self, resourceId, params_dict):
        target_uri = "%s/sloprovisioning/symmetrix/%s/portgroup" % (self.rest.url, resourceId)
        return self.rest.post(target_uri, params_dict)

    def get_slo_array_portgroup(self, symmId, pgId):
        target_uri = "%s/sloprovisioning/symmetrix/%s/portgroup/%s" % (self.rest.url, symmId, pgId)
        return self.rest.get(target_uri)

    def edit_slo_array_portgroup(self, symmId, pgId, params_dict):
        target_uri = "%s/sloprovisioning/symmetrix/%s/portgroup/%s" % (self.rest.url, symmId, pgId)
        return self.rest.get(target_uri, params_dict)

    def delete_slo_array_portgroup(self, symmId, pgId):
        target_uri = "%s/sloprovisioning/symmetrix/%s/portgroup/%s" % (self.rest.url, symmId, pgId)
        return self.rest.delete(target_uri)

    def get_slo_array_slos(self, resourceId, params_dict):
        target_uri = "%s/sloprovisioning/symmetrix/%s/slo" % (self.rest.url, resourceId)
        return self.rest.get(target_uri, params_dict)

    def get_slo_array_slo(self, symmId, sloId):
        target_uri = "%s/sloprovisioning/symmetrix/%s/slo/%s" % (self.rest.url, symmId, sloId)
        return self.rest.get(target_uri)

    def edit_slo_array_slo(self, symmId, sloId, params_dict):
        target_uri = "%s/sloprovisioning/symmetrix/%s/slo/%s" % (self.rest.url, symmId, sloId)
        return self.rest.put(target_uri, params_dict)

    def get_slo_array_srps(self, resourceId, params_dict):
        target_uri = "%s/sloprovisioning/symmetrix/%s/srp" % (self.rest.url, resourceId)
        return self.rest.get(target_uri, params_dict)

    def get_slo_array_srp(self, symmId, srpId):
        target_uri = "%s/sloprovisioning/symmetrix/%s/srp/%s" % (self.rest.url, symmId, srpId)
        return self.rest.get(target_uri)

    def get_slo_array_storagegroups(self, resourceId):
        target_uri = "%s/sloprovisioning/symmetrix/%s/storagegroup" % (self.rest.url, resourceId)
        return self.rest.get(target_uri)

    def create_slo_array_storagegroup(self, resourceId, params_dict):
        target_uri = "%s/sloprovisioning/symmetrix/%s/storagegroup" % (self.rest.url, resourceId)
        return self.rest.post(target_uri, params_dict)

    def get_slo_array_storagegroup(self, symmId, sgId):
        target_uri = "%s/sloprovisioning/symmetrix/%s/storagegroup/%s" % (self.rest.url, symmId, sgId)
        return self.rest.get(target_uri)

    def edit_slo_array_storagegroup(self, symmId, sgId, params_dict):
        target_uri = "%s/sloprovisioning/symmetrix/%s/storagegroup/%s" % (self.rest.url, symmId, sgId)
        return self.rest.put(target_uri, params_dict)

    def delete_slo_array_storagegroup(self, symmId, sgId):
        target_uri = "%s/sloprovisioning/symmetrix/%s/storagegroup/%s" % (self.rest.url, symmId, sgId)
        return self.rest.delete(target_uri)

    def get_slo_array_volumes(self, resourceId, params_dict):
        target_uri = "%s/sloprovisioning/symmetrix/%s/volume" % (self.rest.url, resourceId)
        return self.rest.get(target_uri, params_dict)

    def get_slo_array_volume(self, symm_id, volume_id):
        target_uri = "%s/sloprovisioning/symmetrix/%s/volume/%s" % (self.rest.url, symm_id, volume_id)
        return self.rest.get(target_uri)

    def delete_slo_array_volume(self, symm_id, volume_id):
        target_uri = "%s/sloprovisioning/symmetrix/%s/volume/%s" % (self.rest.url, symm_id, volume_id)
        return self.rest.delete(target_uri)

    def get_slo_array_workloads(self, symm_id):
        target_uri = "%s/sloprovisioning/symmetrix/%s/workloadtype" % (self.rest.url, symm_id)
        return self.rest.get(target_uri)


    ######################################
    ## SYSTEM Resource group
    ######################################

    ################
    ## get a list of All Alert ids across all symmetrix arrays
    ################
    def get_alerts(self):
        target_uri = "%s/system/alert" % (self.rest.url)
        return self.rest.get(target_uri)

    ################
    ## queries for a specified Alert
    ################
    def get_alert(self, resourceId):
        target_uri = "%s/system/alert/%s" % (self.rest.url, resourceId)
        return self.rest.get(target_uri)

    ################
    ## queries for a list of Job ids across all symmetrix arrays
    ################
    def get_jobs(self):
        target_uri = "%s/system/job" % (self.rest.url)
        return self.rest.get(target_uri)

    ################
    ## queries for a specified job
    ################
    def get_job(self, resourceId):
        target_uri = "%s/system/job/%s" % (self.rest.url, resourceId)
        return self.rest.get(target_uri)

    ################
    ## get a list of symmetrix serial #'s known by Unisphere
    ################
    def get_arrays(self):
        target_uri = "%s/system/symmetrix" % (self.rest.url)
        return self.rest.get(target_uri)

    ################
    ## This call queries for a specific Authorized Symmetrix Object that is compatible with slo provisioning using its ID
    ################
    def get_array(self, resourceId):
        target_uri = "%s/system/symmetrix/%s" % (self.rest.url, resourceId)
        return self.rest.get(target_uri)

    ################
    ## get a list of All Alert ids for a specific array id
    ################
    def get_array_alerts(self, resourceId):
        target_uri = "%s/system/symmetrix/%s/alert" % (self.rest.url, resourceId)
        return self.rest.get(target_uri)

    ################
    ## queries for a specified Alert on a specified array
    ################
    def get_array_alert(self, symId, alertId):
        target_uri = "%s/system/symmetrix/%s/alert/%s" % (self.rest.url, symId, alertId)
        return self.rest.get(target_uri)

    ################
    ## queries for a list of Job ids on a specified array
    ################
    def get_array_jobs(self, resourceId):
        target_uri = "%s/system/symmetrix/%s/job" % (self.rest.url, resourceId)
        return self.rest.get(target_uri)

    ################
    ## queries for a specified job on a specified array
    ################
    def get_array_job(self, symId, jobId):
        target_uri = "%s/system/symmetrix/%s/job/%s" % (self.rest.url, symId, jobId)
        return self.rest.get(target_uri)

    ################
    ## get the version of Unisphere (the API)
    ################
    def get_version(self):
        target_uri = "%s/system/version" % (self.rest.url)
        return self.rest.get(target_uri)

    ######################################
    ## VVOL Resource group
    ######################################
    # TODO


    ######################################
    ## WORKLOAD Resource group
    ######################################
    # TODO
