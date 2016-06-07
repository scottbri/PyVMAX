# PyVMAX REST API for EMC VMAX
Example implementation of a python REST client for EMC Unisphere for VMAX

Includes a Restful class that simplifies the consumption of EMC VMAX REST API.  The package also implements an example python client of the Unisphere REST API as a demonstration of functionality.

# INSTALLATION
Download the python files and copy them into your working directory.  Requires the 'requests' JSON parsing package.
```
pip install requests
```

# USAGE
PyVMAX is primarily a representation of the EMC Unisphere for VMAX API as a Python module.  It's very simple to use, just:
```
import pyvmax
vmax_api = pyvmax.connect(URL, USER, PASSWORD)
unisphere_version = vmax_api.get_version()
```

URL is an https FQDN or IP address of your Unisphere server, specifying port 8443 (typically)
for example:  https://192.168.1.1:8443
USER and PASSWD are your unisphere credentials used to login to the GUI

Also included in the package are some functional example python scripts using the API described below.

### example.py
* Queries the Unisphere server and builds a list of all known VMAX arrays.  
* Then for each, we gather thin pool data for VMAX 2 and older, or SRP and Storage Group data for VMAX3.
* In the end, the data structure is merely printed out for your enjoyment.

```
usage: example.py [-h] -url URL -user USER -passwd PASSWD

Example implementation of a Python REST client for EMC Unisphere for VMAX.

optional arguments:
  -h, --help      show this help message and exit

Required arguments:
  -url URL        Base Unisphere URL. e.g. https://10.0.0.1:8443
  -user USER      Unisphere username. e.g. smc
  -passwd PASSWD  Unisphere password. e.g. smc
```

### example_performance.py
* Queries the Unisphere server and builds a list of all known VMAX arrays.  
* Then for each, we gather the last hour of a few example performance metrics 
* As before for your amusement, we merely print out the data structure, but suggest you do something more useful with it

```
usage: example_performance.py [-h] -url URL -user USER -passwd PASSWD

Example implementation of a Python REST client for EMC Unisphere for VMAX
performance statistics.

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

You can download api documentation by pointing your browser to URL/univmax/restapi/docs (URL as above):
eg: https://10.0.0.1:8443/univmax/restapi/docs

# TODO
* fully implement the full API
  * still have replication and workload resource groups to implement
  * rationalize function names between provisioning and SLO arrays
  * rationalize strategy for supporting api versions ongoing and best use of newer api paths
  * implement the latest v82 calls in SLO Resource group
* implement additional functional examples:
  * duplicate some reporting that happens now for performance and configuration analysis (examples needed)
  * incorporate FAST Pool subscription reports per http://www.scottbrightwell.org/2013/11/21/some-emc-vmax-storage-reporting-formulas/
  * example performance outputs to csv format 


# API ISSUES / WISHLIST
* api sometimes returns list when guaranteed only a single element returned
* can't see how to report on subscribed capacity in thin provisioned arrays
