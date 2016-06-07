import requests
import json


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
        self.verify_ssl = verifySSL

        # set the headers for how we want the response
        self.headers = {'content-type': 'application/json', 'accept':'application/json'}

    def set_url(self, new_url):
        self.url = new_url

    def print_json(self, json_obj):
        print(json.dumps(json_obj, sort_keys=False, indent=2))

    ################
    ## make the json GET call to the public api
    ################
    def get(self, target_url, payload=None):

        try:
            response = requests.get(target_url,
                                    params=json.dumps(payload),
                                    auth=(self.user, self.password),
                                    headers=self.headers,
                                    verify=self.verify_ssl)
        except Exception:
            print("Exception:  Can't GET to API server URL:  " + target_url)
            print("Exiting")
            exit(1)

        #take the raw response text and deserialize it into a python object.
        try:
            response_object = json.loads(response.text)
        except Exception:
            print("Exception")
            print(response.text)
            return dict()

        return response_object

    ################
    ## make the json POST call to the public api
    ################
    def post(self, target_url, request_object=None):

        #make the actual request, specifying the URL, the JSON from above,
        #standard basic auth, the headers and not to verify the SSL cert.
        try:
            response = requests.post(target_url,
                                     data=json.dumps(request_object),
                                     auth=(self.user, self.password),
                                     headers=self.headers,
                                     verify=self.verify_ssl)

            #take the raw response text and deserialize it into a python object.
            try:
                response_object = json.loads(response.text)
            except Exception:
                print("Exception")
                print(response.text)
                return dict()
        except Exception:
            print("Exception:  Can't POST to API server URL:  " + target_url)
            print_json(request_object)
            print("Exiting")
            exit(1)

        return response_object


    ################
    ## make the json PUT call to the public api
    ################
    def put(self, target_url, request_object=None):

        #turn this into a JSON string
        request_json = json.dumps(request_object, sort_keys=True, indent=4)

        #make the actual request, specifying the URL, the JSON from above,
        #standard basic auth, the headers and not to verify the SSL cert.
        try:
            response = requests.put(target_url,
                                    request_json,
                                    auth=(self.user, self.password),
                                    headers=self.headers,
                                    verify=self.verify_ssl)
        except Exception:
            print("Exception:  Can't PUT to API server URL:  " + target_url)
            print_json(request_object)
            print("Exiting")
            exit(1)

        #take the raw response text and deserialize it into a python object.
        try:
            response = json.loads(response.text)
        except Exception:
            print("Exception")
            print(repsonse.text)
        return response


    ################
    ## make the json DELETE call to the public api
    ################
    def delete(self, target_url, request_object=None):

        #turn this into a JSON string
        request_json = json.dumps(request_object, sort_keys=True, indent=4)

        #make the actual request, specifying the URL, the JSON from above,
        #standard basic auth, the headers and not to verify the SSL cert.
        try:
            response = requests.delete(target_url,
                                       request_json,
                                       auth=(self.user, self.password),
                                       headers=self.headers,
                                       verify=self.verify_ssl)
        except Exception:
            print("Exception:  Can't DELETE to API server URL:  " + target_url)
            print_json(request_object)
            print("Exiting")
            exit(1)

        #take the raw response text and deserialize it into a python object.
        try:
            response = json.loads(response.text)
        except Exception:
            print("Exception")
            print(response.text)
        return response


