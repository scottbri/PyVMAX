"""PyVMAX is an implementation of the EMC Unisphere for VMAX API as a Python package

It's very simple to use. In your script just import the module, issue the connect() and make your first API call:
Example:
    import pyvmax
    vmax_api = pyvmax.connect(URL, USER, PASSWORD)
    unisphere_version = vmax_api.get_version()

URL is an https FQDN or IP address of your Unisphere server, specifying port 8443 (typically) for example: https://192.168.1.1:8443
USER and PASSWD are your unisphere credentials used to login to the GUI

"""
__version__ = "0.8.2"

from pyvmax.Restful import Restful
import pyvmax.Logger

def connect(url, username, password):
    """main initalizer for the module setting up base connection to API server

    Args:
        url (str): base html FQDN and port of the API server eg: http://10.0.0.1:8443
        username (str): username for basic authentication
        password (str): password for that user
    Returns:
        object of type VmaxApi
    """
    Logger.logger_setup()
    log = Logger.get_logger('pyvmax')
    log.info("beginning initial api connection")

    rest_client = Restful(url, username, password)
    target_uri = "%s/univmax/restapi/system/version" % (url)
    version_response = rest_client.get(target_uri)
    if 'version' in version_response:
        univmax_version = version_response.get('version', '')
    else:
        log.debug('Incorrect version response')

# import the correct API module for the version of Unisphere discovered
    version_major = ""
    version_minor = ""
    if '.' in univmax_version:
        _version_parts = univmax_version.split('.')
        version_major, version_minor = '.'.join(_version_parts[:2]), '.'.join(_version_parts[2:])
    if version_major == 'V8.2':
        from pyvmax.VmaxApi_v82 import VmaxApi
        log.debug('Importing VmaxApi_v82')
    elif version_major == 'V8.0':
        from pyvmax.VmaxApi_v80 import VmaxApi
        log.debug('Importing VmaxApi_v80')
    else:
        from pyvmax.VmaxApi_v82 import VmaxApi
        log.debug('Importing VmaxApi_v82')
        log.warn('Unsupported VMAX API Version', univmax_version)
        log.warn('Using latest VMAX API Version')

    return VmaxApi(rest_client, url)

__all__ = ['connect']
