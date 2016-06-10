# PyVMAX REST API for EMC VMAX
Implementation of a REST client python package for EMC Unisphere for VMAX

Includes a VmaxApi class sitting in the pyvmax module that simplifies the consumption of EMC VMAX REST API.  The package also implements a number of example scripts that consume the module as a demonstration of functionality.

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
PyVMAX is an implementation of the EMC Unisphere for VMAX API as a Python package.  It's very simple to use.  In your script just import the module, issue the connect() and make your first API call:
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

### example_performance.py
* Queries the Unisphere server and builds a list of all known VMAX arrays.  
* Then for each, we gather the last hour of a few example performance metrics 
* As before for your amusement, we merely print out the data structure, but suggest you do something more useful with it

### example_capacities.py
* Queries the Unisphere server and builds a list of all known VMAX3 arrays.  
* Then for each, we gather capacity information at the array, SRP, and Storage Group levels building a big data structure
* Finally, it reports the array level information into a simple comma delimited table 
```
usage: example*.py [-h] -url URL -user USER -passwd PASSWD

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

# DOCUMENTATION
Meh, none yet. ;-)  peruse `pyvmax\VmaxApi_V82.py` to see all the available  methods.  Compare this with the EMC official API documentation you can get from Unisphere.  Get the EMC documentation by pointing your browser to `URL/univmax/restapi/docs` eg: `https://10.0.0.1:8443/univmax/restapi/docs`.


That URL will start a download of a ZIP package containing all the official documentation for the API.  It contains descriptions of all of the REST API calls, the JSON request and response formats, and if you dig far enough all the available performance metrics are there too.
