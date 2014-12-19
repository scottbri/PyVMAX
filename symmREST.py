#!/usr/bin/python

import requests, json, pprint, time, socket

#target_url = "https://10.5.132.58:8443/univmax/restapi/performance/Array/metrics"
#target_url = "https://192.168.250.250:8443/univmax/restapi/system/version"
#target_url = "https://192.168.250.250:8443/univmax/restapi/system/symmetrix"
target_url = "https://192.168.250.250:8443/univmax/restapi/sloprovisioning/symmetrix/000197400230/storagegroup/LP01"

requestObj = {'arrayParam': 
            {'endDate': int(time.time()*1000), #End time to specify is now.
             'startDate': int(time.time()*1000)-(3600*1000), #start time is 60 minutes before that
             'metrics': ['IO_RATE'], #array of what metrics we want
             'symmetrixId': '000194900728' #symmetrix ID (full 12 digits)
            }
          }
          
#turn this into a JSON string
requestJSON = json.dumps(requestObj, sort_keys=True, indent=4) 
#print requestJSON

#set the headers for how we want the response
headers = {'content-type': 'application/json','accept':'application/json'} 

#make the actual request, specifying the URL, the JSON from above, standard basic auth, the headers and not to verify the SSL cert.
#r = requests.post(target_url, requestJSON, auth=('smc', 'smc'), headers=headers, verify=False)
r = requests.get(target_url, auth=('smc', 'smc'), headers=headers, verify=False)

#take the raw response text and deserialize it into a python object.
try:
    responseObj = json.loads(r.text)
except:
    print "Exception"
    print r.text
print json.dumps(responseObj, sort_keys=False, indent=2)

#make sure we actually get a value back.
##data = None
#if len(responseObj["iterator"]["resultList"]["result"]) > 0:
#    data = float(responseObj["iterator"]["resultList"]["result"][0]['IO_RATE'])
#    line = 'Symmetrix.System.IO_RATE %d %d' % (data, int(time.time()))
#    print line
#else:
#    print "Short response"
