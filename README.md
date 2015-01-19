unisphere-rest-client
=====================

Example implementation of a python REST client for EMC Unisphere for VMAX3

Right now, code is totally for demonstration purposes only and assumes VMAX3 array

TODO
====
* add support for Unisphere <8.0.1
* investigate additional query options, replication, capacity, performance, etc.
* duplicate some reporting that happens now for performance and configuration analysis
* incorporate FAST Pool subscription reports per http://www.scottbrightwell.org/2013/11/21/some-emc-vmax-storage-reporting-formulas/
* bring in URI and credentials from outside (not hard coded)

How to use this from scratch
============================
* download Git from: 		https://github.com/msysgit/msysgit/releases/download/Git-1.9.5-preview20141217/Git-1.9.5-preview20141217.exe 
* download python from:		https://www.python.org/ftp/python/2.7.9/python-2.7.9.msi
* install Git by:		Git-1.9.5-preview20141217.exe
* get the package:  		git clone https://www.github.com/scottbri/unisphere-rest-client
* execute the deploy script: 	deploy.bat

