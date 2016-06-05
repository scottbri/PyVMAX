__version__ = "0.3"

from .Restful import Restful

def connect(url, username, password):

    rest_client = Restful(url, username, password)
    target_uri = "%s/univmax/restapi/system/version" % (url)
    version_response = rest_client.get(target_uri)
    if 'version' in version_response:
        univmax_version = version_response.get('version')

# import the correct API module for the version of Unisphere discovered

    if univmax_version == 'V8.2.0.5':
        from .VmaxApi_v82 import VmaxApi
    elif univmax_version == 'V8.0.1.7':
        from .VmaxApi_v80 import VmaxApi
    else:
        from .VmaxApi_v82 import VmaxApi
    	print('Unsupported VMAX API Version {}'.format(univmax_version))
    	print('Using VMAX API Version {}'.format())

    return VmaxApi(rest_client, url)

__all__ = ['connect']
