PyMAX REST API for EMC VMAX
===========================

Example implementation of a python REST client for EMC Unisphere for VMAX

Includes a Restful class that simplifies the consumption of EMC VMAX REST API.  The package also implements an example python client of the Unisphere REST API as a demonstration of functionality.

INSTALLATION
===========
Download the python files and copy them into your working directory.  Requires the 'requests' JSON parsing package.
```
pip install requests
```

USAGE
=====
```
usage: symmREST.py [-h] -url URL -user USER -passwd PASSWD

Example implementation of a Python REST client for EMC Unisphere for VMAX.

optional arguments:
  -h, --help      show this help message and exit

Required arguments:
  -url URL        Base Unisphere URL. e.g. https://10.0.0.1:8443
  -user USER      Unisphere username. e.g. smc
  -passwd PASSWD  Unisphere password. e.g. smc
```

URL is an https FQDN or IP address of your Unisphere server, specifying port 8443 (typically)
for example:  https://192.168.1.1:8443

USER and PASSWD are your unisphere credentials used to login to the GUI

In your own code simply import the class as follows:
```
from symmRestApi import Restful
```
Requires the 'requests' JSON parsing package 

TODO
====
* fully implement the reporting API
  * rationalize function names between provisioning and SLO arrays
* implement all available CRUD API calls
* implement additional functional examples:
  * duplicate some reporting that happens now for performance and configuration analysis
  * incorporate FAST Pool subscription reports per http://www.scottbrightwell.org/2013/11/21/some-emc-vmax-storage-reporting-formulas/
  * example performance outputs to csv format 
