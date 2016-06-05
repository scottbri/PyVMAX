__version__ = "0.3"

from .Restful import Restful
#from .VmaxApi import VmaxApi


def connect(url, username, password):

    rest_client = Restful(url, username, password)

# potential code to solve the dilemma of multiple API versions
# if we could query the univmax verison from REST up front, and then decide
# which VmaxApi module or class to load dynamically, we could keep the various
# api versions in separate files for easier management

    target_uri = "%s/univmax/restapi/system/version" % (url)
    print target_uri
    version_response = rest_client.get(target_uri)
    if 'version' in version_response:
        univmax_version = version_response.get('version')

# import the correct API module for the version of Unisphere discovered
    if univmax_version == 'V8.2.0.5':
        from .VmaxApi_v82 import VmaxApi
    elif univmax_version == 'V8.0.1.5':
        from .VmaxApi_v80 import VmaxApi
    else:
        from .VmaxApi import VmaxApi

    return VmaxApi(rest_client, url)

__all__ = ['connect']
