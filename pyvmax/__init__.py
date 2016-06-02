__version__ = "0.3"

from .Restful import Restful
from .VmaxApi import VmaxApi

def vmax_connect(url, username, password):

    rest_client =  Restful(url, username, password)
    return VmaxApi(rest_client, url)

__all__ = ['connect']
