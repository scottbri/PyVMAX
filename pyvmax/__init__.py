__version__ = "0.3"

from .client import UnisphereClient

def connect (url, username, password):

    return UnisphereClient(url, username, password)

__all__ = ['connect']
