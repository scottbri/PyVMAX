unisphere-rest-client
=====================

Example implementation of a python REST client for EMC Unisphere for VMAX3

Right now, code is totally for demonstration purposes only and assumes querying a VMAX3 array

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


TODO
====
* add support for Unisphere <8.0.1
* investigate additional query options, replication, capacity, performance, etc.
* duplicate some reporting that happens now for performance and configuration analysis
* incorporate FAST Pool subscription reports per http://www.scottbrightwell.org/2013/11/21/some-emc-vmax-storage-reporting-formulas/
