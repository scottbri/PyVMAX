__version__ = "0.8.2"

from pyvmax.Restful import Restful
import pyvmax.Logger 

def connect(url, username, password):

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
