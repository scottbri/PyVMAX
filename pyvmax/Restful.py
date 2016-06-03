import requests, json, pprint, time, socket

# Disable warnings from untrusted server certificates
try:
    from requests.packages.urllib3.exceptions import InsecureRequestWarning
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
except Exception:
    print("Ignore messages related to insecure SSL certificates")

class Restful:

    def __init__(self, base_url, username, password, verifySSL=False):
        self.url = base_url
        self.user = username
        self.password = password
        self.verify_SSL = verifySSL

        # set the headers for how we want the response
        self.headers = {'content-type': 'application/json','accept':'application/json'}

    def setURL(self, newUrl):
        self.url = newUrl

    ################
    ## make the json GET call to the public api
    ################
    def get(self, targetUrl, payload=None):

        try:
            r = requests.get(targetUrl, params=json.dumps(payload), auth=(self.user, self.password), headers=self.headers, verify=self.verify_SSL)
        except:
            print("Exception:  Can't connect to API server URL:  " + targetUrl)
            print("Exiting")
            exit(1)

        #take the raw response text and deserialize it into a python object.
        try:
            responseObj = json.loads(r.text)
        except:
            print("Exception")
            print(r.text)

            print(responseObj.get("message", "API failed to return expected result"))
            self.jsonPrint(responseObj)
            return dict()

        return responseObj

    ################
    ## make the json POST call to the public api
    ################
    def post(self, targetUrl, requestObj=None):

        #make the actual request, specifying the URL, the JSON from above, standard basic auth, the headers and not to verify the SSL cert.
        try:
            r = requests.post(targetUrl, data=json.dumps(requestObj), auth=(self.user, self.password), headers=self.headers, verify=self.verify_SSL)
	    
	    #take the raw response text and deserialize it into a python object.
	    try:
		responseObj = json.loads(r.text)
	    except:
		print("Exception")
		print(r.text)
		return dict()
        except:
            print("Exception:  Can't POST to API server URL:  " + targetUrl)
	    self.printJSON(requestObj)
            print("Exiting")
            exit(1)

        return responseObj


    ################
    ## make the json PUT call to the public api
    ################
    def put(self, targetUrl, requestObj=None):

        #turn this into a JSON string
        requestJSON = json.dumps(requestObj, sort_keys=True, indent=4)

        #make the actual request, specifying the URL, the JSON from above, standard basic auth, the headers and not to verify the SSL cert.
        try:
            r = requests.put(targetUrl, requestJSON, auth=(self.user, self.password), headers=self.headers, verify=self.verify_ssl)
        except:
            print("Exception:  Can't connect to API server URL:  " + targetUrl)
            print("Exiting")
            exit(1)

        #take the raw response text and deserialize it into a python object.
        try:
            response = json.loads(r.text)
        except:
            print("Exception")
            print(r.text)
        return response


    ################
    ## make the json DELETE call to the public api
    ################
    def delete(self, targetUrl, requestObj=None):

        #turn this into a JSON string
        requestJSON = json.dumps(requestObj, sort_keys=True, indent=4)

        #make the actual request, specifying the URL, the JSON from above, standard basic auth, the headers and not to verify the SSL cert.
        try:
            r = requests.delete(targetUrl, requestJSON, auth=(self.user, self.password), headers=self.headers, verify=self.verify_ssl)
        except:
            print("Exception:  Can't connect to API server URL:  " + targetUrl)
            print("Exiting")
            exit(1)

        #take the raw response text and deserialize it into a python object.
        try:
            response = json.loads(r.text)
        except:
            print("Exception")
            print(r.text)
        return response


    ################
    ## print a json object nicely
    ################
    def printJSON(self, jsonObj):
    	print(json.dumps(jsonObj, sort_keys=False, indent=2))
