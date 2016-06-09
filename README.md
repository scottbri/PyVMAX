# PyVMAX REST API for EMC VMAX
Implementation of a REST client python module for EMC Unisphere for VMAX

Includes a VmaxApi class that simplifies the consumption of EMC VMAX REST API.  The package also implements a number of example scripts that consume REST API as a demonstration of functionality.

# INSTALLATION
Download the python files and copy them into your working directory.   
Requires the 'requests' JSON parsing package.
```
$ pip install requests
$ git clone https://github.com/scottbri/PyVMAX
$ cd pyvmax
$ cp -r pyvmax /your/project/dir
```

# USAGE
PyVMAX is primarily a representation of the EMC Unisphere for VMAX API as a Python module.  It's very simple to use.  In your script just import the module, issue the connect() method and make your first API call:
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
* This example shows how to report the API last call resopnse time and overall average response time as well

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

### example_capacities.py
* Queries the Unisphere server and builds a list of all known VMAX3 arrays.  
* Then for each, we gather capacity information at the array, SRP, and Storage Group levels building a big data structure
* Finally, it reports the array level information into a simple comma delimited table 
```
usage: example_capacities.py [-h] -url URL -user USER -passwd PASSWD

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

You can download api documentation by pointing your browser to URL/univmax/restapi/docs (URL as above):
eg: https://10.0.0.1:8443/univmax/restapi/docs

# TODO
* fully implement the full API about 90% complete
  * still have replication and workload resource groups to implement
  * implement the latest v82 calls in SLO Resource group

# API ISSUES / WISHLIST
* api sometimes returns list when guaranteed only a single element returned
* can't see how to report on subscribed capacity in thin provisioned arrays
