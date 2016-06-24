class VmaxApi(object):
    """API definition class that implements one method for each REST API call
    Attributes:
        version (str): descripter of the API version
        api_counter (int): number of API calls made during this python interpreter session
        api_timer (int): sum of ms response time of all API calls made during this python interpreter session
        api_last_resp_time (int): ms response time of last API call made during this python interpreter session
    Args:
        Restful (:obj:`Restful`): connection object to the API server
        base_url (str):  the ip and port # of api server
    """

    def __init__(self, Restful, base_url):

        self.rest = Restful
        url = "%s/univmax/restapi" % (base_url)
        self.rest.set_url(url)
        self.version = 'v82'

    ######################################
    ## ADMINISTRATION Resource group
    ######################################
    def get_app_list(self):
        """/common/Application/list
        List the applications registered with this instance of EMC Unisphere for VMAX
        """
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

    def get_perf_host_keys(self, params_dict):
        target_uri = "%s/81/performance/Host/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_host_metrics(self, params_dict):
        target_uri = "%s/81/performance/Host/metrics" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_initiator_keys(self, params_dict):
        target_uri = "%s/81/performance/Initiator/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_initiator_metrics(self, params_dict):
        target_uri = "%s/81/performance/Initiator/metrics" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_initiatorbyport_keys(self, params_dict):
        target_uri = "%s/81/performance/InitiatorByPort/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_initiatorbyport_metrics(self, params_dict):
        target_uri = "%s/81/performance/InitiatorByPort/metrics" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_iscsiclient_keys(self, params_dict):
        target_uri = "%s/81/performance/ISCSIClient/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_scsiclient_metrics(self, params_dict):
        target_uri = "%s/81/performance/ISCSIClient/metrics" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_iscsitarget_keys(self, params_dict):
        target_uri = "%s/81/performance/ISCSITarget/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_scsitarget_metrics(self, params_dict):
        target_uri = "%s/81/performance/ISCSITarget/metrics" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_storagecontainer_keys(self, params_dict):
        target_uri = "%s/82/performance/StorageContainer/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_storagecontainer_metrics(self, params_dict):
        target_uri = "%s/82/performance/StorageContainer/metrics" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_storageresrource_keys(self, params_dict):
        target_uri = "%s/82/performance/StorageResource/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_storageresource_metrics(self, params_dict):
        target_uri = "%s/82/performance/StorageResource/metrics" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_storageresrourcebypool_keys(self, params_dict):
        target_uri = "%s/82/performance/StorageResourceByPool/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_storageresourcebypool_metrics(self, params_dict):
        target_uri = "%s/82/performance/StorageResourceByPool/metrics" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_array_alerts(self, params_dict):
        target_uri = "%s/performance/Array/alerts" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_array_keys(self, params_dict):
        target_uri = "%s/performance/Array/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_array_metrics(self, params_dict):
        target_uri = "%s/performance/Array/metrics" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_BEDirector_keys(self, params_dict):
        target_uri = "%s/performance/BEDirector/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_BEDirector_metrics(self, params_dict):
        target_uri = "%s/performance/BEDirector/metrics" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_beemulation_keys(self, params_dict):
        target_uri = "%s/performance/BeEmulation/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_beemulation_metrics(self, params_dict):
        target_uri = "%s/performance/BeEmulation/metrics" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_beport_keys(self, params_dict):
        target_uri = "%s/performance/BEPort/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_beport_metrics(self, params_dict):
        target_uri = "%s/performance/BEPort/metrics" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_board_keys(self, params_dict):
        target_uri = "%s/performance/Board/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_board_metrics(self, params_dict):
        target_uri = "%s/performance/Board/metrics" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_cachepartition_keys(self, params_dict):
        target_uri = "%s/performance/CachePartition/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_cachepartition_metrics(self, params_dict):
        target_uri = "%s/performance/CachePartition/metrics" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_core_keys(self, params_dict):
        target_uri = "%s/performance/Core/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_core_metrics(self, params_dict):
        target_uri = "%s/performance/Core/metrics" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_database_keys(self, params_dict):
        target_uri = "%s/performance/Database/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_database_metrics(self, params_dict):
        target_uri = "%s/performance/Database/metrics" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_databasebypool_keys(self, params_dict):
        target_uri = "%s/performance/DatabaseByPool/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_databasebypool_metrics(self, params_dict):
        target_uri = "%s/performance/DatabaseByPool/metrics" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_devicegroup_keys(self, params_dict):
        target_uri = "%s/performance/DeviceGroup/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_devicegroup_metrics(self, params_dict):
        target_uri = "%s/performance/DeviceGroup/metrics" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_disk_keys(self, params_dict):
        target_uri = "%s/performance/Disk/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_disk_metrics(self, params_dict):
        target_uri = "%s/performance/Disk/metrics" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_diskgroup_keys(self, params_dict):
        target_uri = "%s/performance/DiskGroup/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_diskgroup_metrics(self, params_dict):
        target_uri = "%s/performance/DiskGroup/metrics" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_disktechpool_keys(self, params_dict):
        target_uri = "%s/performance/DiskTechPool/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_disktechpool_metrics(self, params_dict):
        target_uri = "%s/performance/DiskTechPool/metrics" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_dsepool_keys(self, params_dict):
        target_uri = "%s/performance/DSEPool/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_dsepool_metrics(self, params_dict):
        target_uri = "%s/performance/DSEPool/metrics" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_edsdirector_keys(self, params_dict):
        target_uri = "%s/performance/EDSDirector/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_edsdirector_metrics(self, params_dict):
        target_uri = "%s/performance/EDSDirector/metrics" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_edsemulation_keys(self, params_dict):
        target_uri = "%s/performance/EDSEmulation/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_edsemulation_metrics(self, params_dict):
        target_uri = "%s/performance/EDSEmulation/metrics" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_externaldisk_keys(self, params_dict):
        target_uri = "%s/performance/ExternalDisk/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_externaldisk_metrics(self, params_dict):
        target_uri = "%s/performance/ExternalDisk/metrics" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_externaldiskgroup_keys(self, params_dict):
        target_uri = "%s/performance/ExternalDiskGroup/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_externaldiskgroup_metrics(self, params_dict):
        target_uri = "%s/performance/ExternalDiskGroup/metrics" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_fastpolicy_keys(self, params_dict):
        target_uri = "%s/performance/FASTPolicy/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_fastpolicy_metrics(self, params_dict):
        target_uri = "%s/performance/FASTPolicy/metrics" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_fedirector_keys(self, params_dict):
        target_uri = "%s/performance/FEDirector/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_fedirector_metrics(self, params_dict):
        target_uri = "%s/performance/FEDirector/metrics" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_fedirectorbyport_keys(self, params_dict):
        target_uri = "%s/performance/FEDirectorByPort/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_fedirectorbyport_metrics(self, params_dict):
        target_uri = "%s/performance/FEDirectorByPort/metrics" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_feemulation_keys(self, params_dict):
        target_uri = "%s/performance/FeEmulation/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_feemulation_metrics(self, params_dict):
        target_uri = "%s/performance/FeEmulation/metrics" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_feport_keys(self, params_dict):
        target_uri = "%s/performance/FEPort/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_feport_metrics(self, params_dict):
        target_uri = "%s/performance/FEPort/metrics" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_ficonemulation_keys(self, params_dict):
        target_uri = "%s/performance/FiconEmulation/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_ficonemulation_metrics(self, params_dict):
        target_uri = "%s/performance/FiconEmulation/metrics" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_imdirector_keys(self, params_dict):
        target_uri = "%s/performance/IMDirector/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_imdirector_metrics(self, params_dict):
        target_uri = "%s/performance/IMDirector/metrics" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_imemulation_keys(self, params_dict):
        target_uri = "%s/performance/IMEmulation/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_imemulation_metrics(self, params_dict):
        target_uri = "%s/performance/IMEmulation/metrics" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_portgroup_keys(self, params_dict):
        target_uri = "%s/performance/PortGroup/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_portgroup_metrics(self, params_dict):
        target_uri = "%s/performance/PortGroup/metrics" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_rdfa_keys(self, params_dict):
        target_uri = "%s/performance/RDFA/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_rdfa_metrics(self, params_dict):
        target_uri = "%s/performance/RDFA/metrics" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_rdfdirector_keys(self, params_dict):
        target_uri = "%s/performance/RDFDirector/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_rdfdirector_metrics(self, params_dict):
        target_uri = "%s/performance/RDFDirector/metrics" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_rdfemulation_keys(self, params_dict):
        target_uri = "%s/performance/RDFEmulation/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_rdfemulation_metrics(self, params_dict):
        target_uri = "%s/performance/RDFEmulation/metrics" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_rdfport_keys(self, params_dict):
        target_uri = "%s/performance/RDFPort/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_rdfport_metrics(self, params_dict):
        target_uri = "%s/performance/RDFPort/metrics" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_rdfs_keys(self, params_dict):
        target_uri = "%s/performance/RDFS/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_rdfs_metrics(self, params_dict):
        target_uri = "%s/performance/RDFS/metrics" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_settings_importfiles(self, params_dict):
        target_uri = "%s/performance/Settings/importFiles" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_snappool_keys(self, params_dict):
        target_uri = "%s/performance/SnapPool/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_snappool_metrics(self, params_dict):
        target_uri = "%s/performance/SnapPool/metrics" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_srp_keys(self, params_dict):
        target_uri = "%s/performance/SRP/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_srp_metrics(self, params_dict):
        target_uri = "%s/performance/SRP/metrics" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_srpthinpool_keys(self, params_dict):
        target_uri = "%s/performance/SRPThinPool/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_storagegroup_keys(self, params_dict):
        target_uri = "%s/performance/StorageGroup/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_storagegroup_metrics(self, params_dict):
        target_uri = "%s/performance/StorageGroup/metrics" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_storagegroupbypool_keys(self, params_dict):
        target_uri = "%s/performance/StorageGroupByPool/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_storagegroupbypool_metrics(self, params_dict):
        target_uri = "%s/performance/StorageGroupByPool/metrics" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_storagegroupbytier_keys(self, params_dict):
        target_uri = "%s/performance/StorageGroupByTier/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_storagegroupbytier_metrics(self, params_dict):
        target_uri = "%s/performance/StorageGroupByTier/metrics" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_storagegroupbytier_perfkeys(self, params_dict):
        target_uri = "%s/performance/StorageGroupByTier/perf/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_storagetier_keys(self, params_dict):
        target_uri = "%s/performance/StorageTier/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_storagetier_metrics(self, params_dict):
        target_uri = "%s/performance/StorageTier/metrics" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_summary_keys(self, params_dict):
        target_uri = "%s/performance/Summary/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_thinpool_keys(self, params_dict):
        target_uri = "%s/performance/ThinPool/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_thinpool_metrics(self, params_dict):
        target_uri = "%s/performance/ThinPool/metrics" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_thintier_keys(self, params_dict):
        target_uri = "%s/performance/ThinTier/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_thintier_metrics(self, params_dict):
        target_uri = "%s/performance/ThinTier/metrics" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_tierbystoragegroup_keys(self, params_dict):
        target_uri = "%s/performance/TierByStorageGroup/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_tierbystoragegroup_metrics(self, params_dict):
        target_uri = "%s/performance/TierByStorageGroup/metrics" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    def get_perf_tierbystoragegroup_perfkeys(self, params_dict):
        target_uri = "%s/performance/TierByStorageGroup/perf/keys" % (self.rest.url)
        return self.rest.post(target_uri, params_dict)

    ######################################
    ## PROVISIONING Resource group
    ######################################

    def get_prov_arrays(self):
        target_uri = "%s/provisioning/symmetrix" % (self.rest.url)
        return self.rest.get(target_uri)

    def get_prov_array(self, array_id):
        target_uri = "%s/82/provisioning/symmetrix/%s" % (self.rest.url, array_id)
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

    def create_fastpolicy(self, array_id, policy_name, params_dict):
        target_uri = "%s/provisioning/symmetrix%s/fastpolicy/%s" % (self.rest.url, array_id, policy_name)
        return self.rest.post(target_uri, params_dict)

    def edit_fastpolicy(self, array_id, policy_name, params_dict):
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

    def get_replica_devicegroup(self, group_id):
        target_uri = "%s/81/replication/devicegroup/%s" % (self.rest.url, group_id)
        return self.rest.get(target_uri)

    def get_replica_srdfgroup(self, symm_id, rdfg_num):
        target_uri = "%s/82/replication/symmetrix/%s/rdf_group/%s" % (self.rest.url, symm_id, rdfg_num)
        return self.rest.get(target_uri)

    def get_replica_storagegroups(self, symm_id, params_dict=None):
        target_uri = "%s/82/replication/symmetrix/%s/storagegroup" % (self.rest.url, symm_id)
        return self.rest.get(target_uri, params_dict)

    def get_replica_storagegroup(self, symm_id, group_id):
        target_uri = "%s/82/replication/symmetrix/%s/storagegroup/%s" % (self.rest.url, symm_id, group_id)
        return self.rest.get(target_uri)

    def get_replica_storagegroup_srdfgroups(self, symm_id, group_id):
        target_uri = "%s/82/replication/symmetrix/%s/storagegroup/%s/rdf_group" % (self.rest.url, symm_id, group_id)
        return self.rest.get(target_uri)

    def create_replica_storagegroup_srdf(self, symm_id, group_id, params_dict):
        target_uri = "%s/82/replication/symmetrix/%s/storagegroup/%s/rdf_group" % (self.rest.url, symm_id, group_id)
        return self.rest.post(target_uri, params_dict)

    def get_replica_storagegroup_srdfgroup(self, symm_id, group_id, rdfg_id):
        target_uri = "%s/82/replication/symmetrix/%s/storagegroup/%s/rdf_group/%s" % (self.rest.url, symm_id, group_id, rdfg_id)
        return self.rest.get(target_uri)

    def edit_replica_storagegroup_srdfgroup(self, symm_id, group_id, rdfg_id):
        target_uri = "%s/82/replication/symmetrix/%s/storagegroup/%s/rdf_group/%s" % (self.rest.url, symm_id, group_id, rdfg_id)
        return self.rest.put(target_uri)

    def delete_replica_storagegroup_srdfgroup(self, symm_id, group_id, rdfg_id, params_dict):
        target_uri = "%s/82/replication/symmetrix/%s/storagegroup/%s/rdf_group/%s" % (self.rest.url, symm_id, group_id, rdfg_id)
        return self.rest.delete(target_uri, params_dict)

    def create_replica_storagegroup_snapshot(self, symm_id, group_id, params_dict):
        target_uri = "%s/82/replication/symmetrix/%s/storagegroup/%s/snapshot" % (self.rest.url, symm_id, group_id)
        return self.rest.post(target_uri, params_dict)

    def recreate_replica_storagegroup_snapshot(self, symm_id, group_id, snap_id, params_dict):
        target_uri = "%s/82/replication/symmetrix/%s/storagegroup/%s/snapshot/%s/generation" % (self.rest.url, symm_id, group_id, snap_id)
        return self.rest.post(target_uri, params_dict)

    def get_replica_array_capabilities(self):
        target_uri = "%s/replication/capabilities/symmetrix" % (self.rest.url)
        return self.rest.get(target_uri)

    def get_replica_devicegroups(self):
        target_uri = "%s/replication/devicegroup" % (self.rest.url)
        return self.rest.get(target_uri)

    def get_replica_devicegroup(self, group_id):
        target_uri = "%s/replication/devicegroup/%s" % (self.rest.url, group_id)
        return self.rest.get(target_uri)

    def edit_replica_devicegroup(self, group_id, params_dict):
        target_uri = "%s/replication/devicegroup/%s" % (self.rest.url, group_id)
        return self.rest.put(target_uri, params_dict)

    def get_replica_devicegroup_rdfgroups(self, group_id):
        target_uri = "%s/replication/devicegroup/%s/rdf_group" % (self.rest.url, group_id)
        return self.rest.get(target_uri)

    def get_replica_arrays(self):
        target_uri = "%s/replication/symmetrix" % (self.rest.url)
        return self.rest.get(target_uri)

    def get_replica_array(self, symm_id):
        target_uri = "%s/replication/symmetrix/%s" % (self.rest.url, symm_id)
        return self.rest.get(target_uri)

    def get_replica_array_rdfgroups(self, symm_id):
        target_uri = "%s/replication/symmetrix/%s/rdf_group"% (self.rest.url, symm_id)
        return self.rest.get(target_uri)

    def get_replica_array_rdfgroup(self, symm_id, rdfg_num):
        target_uri = "%s/replication/symmetrix/%s/rdf_group/%s" (self.rest.url, symm_id, rdfg_num)
        return self.rest.get(target_uri)

    def get_replica_array_storagegroups(self, symm_id):
        target_uri = "%s/replication/symmetrix/%s/storagegroup" (self.rest.url, symm_id )
        return self.rest.get(target_uri)

    def get_replica_array_storagegroup(self, symm_id, group_id):
        target_uri = "%s/replication/symmetrix/%s/storagegroup/%s" (self.rest.url, symm_id, group_id)
        return self.rest.get(target_uri)

    def get_replica_array_storagegroup_snaps(self, symm_id, group_id):
        target_uri = "%s/replication/symmetrix/%s/storagegroup/%s/snapshot" (self.rest.url, symm_id, group_id)
        return self.rest.get(target_uri)

    def create_replica_array_storagegroup_snaps(self, symm_id, group_id, params_dict):
        target_uri = "%s/replication/symmetrix/%s/storagegroup/%s/snapshot" (self.rest.url, symm_id, group_id)
        return self.rest.post(target_uri, params_dict)

    def get_replica_array_storagegroup_snap(self, symm_id, group_id, snap_id):
        target_uri = "%s/replication/symmetrix/%s/storagegroup/%s/snapshot/%s" (self.rest.url, symm_id, group_id, snap_id)
        return self.rest.get(target_uri)

    def recreate_replica_array_storagegroup_snaps(self, symm_id, group_id, snap_id, params_dict):
        target_uri = "%s/replication/symmetrix/%s/storagegroup/%s/snapshot/%s/generation" (self.rest.url, symm_id, group_id, snap_id)
        return self.rest.post(target_uri, params_dict)

    def get_replica_array_storagegroup_snaps(self, symm_id, group_id, snap_id):
        target_uri = "%s/replication/symmetrix/%s/storagegroup/%s/snapshot/%s/generation" (self.rest.url, symm_id, group_id, snap_id)
        return self.rest.get(target_uri)

    def get_replica_array_storagegroup_snap_version(self, symm_id, group_id, snap_id, version_id):
        target_uri = "%s/replication/symmetrix/%s/storagegroup/%s/snapshot/%s/generation/%s" (self.rest.url, symm_id, group_id, snap_id, version_id)
        return self.rest.get(target_uri)

    def edit_replica_array_storagegroup_snap_version(self, symm_id, group_id, snap_id, version_id, params_dict):
        target_uri = "%s/replication/symmetrix/%s/storagegroup/%s/snapshot/%s/generation/%s" (self.rest.url, symm_id, group_id, snap_id, version_id)
        return self.rest.put(target_uri, params_dict)

    def delete_replica_array_storagegroup_snap_version(self, symm_id, group_id, snap_id, version_id):
        target_uri = "%s/replication/symmetrix/%s/storagegroup/%s/snapshot/%s/generation/%s" (self.rest.url, symm_id, group_id, snap_id, version_id)
        return self.rest.delete(target_uri)


    ######################################
    ## SLO PROVISIONING Resource group
    ######################################

    def get_slo_arrays(self):
        target_uri = "%s/82/sloprovisioning/symmetrix" % (self.rest.url)
        return self.rest.get(target_uri)

    def get_slo_array(self, array_id):
        target_uri = "%s/82/sloprovisioning/symmetrix/%s" % (self.rest.url, array_id)
        return self.rest.get(target_uri)

    def get_slo_array_directors(self, array_id):
        target_uri = "%s/sloprovisioning/symmetrix/%s/director" % (self.rest.url, array_id)
        return self.rest.get(target_uri)

    def get_slo_array_director(self, array_id, director_id):
        target_uri = "%s/sloprovisioning/symmetrix/%s/director/%s" % (self.rest.url, array_id, director_id)
        return self.rest.get(target_uri)

    def get_slo_array_director_ports(self, array_id, director_id, params_dict=None):
        target_uri = "%s/sloprovisioning/symmetrix/%s/director/%s/port" % (self.rest.url, array_id, director_id)
        return self.rest.get(target_uri, params_dict)

    def get_slo_array_port(self, array_id, director_id, port_id):
        target_uri = "%s/sloprovisioning/symmetrix/%s/director/%s/port/%s" % (self.rest.url, array_id, director_id, port_id)
        return self.rest.get(target_uri)

    def get_slo_array_hosts(self, array_id, params_dict=None):
        target_uri = "%s/sloprovisioning/symmetrix/%s/host" % (self.rest.url, array_id)
        return self.rest.get(target_uri, params_dict)

    def create_slo_array_host(self, array_id, params_dict):
        target_uri = "%s/sloprovisioning/symmetrix/%s/host" % (self.rest.url, array_id)
        return self.rest.post(target_uri, params_dict)

    def get_slo_array_host(self, array_id, host_id):
        target_uri = "%s/sloprovisioning/symmetrix/%s/host/%s" % (self.rest.url, array_id, host_id)
        return self.rest.get(target_uri)

    def edit_slo_array_host(self, array_id, host_id, params_dict):
        target_uri = "%s/sloprovisioning/symmetrix/%s/host/%s" % (self.rest.url, array_id, host_id)
        return self.rest.put(target_uri, params_dict)

    def delete_slo_array_host(self, array_id, host_id):
        target_uri = "%s/sloprovisioning/symmetrix/%s/host/%s" % (self.rest.url, array_id, host_id)
        return self.rest.delete(target_uri)

    def get_slo_array_hostgroups(self, array_id, params_dict=None):
        target_uri = "%s/sloprovisioning/symmetrix/%s/hostgroup" % (self.rest.url, array_id)
        return self.rest.get(target_uri, params_dict)

    def create_slo_array_hostgroup(self, array_id, params_dict):
        target_uri = "%s/sloprovisioning/symmetrix/%s/hostgroup" % (self.rest.url, array_id)
        return self.rest.post(target_uri, params_dict)

    def get_slo_array_hostgroup(self, array_id, group_id):
        target_uri = "%s/sloprovisioning/symmetrix/%s/hostgroup/%s" % (self.rest.url, array_id, group_id)
        return self.rest.get(target_uri)

    def edit_slo_array_hostgroup(self, array_id, group_id, params_dict):
        target_uri = "%s/sloprovisioning/symmetrix/%s/hostgroup/%s" % (self.rest.url, array_id, group_id)
        return self.rest.put(target_uri, params_dict)

    def delete_slo_array_hostgroup(self, array_id, group_id):
        target_uri = "%s/sloprovisioning/symmetrix/%s/hostgroup/%s" % (self.rest.url, array_id, group_id)
        return self.rest.delete(target_uri)

    def get_slo_array_initiators(self, array_id, params_dict=None):
        target_uri = "%s/sloprovisioning/symmetrix/%s/initiator" % (self.rest.url, array_id)
        return self.rest.get(target_uri, params_dict)

    def get_slo_array_initiator(self, array_id, initiator_id):
        target_uri = "%s/sloprovisioning/symmetrix/%s/initiator/%s" % (self.rest.url, array_id, initatorId)
        return self.rest.get(target_uri)

    def edit_slo_array_initiator(self, array_id, initiator_id, params_dict):
        target_uri = "%s/sloprovisioning/symmetrix/%s/initiator/%s" % (self.rest.url, array_id, initatorId)
        return self.rest.put(target_uri, params_dict)

    def get_slo_array_maskingviews(self, array_id, params_dict=None):
        target_uri = "%s/sloprovisioning/symmetrix/%s/maskingview" % (self.rest.url, array_id)
        return self.rest.get(target_uri, params_dict)

    def create_slo_array_maskingviews(self, array_id, params_dict):
        target_uri = "%s/sloprovisioning/symmetrix/%s/maskingview" % (self.rest.url, array_id)
        return self.rest.post(target_uri, params_dict)

    def get_slo_arary_maskingview(self, array_id, mv_id):
        target_uri = "%s/sloprovisioning/symmetrix/%s/maskingview/%s" % (self.rest.url, array_id, mv_id)
        return self.rest.get(target_uri)

    def edit_slo_arary_maskingview(self, array_id, mv_id, params_dict):
        target_uri = "%s/sloprovisioning/symmetrix/%s/maskingview/%s" % (self.rest.url, array_id, mv_id)
        return self.rest.put(target_uri, params_dict)

    def delete_slo_arary_maskingview(self, array_id, mv_id):
        target_uri = "%s/sloprovisioning/symmetrix/%s/maskingview/%s" % (self.rest.url, array_id, mv_id)
        return self.rest.delete(target_uri)

    def get_slo_array_maskingview_connections(self, array_id, mv_id, params_dict=None):
        target_uri = "%s/sloprovisioning/symmetrix/%s/maskingview/%s/connections" % (self.rest.url, array_id, mv_id)
        return self.rest.get(target_uri, params_dict)

    def get_slo_array_ports(self, array_id, params_dict=None):
        target_uri = "%s/sloprovisioning/symmetrix/%s/port" % (self.rest.url, array_id)
        return self.rest.get(target_uri, params_dict)

    def get_slo_array_portgroups(self, array_id, params_dict=None):
        target_uri = "%s/sloprovisioning/symmetrix/%s/portgroup" % (self.rest.url, array_id)
        return self.rest.get(target_uri, params_dict)

    def create_slo_array_portgroup(self, array_id, params_dict):
        target_uri = "%s/sloprovisioning/symmetrix/%s/portgroup" % (self.rest.url, array_id)
        return self.rest.post(target_uri, params_dict)

    def get_slo_array_portgroup(self, array_id, portgroup_id):
        target_uri = "%s/sloprovisioning/symmetrix/%s/portgroup/%s" % (self.rest.url, array_id, portgroup_id)
        return self.rest.get(target_uri)

    def edit_slo_array_portgroup(self, array_id, portgroup_id, params_dict):
        target_uri = "%s/sloprovisioning/symmetrix/%s/portgroup/%s" % (self.rest.url, array_id, portgroup_id)
        return self.rest.get(target_uri, params_dict)

    def delete_slo_array_portgroup(self, array_id, portgroup_id):
        target_uri = "%s/sloprovisioning/symmetrix/%s/portgroup/%s" % (self.rest.url, array_id, portgroup_id)
        return self.rest.delete(target_uri)

    def get_slo_array_slos(self, array_id, params_dict=None):
        target_uri = "%s/82/sloprovisioning/symmetrix/%s/slo" % (self.rest.url, array_id)
        return self.rest.get(target_uri, params_dict)

    def get_slo_array_slo(self, array_id, slo_id):
        target_uri = "%s/sloprovisioning/symmetrix/%s/slo/%s" % (self.rest.url, array_id, slo_id)
        return self.rest.get(target_uri)

    def edit_slo_array_slo(self, array_id, slo_id, params_dict):
        target_uri = "%s/sloprovisioning/symmetrix/%s/slo/%s" % (self.rest.url, array_id, slo_id)
        return self.rest.put(target_uri, params_dict)

    def get_slo_array_splits(self, array_id):
        target_uri = "%s/82/sloprovisioning/symmetrix/%s/split" % (self.rest.url, array_id)
        return self.rest.get(target_uri)

    def get_slo_array_split(self, array_id, split_id):
        target_uri = "%s/82/sloprovisioning/symmetrix/%s/split/%s" % (self.rest.url, array_id, split_id)
        return self.rest.get(target_uri)

    def get_slo_array_split_cuimages(self, array_id, split_id):
        target_uri = "%s/82/sloprovisioning/symmetrix/%s/split/%s/cuimage" % (self.rest.url, array_id, split_id)
        return self.rest.get(target_uri)

    def create_slo_array_split_cuimages(self, array_id, split_id, params_dict):
        target_uri = "%s/82/sloprovisioning/symmetrix/%s/split/%s/cuimage" % (self.rest.url, array_id, split_id)
        return self.rest.post(target_uri, params_dict)

    def get_slo_array_split_cuimage(self, array_id, split_id, cu_id):
        target_uri = "%s/82/sloprovisioning/symmetrix/%s/split/%s/cuimage/%s" % (self.rest.url, array_id, split_id, cu_id)
        return self.rest.get(target_uri)

    def edit_slo_array_split_cuimage(self, array_id, split_id, cu_id, params_dict):
        target_uri = "%s/82/sloprovisioning/symmetrix/%s/split/%s/cuimage/%s" % (self.rest.url, array_id, split_id, cu_id)
        return self.rest.put(target_uri, params_dict)

    def get_slo_array_split_cuimage_volumes(self, array_id, split_id, cu_id):
        target_uri = "%s/82/sloprovisioning/symmetrix/%s/split/%s/cuimage/%s/volume" % (self.rest.url, array_id, split_id, cu_id)
        return self.rest.get(target_uri)

    def get_slo_array_split_cuimage_volume(self, array_id, split_id, cu_id, vol_id):
        target_uri = "%s/82/sloprovisioning/symmetrix/%s/split/%s/cuimage/%s/volume/%s" % (self.rest.url, array_id, split_id, cu_id, vol_id)
        return self.rest.get(target_uri)

    def provision_slo_array_split(self, array_id, split_id, params_dict):
        target_uri = "%s/82/sloprovisioning/symmetrix/%s/split/%s/storageProvisioningToHost" % (self.rest.url, array_id, split_id)
        return self.rest.post(target_uri, params_dict)

    def get_slo_array_srps(self, array_id, params_dict=None):
        target_uri = "%s/82/sloprovisioning/symmetrix/%s/srp" % (self.rest.url, array_id)
        return self.rest.get(target_uri, params_dict)

    def get_slo_array_srp(self, array_id, srp_id):
        target_uri = "%s/sloprovisioning/symmetrix/%s/srp/%s" % (self.rest.url, array_id, srp_id)
        return self.rest.get(target_uri)

    def get_slo_array_storagegroups(self, array_id, params_dict=None):
        target_uri = "%s/82/sloprovisioning/symmetrix/%s/storagegroup" % (self.rest.url, array_id)
        return self.rest.get(target_uri, params_dict)

    def create_slo_array_storagegroup(self, array_id, params_dict):
        target_uri = "%s/82/sloprovisioning/symmetrix/%s/storagegroup" % (self.rest.url, array_id)
        return self.rest.post(target_uri, params_dict)

    def get_slo_array_storagegroup(self, array_id, sg_id):
        target_uri = "%s/sloprovisioning/symmetrix/%s/storagegroup/%s" % (self.rest.url, array_id, sg_id)
        return self.rest.get(target_uri)

    def edit_slo_array_storagegroup(self, array_id, sg_id, params_dict):
        target_uri = "%s/82/sloprovisioning/symmetrix/%s/storagegroup/%s" % (self.rest.url, array_id, sg_id)
        return self.rest.put(target_uri, params_dict)

    def delete_slo_array_storagegroup(self, array_id, sg_id):
        target_uri = "%s/sloprovisioning/symmetrix/%s/storagegroup/%s" % (self.rest.url, array_id, sg_id)
        return self.rest.delete(target_uri)

    def get_slo_array_volumes(self, array_id, params_dict=None):
        target_uri = "%s/82/sloprovisioning/symmetrix/%s/volume" % (self.rest.url, array_id)
        return self.rest.get(target_uri, params_dict)

    def get_slo_array_volume(self, array_id, volume_id):
        target_uri = "%s/82/sloprovisioning/symmetrix/%s/volume/%s" % (self.rest.url, array_id, volume_id)
        return self.rest.get(target_uri)

    def delete_slo_array_volume(self, array_id, volume_id):
        target_uri = "%s/sloprovisioning/symmetrix/%s/volume/%s" % (self.rest.url, array_id, volume_id)
        return self.rest.delete(target_uri)

    def get_slo_array_workloads(self, array_id):
        target_uri = "%s/sloprovisioning/symmetrix/%s/workloadtype" % (self.rest.url, array_id)
        return self.rest.get(target_uri)


    ######################################
    ## SYSTEM Resource group
    ######################################

    def get_alert_summary(self):
        target_uri = "%s/82/system/alert_summary" % (self.rest.url)
        return self.rest.get(target_uri)

    def get_alerts(self):
        target_uri = "%s/system/alert" % (self.rest.url)
        return self.rest.get(target_uri)

    ################
    ## queries for a specified Alert
    ################
    def get_alert(self, array_id):
        target_uri = "%s/system/alert/%s" % (self.rest.url, array_id)
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
    def get_job(self, array_id):
        target_uri = "%s/system/job/%s" % (self.rest.url, array_id)
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
    def get_array(self, array_id):
        target_uri = "%s/system/symmetrix/%s" % (self.rest.url, array_id)
        return self.rest.get(target_uri)

    ################
    ## get a list of All Alert ids for a specific array id
    ################
    def get_array_alerts(self, array_id):
        target_uri = "%s/system/symmetrix/%s/alert" % (self.rest.url, array_id)
        return self.rest.get(target_uri)

    ################
    ## queries for a specified Alert on a specified array
    ################
    def get_array_alert(self, array_id, alert_id):
        target_uri = "%s/system/symmetrix/%s/alert/%s" % (self.rest.url, array_id, alert_id)
        return self.rest.get(target_uri)

    ################
    ## queries for a list of Job ids on a specified array
    ################
    def get_array_jobs(self, array_id):
        target_uri = "%s/system/symmetrix/%s/job" % (self.rest.url, array_id)
        return self.rest.get(target_uri)

    ################
    ## queries for a specified job on a specified array
    ################
    def get_array_job(self, array_id, job_id):
        target_uri = "%s/system/symmetrix/%s/job/%s" % (self.rest.url, array_id, job_id)
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

    def get_vvol_arrays(self):
        target_uri = "%s/81/vvol/symmetrix" % (self.rest.url)
        return self.rest.get(target_uri)

    def get_vvol_array(self, array_id):
        target_uri = "%s/81/vvol/symmetrix/%s" % (self.rest.url, array_id)
        return self.rest.get(target_uri)

    def get_vvol_array_protocolendpoints(self, array_id, params_dict=None):
        target_uri = "%s/81/vvol/symmetrix/%s/protocolendpoint" % (self.rest.url, array_id)
        return self.rest.get(target_uri, params_dict)

    def create_vvol_array_maskingview(self, array_id, params_dict):
        target_uri = "%s/81/vvol/symmetrix/%s/protocolendpoint" % (self.rest.url, array_id)
        return self.rest.post(target_uri, params_dict)

    def get_vvol_array_protocolendpoint(self, array_id, proto_id):
        target_uri = "%s/81/vvol/symmetrix/%s/protocolendpoint/%s" % (self.rest.url, array_id, proto_id)
        return self.rest.get(target_uri)

    def get_vvol_array_storagecontainers(self, array_id, params_dict=None):
        target_uri = "%s/81/vvol/symmetrix/%s/storagecontainer" % (self.rest.url, array_id)
        return self.rest.get(target_uri, params_dict)

    def create_vvol_array_storagecontainer(self, array_id, params_dict):
        target_uri = "%s/81/vvol/symmetrix/%s/storagecontainer" % (self.rest.url, array_id)
        return self.rest.post(target_uri, params_dict)

    def get_vvol_array_storagecontainer(self, array_id, storcont_id):
        target_uri = "%s/81/vvol/symmetrix/%s/storagecontainer/%s" % (self.rest.url, array_id, storcont_id)
        return self.rest.get(target_uri)

    def edit_vvol_array_storagecontainer(self, array_id, storcont_id, params_dict):
        target_uri = "%s/81/vvol/symmetrix/%s/storagecontainer/%s" % (self.rest.url, array_id, storcont_id)
        return self.rest.put(target_uri, params_dict)

    def delete_vvol_array_storagecontainer(self, array_id, storcont_id):
        target_uri = "%s/81/vvol/symmetrix/%s/storagecontainer/%s" % (self.rest.url, array_id, storcont_id)
        return self.rest.delete(target_uri)

    def get_vvol_array_storagecontainer_storageresources(self, array_id, storcont_id, params_dict=None):
        target_uri = "%s/81/vvol/symmetrix/%s/storagecontainer/%s/storageresource" % (self.rest.url, array_id, storcont_id)
        return self.rest.get(target_uri, params_dict)

    def get_vvol_array_storagecontainer_storageresource(self, array_id, storcont_id, storresource_id):
        target_uri = "%s/81/vvol/symmetrix/%s/storagecontainer/%sstorageresource/%s" % (self.rest.url, array_id, storcont_id, storresource_id)
        return self.rest.get(target_uri)

    def edit_vvol_array_storagecontainer_storageresource(self, array_id, storcont_id, storresource_id, params_dict):
        target_uri = "%s/81/vvol/symmetrix/%s/storagecontainer/%sstorageresource/%s" % (self.rest.url, array_id, storcont_id, storresource_id)
        return self.rest.put(target_uri, params_dict)

    def get_vvol_array_vasaprovider(self, array_id):
        target_uri = "%s/82/vvol/symmetrix/%s/vasaprovider" % (self.rest.url, array_id)
        return self.rest.get(target_uri)

    def create_vvol_array_vasaprovider(self, array_id, params_dict):
        target_uri = "%s/82/vvol/symmetrix/%s/vasaprovider" % (self.rest.url, array_id)
        return self.rest.post(target_uri, params_dict)

    def edit_vvol_array_vasaprovider(self, array_id, params_dict):
        target_uri = "%s/82/vvol/symmetrix/%s/vasaprovider" % (self.rest.url, array_id)
        return self.rest.put(target_uri, params_dict)

    def delete_vvol_array_vasaprovider(self, array_id):
        target_uri = "%s/82/vvol/symmetrix/%s/vasaprovider" % (self.rest.url, array_id)
        return self.rest.delete(target_uri)

    ######################################
    ## WORKLOAD Resource group
    ######################################

    def get_workload_array(self, array_id):
        target_uri = "%s/82/wlp/symmetrix/%s" % (self.rest.url, array_id)
        return self.rest.get(target_uri)

    def edit_workload_array(self, array_id, params_dict):
        target_uri = "%s/82/wlp/symmetrix/%s" % (self.rest.url, array_id)
        return self.rest.put(target_uri, params_dict)

    def get_workload_array_admissibility(self, array_id, params_dict):
        target_uri = "%s/82/wlp/symmetrix/%s/admissibility" % (self.rest.url, array_id)
        return self.rest.post(target_uri, params_dict)

    def get_workload_array_sgcompliances(self, array_id):
        target_uri = "%s/82/wlp/symmetrix/%s/compliance" % (self.rest.url, array_id)
        return self.rest.get(target_uri)

    def get_workload_array_headroom(self, array_id, params_dict=None):
        target_uri = "%s/82/wlp/symmetrix/%s/headroom" % (self.rest.url, array_id)
        return self.rest.get(target_uri, params_dict)

    def get_workload_array_referenceworkloads(self, array_id):
        target_uri = "%s/82/wlp/symmetrix/%s/referenceworkload" % (self.rest.url, array_id)
        return self.rest.get(target_uri)

    def create_workload_array_referenceworkload(self, array_id, params_dict):
        target_uri = "%s/82/wlp/symmetrix/%s/referenceworkload" % (self.rest.url, array_id)
        return self.rest.post(target_uri, params_dict)

    def get_workload_array_referenceworkload(self, array_id, work_id, params_dict=None):
        target_uri = "%s/82/wlp/symmetrix/%s/referenceworkload/%s" % (self.rest.url, array_id, work_id)
        return self.rest.get(target_uri, params_dict)

    def delete_workload_array_referenceworkload(self, array_id, work_id):
        target_uri = "%s/82/wlp/symmetrix/%s/referenceworkload/%s" % (self.rest.url, array_id, work_id)
        return self.rest.delete(target_uri)

    def edit_workload_array_referenceworkload(self, array_id, work_id, params_dict):
        target_uri = "%s/82/wlp/symmetrix/%s/referenceworkload/%s" % (self.rest.url, array_id, work_id)
        return self.rest.put(target_uri, params_dict)

    def get_workload_array_utilization(self, array_id, params_dict=None):
        target_uri = "%s/82/wlp/symmetrix/%s/utilization" % (self.rest.url, array_id)
        return self.rest.get(target_uri, params_dict)

    def get_workload_array_capabilities(self):
        target_uri = "%s/wlp/capabilities/symmetrix" % (self.rest.url)
        return self.rest.get(target_uri)

    def get_workload_array_capability(self, symm_id):
        target_uri = "%s/wlp/capabilities/symmetrix/%s" % (self.rest.url, symm_id)
        return self.rest.get(target_uri)

    def get_workload_arrays(self):
        target_uri = "%s/wlp/symmetrix" % (self.rest.url)
        return self.rest.get(target_uri)

    def get_workload_array_characterizations(self, symm_id, params_dict):
        target_uri = "%s/wlp/symmetrix/%s/characterize" % (self.rest.url, symm_id)
        return self.rest.post(target_uri, params_dict)

    def get_workload_array_slo_characterize(self, symm_id, capacity_gb):
        target_uri = "%s/wlp/symmetrix/%s/characterize_slo/capacity/%s" % (self.rest.url, symm_id, capacity_gb)
        return self.rest.post(target_uri)

    def get_workload_characterize_slo(self, symm_id, capacity_gb, slo_id):
        target_uri = "%s/wlp/symmetrix/%s/characterize_slo/capacity/%s/slo/%s" % (self.rest.url, symm_id, capacity_gb, slo_id)
        return self.rest.get(target_uri)

    def get_workload_array_storagegroups(self, symm_id):
        target_uri = "%s/wlp/symmetrix/%s/storagegroup" % (self.rest.url, symm_id)
        return self.rest.get(target_uri)

    def get_workload_array_storagegroup(self, symm_id, group_id):
        target_uri = "%s/wlp/symmetrix/%s/storagegroup/%s" % (self.rest.url, symm_id, group_id)
        return self.rest.get(target_uri)

    def edit_workload_array_storagegroup(self, symm_id, group_id, params_dict):
        target_uri = "%s/wlp/symmetrix/%s/storagegroup/%s" % (self.rest.url, symm_id, group_id)
        return self.rest.put(target_uri, params_dict)
