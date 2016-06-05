__version__ = "0.3"

# import importlib
from .Restful import Restful
from .VmaxApi import VmaxApi


def connect(url, username, password):

    rest_client =  Restful(url, username, password)
    return VmaxApi(rest_client, url)

'''
# potential code to solve the dilemma of multiple API versions
# if we could query the univmax verison from REST up front, and then decide
# which VmaxApi module or class to load dynamically, we could keep the various
# api versions in separate files for easier management

    target_uri = "%s/system/version" % (url)
    version_response = rest_client.get(target_uri)
    if 'version' in version_response:
        univmax_version = version_response.get('version')

    SUPPORTED_VERSIONS = {'V8.2.0.5' : '.VmaxApi82',
                          'V8.0.1.5' : '.VmaxApi80'}

    VmaxApi = getattr(importlib.import_module(SUPPORTED_VERSIONS.get(univmax_version)), "VmaxApi")
'''

__all__ = ['connect']
